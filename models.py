from flask_sqlalchemy import SQLAlchemy
import datetime

from marshmallow import Schema, fields, pprint

db = SQLAlchemy()


class Company(db.Model):
# """model for one of your table"""
    __tablename__ = 'company'
    # define your model
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(80))
    email = db.Column(db.String(100))
    phone_no = db.Column(db.String)
    address = db.Column(db.String(120))

    def __init__(self,company_name,email,phone_no,address):
        # self.company_id=company_id
        self.company_name=company_name
        self.email =email
        self.phone_no = phone_no
        self.address=address

    def __repr__(self):
        return '<Company Name %r>' % self.company_name


class CompanySchema(Schema):
    company_id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    phone_no = fields.Str()
    address = fields.Str()
    formatted_name = fields.Method("format_name", dump_only=True)

    def format_name(self, company):
        return "{}, {}, {}, {}, {}".format(company.company_id, company.company_name,company.email,company.phone_no,company.address)

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)
