# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class autor(models.Model):
    _name='libros.autor'
    _inherits = {'res.partner': 'partner_id'}
    _sql_constraints = [('partner_uniq', 'UNIQUE(partner_id)', 'El autor debe ser único')]
    
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    book_ids = fields.One2many('libros.libro', inverse_name='author_id', string='Libros escritos')
    published_books = fields.Integer('Número de libros publicados', compute='_num_libros', store=False)

    @api.depends('book_ids')
    def _num_libros(self):
        for record in self:
          record.published_books = len(record.book_ids)
