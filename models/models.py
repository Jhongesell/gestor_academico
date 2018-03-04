# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class departamento(models.Model):
    _name="departamento"
    name=fields.Char("Nombre")

class estudiante(models.Model):
    _name = "ga.estudiante"
    name = fields.Char(string="Nombre",required=True)
    edad = fields.Integer(string="Edad",required=True)
    fec_nac = fields.Date(string="Fecha de Nacimiento",required=True)
    estatura = fields.Float(string="Estatura")
    descripcion = fields.Text(string="Descripción")
    sexo = fields.Selection(selection=[('F',"Femenino"),("M","Masculino")],string="Sexo")
    curso_ids = fields.Many2many("ga.curso",string="Cursos")
    evaluacion_ids = fields.One2many("ga.evaluacion","estudiante_id",string="Evaluaciones")

    def _get_selection(self):
        objects_departamento=self.env["departamento"].search([])
        lista_departamento = []
        for dep in objects_departamento:
            lista_departamento.append((dep.name ,dep.name ))
        return lista_departamento

    departamento = fields.Selection(selection=_get_selection)

    @api.one
    @api.depends("evaluacion_ids.nota")
    def _compute_pp(self):
        suma=0
        length=len(self.evaluacion_ids)
        for evaluacion in self.evaluacion_ids:
            suma=suma+evaluacion.nota
        if length!=0:
            promedio= suma/float(length)
        else:
            promedio=0

    pp = fields.Float(string= "Promedio Ponderado",compute="_compute_pp")

class curso(models.Model):
    _name="ga.curso"
    name = fields.Char("Nombre")
    descripcion = fields.Text("Descripción")
    #Many2many(<nombre_clase>)
    estudiante_ids = fields.Many2many("ga.estudiante",string="Estudiantes")
    evaluacion_ids = fields.One2many("ga.evaluacion","curso_id",string="Evaluaciones",help="Aquí seañaden las evaluaciones")
    profesor_id = fields.Many2one("ga.profesor",string="Profesor")


class evaluacion(models.Model):
    _name = "ga.evaluacion"
    name = fields.Char("Nombre")
    curso_id = fields.Many2one("ga.curso",string="Curso")
    estudiante_id = fields.Many2one("ga.estudiante",string="Estudiante")
    res_partner_id=fields.Many2one("res.partner",string="Estudiante - Partner")
    nota = fields.Integer("Nota")

    @api.constrains("nota")
    def validar_nota(self):
        if self.nota<0 or self.nota>20:
            raise ValidationError("La nota debe estar comprendida entre 0 y 20")


class profesor(models.Model):
    _name = "ga.profesor"
    name = fields.Char("Nombre")
    curso_ids = fields.One2many("ga.curso","profesor_id")



class respartner(models.Model):
    _inherit = "res.partner"
    dni=fields.Char("DNI")
    profesor = fields.Boolean("Es profesor")
    estudiante = fields.Boolean("Es Estudiante")
    edad = fields.Integer(string="Edad",required=True)
    fec_nac = fields.Date(string="Fecha de Nacimiento",required=True)
    estatura = fields.Float(string="Estatura")
    descripcion = fields.Text(string="Descripción")
    sexo = fields.Selection(selection=[('F',"Femenino"),("M","Masculino")],string="Sexo")
    curso_ids = fields.Many2many("ga.curso",string="Cursos")
    evaluacion_ids = fields.One2many("ga.evaluacion","res_partner_id",string="Evaluaciones")

    def _get_selection(self):
        objects_departamento=self.env["departamento"].search([])
        lista_departamento = []
        for dep in objects_departamento:
            lista_departamento.append((dep.name ,dep.name ))
        return lista_departamento

    departamento = fields.Selection(selection=_get_selection)

    @api.one
    @api.depends("evaluacion_ids.nota")
    def _compute_pp(self):
        suma=0
        length=len(self.evaluacion_ids)
        for evaluacion in self.evaluacion_ids:
            suma=suma+evaluacion.nota
        if length!=0:
            promedio= suma/float(length)
        else:
            promedio=0
        self.pp=promedio

    pp = fields.Float(string= "Promedio Ponderado",compute="_compute_pp")







