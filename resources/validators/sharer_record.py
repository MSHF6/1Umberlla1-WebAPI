# -*- coding: utf-8 -*-
from flask_restful import reqparse
from decimal import Decimal
"""
Validator : SharerRecord
"""

class PostValidator(object):
	def __init__(self):
		self.parser = reqparse.RequestParser(bundle_errors=True)
		self.parser.add_argument('location_lat', type=Decimal, required=True)
		self.parser.add_argument('location_lng', type=Decimal, required=True)


class UpdateValidator(object):
	def __init__(self):
		self.parser = reqparse.RequestParser(bundle_errors=True)
		self.parser.add_argument('switch', type=bool)
		self.parser.add_argument('location_lat', type=Decimal)
		self.parser.add_argument('location_lng', type=Decimal)