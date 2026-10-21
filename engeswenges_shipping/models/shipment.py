from odoo import models, fields


class ShippingShipment(models.Model):
    _name = 'engeswenges.shipment'
    _description = 'EngeSwEngeS Shipment'
    _order = 'create_date desc'

    name = fields.Char(
        string='Tracking Number',
        required=True,
        copy=False,
        default='New'
    )

    sender_name = fields.Char(
        string='Merchant Name',
        required=True
    )

    recipient_name = fields.Char(
        string='Recipient Name',
        required=True
    )

    recipient_phone = fields.Char(
        string='Recipient Phone',
        required=True
    )

    delivery_address = fields.Text(
        string='Delivery Address',
        required=True
    )

    shipping_fee = fields.Float(
        string='Shipping Fee',
        default=0.0
    )

    cod_amount = fields.Float(
        string='Cash on Delivery',
        default=0.0
    )

    status = fields.Selection([
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
    ], string='Shipment Status', default='pending', required=True)
