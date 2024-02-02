from odoo import models, fields

class puntodeventa(models.Model):
    _name = 'restaurante.punto_de_venta'
    _description = 'Puntos de Venta '

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    ciudad_id = fields.Selection([
        ('barranquilla', 'Barranquilla'),
        ('cartagena', 'Cartagena')],
        string='Ciudad'
    )    
    empleados = fields.Integer(string='Número de Empleados')