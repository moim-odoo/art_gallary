from odoo import fields,models

class interaction(models.Model):
    _name="artgallary.interaction"
    _description="Art Gallary Iteraction Model"

    user_id=fields.Many2one("artgallary.user" , string="Interacted Person",required=True)
    artwork_id=fields.Many2one("artgallary.artwork" , string="Interacted Art",required=True)
    comment=fields.Char(string="Comment")
    rating=fields.Selection(selection=[('worst','Worst'),('average','Avarege'),('good','Good'),('best','Best'),('excellent','Excellent')] , string="Ratting")