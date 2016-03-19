# -*- coding: utf-8 -*-
from flask_restful import reqparse
from decimal import Decimal
"""
Validator : User
"""

class PostValidator(object):
	def __init__(self):
		self.parser = reqparse.RequestParser(bundle_errors=True)
		self.parser.add_argument(
			'name', type=unicode, required=True)
		self.parser.add_argument(
			'cellphone', type=str, required=True)
		self.parser.add_argument(
			'password', type=str, required=True)
		self.parser.add_argument('address', type=unicode)


class UpdateValidator(object):
	def __init__(self):
		self.parser = reqparse.RequestParser(bundle_errors=True)
		self.parser.add_argument(
			'name', type=unicode)
		self.parser.add_argument('cellphone', type=str)
		self.parser.add_argument('password', type=str)
		self.parser.add_argument('address', type=unicode)
