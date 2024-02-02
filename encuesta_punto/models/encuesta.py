from odoo import models, fields

class encuesta(models.Model):
    _name = 'restaurante.encuesta'
    _description = 'Encuestas'

    name = fields.Char(string='Nombre', required=True)
    punto_venta_id = fields.Many2one('restaurante.punto_de_venta', string='Punto de Venta')
    comodidad = fields.Integer(string='Comodidad')
    comida = fields.Integer(string='Comida')
    atencion = fields.Integer(string='Atención')
    musica = fields.Integer(string='Música')
    tiempo_espera = fields.Integer(string='Tiempo de Espera')
    mesero = fields.Integer(string='Del Mesero')
    notas_cliente = fields.Text(string='Notas del Cliente')