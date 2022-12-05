from flask import Flask

from config import config
from routes import apiPersons
from routes import apiProducts
from routes import apiInvoice

app = Flask(__name__)
def page_not_found(e):
    return "<h1>not found page</h1>", 404
if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Blueprints
    app.register_blueprint(apiPersons.main, url_prefix='/api/persons')
    
    app.register_blueprint(apiProducts.main, url_prefix='/api/products')
    app.register_blueprint(apiInvoice.main, url_prefix='/api/invoice')

    app.register_error_handler(404,page_not_found)
    app.run()

