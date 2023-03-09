from odoo import http
from odoo.http import request



class MyController(http.Controller):
    @http.route('/translate_lang', type='http', auth='none', csrf=False)
    def update_lang(self, **kwargs):
        main_company_id = kwargs.get('main_company_id')
        stock_picking = request.env['stock.picking.type'].sudo().search([])
        stock_picking.do_functionality(main_company_id)
        return 'Success'
