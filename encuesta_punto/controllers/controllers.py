# -*- coding: utf-8 -*-
# from odoo import http


# class EncuestaPunto(http.Controller):
#     @http.route('/encuesta_punto/encuesta_punto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/encuesta_punto/encuesta_punto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('encuesta_punto.listing', {
#             'root': '/encuesta_punto/encuesta_punto',
#             'objects': http.request.env['encuesta_punto.encuesta_punto'].search([]),
#         })

#     @http.route('/encuesta_punto/encuesta_punto/objects/<model("encuesta_punto.encuesta_punto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('encuesta_punto.object', {
#             'object': obj
#         })
