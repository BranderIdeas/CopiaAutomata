# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class om_automata_licitaciones(models.Model):
#     _name = 'om_automata_licitaciones.om_automata_licitaciones'
#     _description = 'om_automata_licitaciones.om_automata_licitaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
