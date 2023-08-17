from odoo import fields,models

class interaction(models.Model):
    _name="artgallary.interaction"
    _description="Art Gallary Iteraction Model"

    user_id=fields.Many2one("artgallary.user" , string="Interacted Person")
    artwork_id=fields.Many2one("artgallary.artwork" , string="Interacted Art")
    comment=fields.Char(string="Comment")
    rating=fields.Selection(selection=[('worst','Worst'),('average','Avarege'),('good','Good'),('best','Best'),('excellent','Excellent')] , string="Ratting")