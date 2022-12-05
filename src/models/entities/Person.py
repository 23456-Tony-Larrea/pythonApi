class Person:
    def __init__(self,id, typeperson=None, Person=None)->None:
        self.id = id
        self.typeperson = typeperson
        self.person = Person
    
    def to_JSON(self):
        return {
            'id': self.id,
            'tipopersona': self.typeperson,
            'persona ': self.person
        }
