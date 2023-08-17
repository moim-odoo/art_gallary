from odoo import fields,models

class artist(models.Model):
    _name='artgallary.artist'
    _description='Art Gallary Artist Model'
    _order='name desc'

    name=fields.Char(string='Name',required=True)
    date_of_birth=fields.Date(string="DOB")
    artwork_ids=fields.One2many('artgallary.artwork','artist_id',string="Arts")
    specility=fields.Char(string="specility")