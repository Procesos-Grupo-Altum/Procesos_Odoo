# -*- conding:utf-8 -*-
from email.policy import default

from odoo import fields, models, api
from odoo.odoo.api import depends


class PazySalvo(models.Model):
    _name = 'pazysalvo'
    _inherit = ['image.mixin']  # Permite agregar imagenes a los registros
    _rec_name = 'employee_id'

    name = fields.Char(string='Nombre Empleado', invisible="1")



    employee_id = fields.Many2one('hr.employee', string='Nombre Empleado', index=True)

    image_1920 = fields.Binary(
        related='employee_id.image_1920',  # <-- aquí el cambio
        readonly=True,
        store=False,
        string='Foto'
    )



    state = fields.Selection(
        selection=[
            ('draft', 'Borrador'),
            ('done', 'Hecho'),
            ('cancel', 'Cancelado'),
        ],
        string='Estado',
        default='draft',
        copy=False,

    )



    x_1_entrego_carnet_presentacion = fields.Boolean(
        string='1. Entrego Carnet de Presentacion',
        help='Entrego el carnet de presentacion del empleado para el Paz y Salvo',
        required=False,
        default= False,
    )

    x_2_entrego_carnet_arl = fields.Boolean(
        string='2. Entrego Carnet de ARL',
        help='Entrego el carnet de la Administradora de Riesgos Laborales (ARL) para el Paz y Salvo',
        required=False,
        default= False,
    )
    x_3_entrego_carnet_eps = fields.Boolean(
        string='3. Entrego Carnet de EPS',
        help='Entrego el carnet de la Entidad Promotora de Salud (EPS) para el Paz y Salvo',
        required=False,
        default= False,
    )

    x_4_entrego_tarjeta_proximidad = fields.Boolean(
        string='4. Entrego Tarjeta de Proximidad',
        help='Entrego la tarjeta de proximidad para el Paz y Salvo',
        required=False,
        default= False,
    )

    x_1_por_que = fields.Char(
        string='1. Por que?',
        help='Por que no entrego el carnet de presentacion?',
        required=False)

    x_2_por_que = fields.Char(
        string='2. Por que?',
        help='Por que no entrego el carnet de Arl?',
        required=False)

    x_3_por_que = fields.Char(
        string='3. Por que?',
        help='Por que no entrego el carnet de EPS?',
        required=False)

    x_4_por_que = fields.Char(
        string='4. Por que?',
        help='Por que no entrego la tarjeta de proximidad?',
        required=False)

    x_contract_id = fields.Many2one(
        'hr.contract', string='Contrato',
        domain="[('employee_id', '=', x_employee_id)]"
    )

    x_employee_id = fields.Many2one(
        'hr.employee', string='Empleado', readonly=True,
        default=lambda self: self.env.user.employee_id,
        compute='_compute_employee_id', store=True)

    def aceptar(self):
        print('Bienvenido')

    def borrar(self):
        print('Me vas a borrar')