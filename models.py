from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Company(BaseModel):
# """model for one of your table"""
    __tablename__ = 'company'
    # define your model
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_no = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __init__(self,company_id,company_name,email,phone_no,address):
        self.company_id=company_id
        self.company_name=company_name
        self.email =email
        self.phone_no = phone_no
        self.address=address

    # def __repr__(self):
    #     return '<Company Name %r>' % self.company_name
