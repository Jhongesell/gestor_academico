# -*- coding: utf-8 -*-
from odoo import models, fields, api

class estudiante(models.Model):
    _name = "ga.estudiante"
    name = fields.Char(string="Nombre",required=True)
    edad = fields.Integer(string="Edad",required=True)
    fec_nac = fields.Date(string="Fecha de Nacimiento",required=True)
    estatura = fields.Float(string="Estatura")
    descripcion = fields.Text(string="Descripción")
    sexo = fields.Selection(selection=[('F',"Femenino"),("M","Masculino")],string="Sexo")
    curso_ids = fields.Many2many("ga.curso")
    evaluacion_ids = fields.One2many("ga.evaluacion","estudiante_id",string="Evaluaciones")

class curso(models.Model):
    _name="ga.curso"
    name = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
    #Many2many(<nombre_clase>)
    estudiante_ids = fields.Many2many("ga.estudiante")
    evaluacion_ids = fields.One2many("ga.evaluacion","curso_id")
    profesor_id = fields.Many2one("ga.profesor")

class evaluacion(models.Model):
    _name = "ga.evaluacion"
    name = fields.Char("Nombre")
    curso_id = fields.Many2one("ga.curso")
    estudiante_id = fields.Many2one("ga.estudiante")

class profesor(models.Model):
    _name = "ga.profesor"
    name = fields.Char("Nombre")
    curso_ids = fields.One2many("ga.curso","profesor_id")
