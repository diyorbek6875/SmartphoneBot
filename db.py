from tinydb import TinyDB, Query

class DB:
    def __init__(self,path):
        self.db = TinyDB(path)

    def get_tables(self):
        """
        To get the list of all the tables in the database
        """
        tables = self.db.tables()
        return list(tables)
        
    def get_phone(self,brand,idx):
        """
        Return phone data by brand
        args:
            brand: str
        return:
            dict
        """
        phone = self.db.table(brand)

        return phone.get(doc_id=idx)

    def get_phone_list(self,brand):
        """
        Return phone list
        """
        phone = self.db.table(brand)

        return phone.all()

    
if __name__ == "__main__":
    smartphone = DB("data.json")

    tables = smartphone.get_tables()
    print(smartphone.get_phone(tables[0], 20))
    