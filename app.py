from flask import Flask, request, flash, jsonify
from json import dumps
from models import *

# from flask_sqlalchemy import SQLAlchemy
# import datetime

# db = SQLAlchemy()

# class BaseModel(db.Model):
#     """Base data model for all objects"""
#     __abstract__ = True

#     def __init__(self, *args):
#         super().__init__(*args)

#     def __repr__(self):
#         """Define a base way to print models"""
#         return '%s(%s)' % (self.__class__.__name__, {
#             column: value
#             for column, value in self._to_dict().items()
#         })

#     def json(self):
#         """
#                 Define a base way to jsonify models, dealing with datetime objects
#         """
#         return {
#             column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
#             for column, value in self._to_dict().items()
#         }


# class Company(BaseModel,db.Model):
# # """model for one of your table"""
#     __tablename__ = 'company'
#     # define your model
#     company_id = db.Column(db.Integer, primary_key=True)
#     company_name = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     phone_no = db.Column(db.Integer, unique=True, nullable=False)
#     address = db.Column(db.String(120), nullable=False)

#     def __init__(self,company_name,email,phone_no,address):
#         # self.company_id=company_id
#         self.company_name=company_name
#         self.email =email
#         self.phone_no = phone_no
#         self.address=address

#     def __repr__(self):
#         return '<Company Name %r>' % self.company_name


app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route('/hello/<name>')
# def hello_world(name):
#     return "hello flask ...%s" %s name


# for models flask
POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'py_crud_git',
    'host': 'localhost',
    'port': '5432',
}



# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'postgres',
#     'db': 'crud_user',
#     'host': 'localhost',
#     'port': '5432',
# }



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# for application context
# def create_app():
#     POSTGRES = {
#         'user': 'postgres',
#         'pw': 'postgres',
#         'db': 'py_crud_git',
#         'host': 'localhost',
#         'port': '5432',
#     }


#     app = Flask(__name__)
#     app.config['DEBUG'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # db.init_app(app)
    # return app

# with app.app_context():
    # db.init_app(app)

db.init_app(app)

@app.route('/')
def hello_world():
    return "hello flask ...ll ana marsh...garau"


# db.session.add(
#     Company('manual comp', 'a', 254585, 'c')
# )
# db.session.commit()




# working
# to add company
@app.route('/api/company', methods=['POST'])
def create_company():
    # company = {}
    # error = []
    if request.method == "POST":
        if not request.form["company_name"] and not request.form["email"] and not request.form["phone_no"] and request.form["address"]:
            flash("Please enter each field of table uniquely.....")
        
        else:
            try:
                company = Company(
                    request.form['company_name'],
                    request.form['email'],
                    request.form['phone_no'],
                    request.form['address']
                )
                print "company"
                print company
                # with app.app_context():                
                db.session.add(company)
                db.session.commit()
            except:

                pass
                # error.append("Unable to add on database")
    print type(company)
    result = company_schema.dump(company)
    # return jsonify({'company': result.data})
    return jsonify({'company': result}) #display data with error
    # return jsonify({'company': result.error})
    # return jsonify(result)


# to update company
@app.route('/api/company/<int:pk>', methods=['PUT'])
def update_company(pk):
    # company = {}
    # error = []
    try:
        company = Company.query.get(pk)
    except IntegrityError:
        return jsonify({"message": "Company could not be found."}), 400

    
    print "company"

    company_name = request.form['company_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    address = request.form['address']

    print company_name

    company.company_name = company_name
    company.email = email
    company.phone_no = phone_no
    company.address = address

    db.session.commit()
    
    result = company_schema.dump(company)
    # return jsonify({'company': result.data})
    return jsonify({'company': result}) #display data with error
   
   
# to get list of company
@app.route('/api/company', methods=['GET'])
def get_company():
    # company = {}
    # error = []
    companies = Company.query.all()
    result = companies_schema.dump(companies)
    # return jsonify({'company': result})
    return jsonify({'company': result.data}) #display data only

# to get company by id
@app.route('/api/company/<int:pk>', methods=['GET'])
def get_company_by_id(pk):
    # company = {}
    # error = []
    try:
        company = Company.query.get(pk)
    except IntegrityError:
        return jsonify({"message": "Company could not be found."}), 400
    result = company_schema.dump(company)
    # return jsonify({'company': result})
    return jsonify({'company': result.data}) #display data only


# to delete company
@app.route('/api/company/<int:pk>', methods=['DELETE'])
def delete_company(pk):
    # company = {}
    # error = []
    company = Company.query.get(pk)
    db.session.delete(company)
    db.session.commit()

    result = company_schema.dump(company)
    # return jsonify({'company': result})
    return jsonify({'company': result.data}) #display data only




# @app.route('/company')
# def company():
#     company = {}
#     error = []
#     try:
#         company = Company("hey mama","hey@gmail.com",5188392,"bkt")
#         print "company"
#         print company
#         db.session.add(company)
#         db.session.commit()
#     except:
#         error.append("Unable to add on database")
#     print type(company)
#     print "same data added unique constraint voilated...."
#     return company.company_name

if __name__ == '__main__':
    app.run() 




   
