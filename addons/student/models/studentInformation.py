# -*- coding: utf-8 -*-
from contextlib import nullcontext
from odoo import api, fields, models


class StudentInformation(models.Model):
    _name = "student.information"  # nameofTable
    _description = "Student Management"

    name = fields.Char(string=("Họ và Tên"), required=True)
    birthday = fields.Date(string=("Ngày sinh"), required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)


class ClassInformation(models.Model):
    _inherit = 'class.information'
    student_list = fields.One2many('student.information', 'class_id', string="Danh sách học sinh")
