# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autor(models.Model):
    _inherit = 'res.partner'
    
    book_ids = fields.One2many('libros.libro', 'book_id', string='Libros escritos')