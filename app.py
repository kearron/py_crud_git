from flask import Flask
from models import db




app = Flask(__name__)

app.config['DEBUG'] = True




# @app.route('/hello/<name>')
# def hello_world(name):
#     return "hello flask ...%s" %s name

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'py_crud_git',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

@app.route('/')
def hello_world():
    return "hello flask ...ll"



if __name__ == '__main__':
   app.run() 


#hello world

   
