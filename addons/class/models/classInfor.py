# -*- coding: utf-8 -*-
from contextlib import nullcontext
from odoo import api, fields, models


class ClassInformation(models.Model):
    _name = "class.information"  # nameofTable
    _description = "Class Management"

    # Moi quan he giua Truong va lop va quan he 1-n (1 truong - nhiều lớp)
    name = fields.Char(string=("Tên lớp"), required=True)
    grade = fields.Char(string=("Tên khối"), required=True)
    mainTeacher = fields.Char(string=("GVCN"), required=True)
    school_id = fields.Many2one("school.information", string="Trường" , required=True)


# class SchoolInformation(models.Model):
#     _inherit = 'school.information'
#     class_list = fields.One2many('class.information', 'school_id', string="Danh sách lớp")
