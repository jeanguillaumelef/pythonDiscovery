# app.py
from flask import Flask
from database import db
from routes import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # replace with real db URI

db.init_app(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)