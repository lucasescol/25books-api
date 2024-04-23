from flask import Flask
from server.routes.user_routes import user_routes
from server.routes.book_routes import book_routes
from server.routes.borrow_routes import borrow_routes


app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.register_blueprint(user_routes)
app.register_blueprint(book_routes)
app.register_blueprint(borrow_routes)
