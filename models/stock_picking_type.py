from odoo import fields, models, api, _

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    code = fields.Selection([('incoming', 'Receipt'), ('outgoing', 'Delivery'), ('internal', 'Internal Transfer'), ('return', 'Return')], string='Type of Operation', required=True, translate=True)

    def do_functionality(self, main_company_id):
        self.set_context_to_action(main_company_id)
        self.create_return_operation(main_company_id)

    def set_context_to_action(self, main_company_id):
        action = self.env.ref('stock.stock_picking_type_action')
        company = self.env['res.company'].search([('id', '=', main_company_id)], limit=1)
        lang = company.lang
        new_context = {'lang': lang}
        action.context = new_context

    def create_return_operation(self, main_company_id):
        stock_picking = self.search(
            [('name', '=', 'Return'), ('code', '=', 'return'), ('company_id', '=', int(main_company_id))], limit=1)
        if not stock_picking:
            stock_picking.create({
                'name': 'Return',
                'code': 'return',
                'company_id': main_company_id,
                'warehouse_id': False,
                'sequence_code': ' ',
            })