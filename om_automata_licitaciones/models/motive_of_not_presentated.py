# -*- coding: utf-8 -*-

from odoo import models, fields, api


class motive_of_not_presentated(models.Model):
    _name = 'om_automata_licitaciones.motive_of_not_presentated'
    _description = 'Motivos de NO PRESENTADA'

    name = fields.Char('Name')
    description = fields.Text('Description')