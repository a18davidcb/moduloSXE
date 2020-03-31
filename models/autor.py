# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autor(models.Model):
    _name='libros.autor'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    book_ids = fields.One2many('libros.libro', inverse_name='author_id', string='Libros escritos')
    published_books = fields.Integer('Número de libros publicados', compute='_num_libros', store=False)

    @api.depends('book_ids')
    def _num_libros(self):
        return len(self.book_ids)
