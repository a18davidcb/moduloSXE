# -*- coding: utf-8 -*-
from odoo import http

# class Libros(http.Controller):
#     @http.route('/libros/libros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libros/libros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('libros.listing', {
#             'root': '/libros/libros',
#             'objects': http.request.env['libros.libros'].search([]),
#         })

#     @http.route('/libros/libros/objects/<model("libros.libros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libros.object', {
#             'object': obj
#         })