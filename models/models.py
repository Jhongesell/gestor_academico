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
    curso_ids = fields.Many2many("ga.curso")

class curso(models.Model):
    _name="ga.curso"
    name = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
    #Many2many(<nombre_clase>)
    estudiante_ids = fields.Many2many("ga.estudiante")

