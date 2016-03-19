# -*- coding:utf-8 -*-
import json
from flask_restful import fields

class LinkField(fields.Raw):
	'''
	Link 欄位
	'''
	def format(self, value):
		'''
		格式化 Link欄位資料為 json
		'''
		link_field = {
			'rel': fields.String,
			'method': fields.String,
			'href': fields.Url(value, absolute=True),
		}
		return json.dump(link_field)


class Unicode(fields.Raw):
	def format(self, value):
		try:
			return unicode(value)
		except ValueError as ve:
			raise ve