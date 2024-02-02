from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
from odoo.http import request, route, Controller

class EncuestaControllers(Controller):
    @route('/api/encuesta', auth='user', website=True, csrf=False)
    def update_data(self, **kwargs):
        puntos_venta = request.env['restaurante.punto_de_venta'].sudo().search([])
        return request.render('encuesta_punto.encuesta_form', {'partner': request.env.user.partner_id,'available_puntos_venta': puntos_venta})

    #Creacion de encuesta
    @route('/api/encuesta_save', auth='user', website=True, csrf=False)
    def update_data_save(self, **kwargs):
        # Validar que los campos estén en el rango de 1 a 5
        for field_name in ['comodidad', 'comida', 'atencion', 'musica', 'tiempo_espera', 'mesero']:
            value = int(kwargs.get(field_name, 0))
            if value < 1 or value > 5:
                raise ValidationError(f"El campo {field_name} debe estar en el rango de 1 a 5.")
       
        
        dict_values = {
            'name':kwargs['name'],
            'punto_venta_id' : int(kwargs['punto_venta_id']),
            'comodidad':kwargs['comodidad'],
            'comida':kwargs['comida'],
            'atencion':kwargs['atencion'],
            'musica':kwargs['musica'],
            'tiempo_espera':kwargs['tiempo_espera'],
            'mesero':kwargs['mesero'],
            'notas_cliente':kwargs['notas_cliente'],
            
        }
        obj_encuesta = request.env['restaurante.encuesta'].sudo().search([])
        obj_encuesta.create(dict_values)
        #Enviar a pagina principal
        puntos_venta = request.env['restaurante.punto_de_venta'].sudo().search([])
        return request.render('encuesta_punto.encuesta_form', {'obj_encuesta': obj_encuesta, 'available_puntos_venta': puntos_venta})