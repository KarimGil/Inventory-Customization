from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    lang = fields.Selection(
        selection='_get_lang_list',
        string='Language',
        help='Default language for the company',
        default='en_US',
    )

    def _get_lang_list(self):
        return self.env['res.lang'].get_installed()
