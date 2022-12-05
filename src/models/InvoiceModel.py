from database.db import get_connection
from .entities.Invoice import Invoice

class InvoicesModel:
    @classmethod
    def getInvoice(self):
        try:
            conn = get_connection()
            products=[]
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM invoices')
                rows = cur.fetchall()
        
            for row in rows:
                products.append(Invoice(row[0], row[1], row[2]).to_JSON())
            return products
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def getInvoicesId(self, id):
        try:
            conn = get_connection()
            
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM invoices where id = %s', (id,))
                rows = cur.fetchone()

                invoice=None
                if rows is not None:
                    invoice=Invoice(rows[0],rows[1],rows[2])
                    invoice=invoice.to_JSON()
                    conn.close()
                    return invoice
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def add_invoice(self, invoice):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO invoices (typeinvoices, invoices) VALUES (%s, %s)', (invoice['typeinvoices'], invoice['invoices']))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_invoices(self, invoices,id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('UPDATE invoices SET typeinvoices = %s, invoices = %s WHERE id = %s', (invoices['typeinvoices'], invoices['invoices'],id))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_invoice(self, id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('DELETE FROM invoices WHERE id = %s', (id,))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)