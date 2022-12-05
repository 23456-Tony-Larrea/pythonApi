from database.db import get_connection
from .entities.Person import Person

class PersonsModel:
    @classmethod
    def getPersons(self):
        try:
            conn = get_connection()
            persons=[]
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM persons')
                rows = cur.fetchall()
        
            for row in rows:
                persons.append(Person(row[0], row[1], row[2]).to_JSON())
            return persons
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def getPersonsId(self, id):
        try:
            conn = get_connection()
            
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM persons where id = %s', (id,))
                rows = cur.fetchone()

                person=None
                if rows is not None:
                    person=Person(rows[0],rows[1],rows[2])
                    person=person.to_JSON()
                    conn.close()
                    return person
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def add_person(self, person):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO persons (typeperson, person) VALUES (%s, %s)', (person['typeperson'], person['person']))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_person(self, person,id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('UPDATE persons SET typeperson = %s, person = %s WHERE id = %s', (person['typeperson'], person['person'],id))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_person(self, id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('DELETE FROM persons WHERE id = %s', (id,))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)