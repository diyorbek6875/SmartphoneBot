from tinydb import TinyDB, Query

class Cart:
    def __init__(self,cart_path:str):
        self.db = TinyDB(cart_path, indent=4)
        self.table = self.db.table('cart')

    def add(self, brand, doc_id, chat_id):
        """
        add card

        data = {
            'brand':brand,
            'doc_id': doc_id,
            chat_id: chat_id
            }
        """

    def get_cart(self, chat_id):
        pass

    def remove(self, chat_id):
        pass