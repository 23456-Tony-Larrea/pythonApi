from database.db import get_connection
from .entities.Products import Products

class ProductsModel:
    @classmethod
    def getProducts(self):
        try:
            conn = get_connection()
            products=[]
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM products')
                rows = cur.fetchall()
        
            for row in rows:
                products.append(Products(row[0], row[1], row[2]).to_JSON())
            return products
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def getProductsId(self, id):
        try:
            conn = get_connection()
            
        
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM products where id = %s', (id,))
                rows = cur.fetchone()

                products=None
                if rows is not None:
                    products=Products(rows[0],rows[1],rows[2])
                    products=products.to_JSON()
                    conn.close()
                    return products
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def add_products(self, products):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('INSERT INTO products (typeproducts, products) VALUES (%s, %s)', (products['typeproducts'], products['products']))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_product(self, products,id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('UPDATE products SET typeproducts = %s, products = %s WHERE id = %s', (products['typeproducts'], products['products'],id))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_product(self, id):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute('DELETE FROM products WHERE id = %s', (id,))
                affected_rows = cur.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)