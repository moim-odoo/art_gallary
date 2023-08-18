from odoo import fields,models

class artwork(models.Model):
    _name="artgallary.artwork"
    _description="Art Work model of art gallary"

    name=fields.Char(string='Title')
    description=fields.Char(string="Description")
    artist_id=fields.Many2one("artgallary.artist" , string="Artist Name")
    image=fields.Image(string="Image" ,required=True)
    price=fields.Float(string='price' )
    state=fields.Selection(string="State",selection=[('available','Available'),('sold','Sold')], default='available')

    _sql_constraints =[
        ('name','CHECK(name is NOT NULL)','please add a art with name')
    ]