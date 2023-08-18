from odoo import fields,models

class user(models.Model):
    _name="artgallary.user"
    _description="Art Gallary User Model"

    name=fields.Char(string="Name" , required=True)
    email=fields.Char(string="Email")
    password=fields.Char(string='password')
    address=fields.Char(string="Address")
    birth_date=fields.Date(string="Date Of Births")



