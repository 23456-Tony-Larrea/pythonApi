class Products:
    def __init__(self,id, typeproducts=None, products=None)->None:
        self.id = id
        self.typeproducts = typeproducts
        self.products = products
    
    def to_JSON(self):
        return {
            'id': self.id,
            'tipo producto': self.typeproducts,
            'producto': self.products
        }
