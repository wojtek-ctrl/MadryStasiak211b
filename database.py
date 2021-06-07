import mysql.connector as mc
class DataBase:
    def __init__(self, host = "localhost", user="root", passwd ="", database="inzynieriaoprogramowania"):
        self.mydb = mc.connect(host=host, user=user, passwd=passwd)
        self.mycursor = self.mydb.cursor()
    def querry(self, SELECT):
        self.mycursor.execute(SELECT)
        array = []
        
        for Querry in self.mycursor:
            array.append(Querry)
        return array
    def commit(self):
        self.mydb.commit()
