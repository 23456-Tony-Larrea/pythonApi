class Invoice:
    def __init__(self,id, typeinvoice=None, inovice=None)->None:
        self.id = id
        self.typeinvoice = typeinvoice
        self.invoice = inovice
    
    def to_JSON(self):
        return {
            'id': self.id,
            'tipo factura': self.typeinvoice,
            'factura': self.invoice
        }
