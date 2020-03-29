# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autor(models.Model):
    _inherit = 'res.partner'
    
    book_ids = fields.One2many('libros.libro', 'id', string='Libros escritos')
    published_books = fields.Integer('Número de libros publicados', compute='_num_libros', store=False)

    @api.depends('book_ids')
    def _num_libros(self):
        for record in self:
            return len(self.book_ids)
