# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libro(models.Model):
    _name='libros.libro'
    
    name = fields.Char('Título', required=True, index=True)
    published_date = fields.Date('Fecha de publicación')
    author_id = fields.Many2one('libros.autor', string='Autor', required=True)