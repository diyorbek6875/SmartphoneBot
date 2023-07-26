from tinydb import TinyDB, Query

class DB:
    def __init__(self,path):
        self.db = TinyDB(path)

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        
    def getPhone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """

    def get_phone_list(self,brand):
        """
        Return phone list
        """