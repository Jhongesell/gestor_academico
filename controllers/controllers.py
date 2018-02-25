# -*- coding: utf-8 -*-
from odoo import http

# class GestorAcademico(http.Controller):
#     @http.route('/gestor_academico/gestor_academico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestor_academico/gestor_academico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestor_academico.listing', {
#             'root': '/gestor_academico/gestor_academico',
#             'objects': http.request.env['gestor_academico.gestor_academico'].search([]),
#         })

#     @http.route('/gestor_academico/gestor_academico/objects/<model("gestor_academico.gestor_academico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestor_academico.object', {
#             'object': obj
#         })