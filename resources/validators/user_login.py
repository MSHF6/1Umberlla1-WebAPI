# -*- coding: utf-8 -*-
from flask_restful import reqparse
"""
Validator : UserLogin
"""

class PostValidator(object):
	def __init__(self):
		self.parser = reqparse.RequestParser(bundle_errors=True)
		self.parser.add_argument(
			'cellphone', type=str, required=True)
		self.parser.add_argument(
			'password', type=str, required=True)
