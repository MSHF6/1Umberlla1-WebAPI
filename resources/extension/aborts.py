# -*- coding:utf-8 -*-
import httplib
from flask_restful import abort

def not_exist(value, field_name):
	"""
	Custom abort not found
	Args:
		value(str):not found message
		field_name(str): which field or data not found
	"""
	abort(
		httplib.NOT_FOUND,
		message="{} {} is not existed".format(field_name, value)
	)

def not_correct(value, field_name):
	"""
	Custom abort not found
	Args:
		value(str):not found message
		field_name(str): which field or data not found
	"""
	abort(
		httplib.NOT_FOUND,
		message="{} {} is not correct".format(field_name, value)
	)


def not_empty(value, field_name):
	"""
	Custom abort not found
	Args:
		value(str):not found message
		field_name(str): which field or data not found
	"""
	abort(
		httplib.INTERNAL_SERVER_ERROR,
		message="{} {} can't empty".format(field_name, value)
	)



def conflict(value, resource_name):
	"""
	Custom abort conflict when post or update
	Args:
		value(str):conflict message
		resource_name(str): which resource conflict when you post
	"""
	abort(
		httplib.CONFLICT,
		message="resource {} is existed, error message: {}".format(
			resource_name, value)
	)
