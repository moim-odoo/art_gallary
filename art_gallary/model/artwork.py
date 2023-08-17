from odoo import fields,models

class artwork(models.Model):
    _name="artgallary.artwork"
    _description="Art Work model of art gallary"

    name=fields.Char(string='Title')
    description=fields.Char(string="Description")
    artist_id=fields.Many2one("artgallary.artist" , string="Artist Name")
    image=fields.Binary(string="Image of art")