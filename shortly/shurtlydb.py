import psycopg2, os
DATABASE_URL = os.environ['DATABASE_URL']
class Datab():
    def createConnect(self):
        #connect_str = "dbname=" + DATABASE_URL + " user='shurtlydb' host='localhost' " + \
        #          "password='shurtlyDB__123'"
        self.con = psycopg2.connect(DATABASE_URL, sslmode='require')
        #self.con = psycopg2.connect(connect_str)
        self.cursor = self.con.cursor()
    
    def closeConnection(self):
        self.cursor.close()

    def insert(self, longURL, shortURL):
        self.cursor.execute("""
         INSERT INTO shurtly 
         VALUES (%s, %s, current_date);
         """,
        (longURL, shortURL))
        self.con.commit()
    
    def selectWHERE(self, shortURL):
        self.cursor.execute("""
        SELECT * FROM shurtly where shortURL = '"""+shortURL + """'""")
        rows = self.cursor.fetchall()
        return rows