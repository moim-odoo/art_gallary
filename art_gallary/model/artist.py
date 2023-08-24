from odoo import fields,models,api

class artist(models.Model):
    _name='artgallary.artist'
    _description='Art Gallary Artist Model'
    _order='name desc'

    name=fields.Char(string='Name',required=True)
    date_of_birth=fields.Date(string="DOB")
    artwork_ids=fields.One2many('artgallary.artwork','artist_id',string="Arts")
    total_welth=fields.Float(string="Total Welth" ,compute="_compute_total_earn" ,store=True)
    specility=fields.Char(string="specility")


    @api.depends("artwork_ids")
    def _compute_total_earn(self):
        for record in self:
            if record.artwork_ids:
                total_art=record.mapped("artwork_ids.price")
                for val in total_art:
                    record.artwork_ids.artist_id.total_welth = record.artwork_ids.artist_id.total_welth + val
            # print(record.total_welth)        