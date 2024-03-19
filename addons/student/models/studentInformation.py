# -*- coding: utf-8 -*-
from contextlib import nullcontext
from odoo import api, fields, models


class StudentInformation(models.Model):
    _name = "student.information"  # nameofTable
    _description = "Student Management"

    name = fields.Char(string=("Họ và Tên"), required=True)
    birthday = fields.Date(string=("Ngày sinh"), required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)

    subject_list = fields.Many2many("subject.information", 'relation_subject_student','student_id', 'subject_id', string="Bảng quan hệ giữa môn học và học sinh")


class ClassInformation(models.Model):
    _inherit = 'class.information'
    student_list = fields.One2many('student.information', 'class_id', string="Danh sách học sinh")


class SubjectInformation(models.Model):
    _name = "subject.information"  # nameofTable
    _description = "Subject Management"

    name = fields.Char(string=("Tên môn học"))
    author = fields.Char(string=("Tác giả"))
