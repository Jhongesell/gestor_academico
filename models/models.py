# -*- coding: utf-8 -*-
from odoo import models, fields, api

class estudiante(models.Model):

    _name = "ga.estudiante"

    name = fields.Char(string="Nombre")
    edad = fields.Integer(string="Edad")
    fec_nac = fields.Date(string="Fecha de Nacimiento")
    estatura = fields.Float(string="Estatura")
    descripcion = fields.Text(string="Descripción")
    sexo = fields.Selection(selection=[('F',"Femenino"),("M","Masculino")],string="Sexo")


