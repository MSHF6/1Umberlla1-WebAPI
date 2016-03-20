# -*- coding:utf-8 -*-
import httplib
from sqlalchemy import exc
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with
from resources import blueprints, endpoints
from resources.extension import aborts
from resources.extension.fields import Unicode
from db.repository.user import user_repository
from resources.validators import user

blueprint = Blueprint(
	blueprints.USER_BP, __name__)

api = Api(blueprint, prefix='/v1.0')

share_records_fields = {
	'id': fields.Integer,
	'uri': fields.Url(
		blueprints.SHARER_RECORD_BP +
		'.' +
		endpoints.SHARER_RECORD_ITEM
	)
}

used_resource_records_fields = {
	'id': fields.Integer,
	'uri': fields.Url(
		blueprints.USED_SHARE_RECORD_BP +
		'.' +
		endpoints.USED_SHARE_RECORD_ITEM
	)
}

get_fields = {
	'id': fields.Integer,
	'name': Unicode(),
	'cellphone': fields.String,
	'address': Unicode(),
	'share_records': fields.List(fields.Nested(share_records_fields)),
	'used_resource_records': fields.List(fields.Nested(used_resource_records_fields))
}

post_location_fields = {
	'id': fields.String,
	'uri': fields.Url('.' + endpoints.USER_ITEM)
}

class UserItem(Resource):
	@marshal_with(get_fields, envelope='resource')
	def get(self, id):
		print 'get:', id
		db_user = user_repository.get(id)
		if db_user:
			return db_user, httplib.OK
		else:
			aborts.not_exist(id, "get user id")

	@marshal_with(get_fields, envelope='resource')
	def delete(self, id):
		db_user = user_repository.delete(id)
		print 'delete:', id
		if db_user:
			return db_user, httplib.OK
		else:
			aborts.not_exist(id, "delete user id")

	@marshal_with(get_fields, envelope='resource')
	def patch(self, id):
		print 'patch:', id
		patch_user = user.UpdateValidator()
		user_args = patch_user.parser.parse_args()
		print 'args:', user_args
		try:
			# 移除 None 值
			for key, value in user_args.items():
				if value is None:
					del user_args[key]
			print 'clear None args:', user_args
			# 更新值
			db_user = user_repository.update(id, user_args)
			if db_user:
				return db_user, httplib.OK
			else:
				aborts.not_exist(id, "get user id")
		except Exception as e:
			aborts.not_empty(e.orig.args, "patch user")

class UserList(Resource):
	@marshal_with(get_fields, envelope='resource')
	def get(self):
		return user_repository.list()

	@marshal_with(post_location_fields, envelope='locatioin')
	def post(self):
		post_user = user.PostValidator()
		user_args = post_user.parser.parse_args()
		print 'post:', user_args
		try:
			result = user_repository.create(user_args)
			if result:
				return {'id': result.id}, httplib.CREATED
		except exc.SQLAlchemyError as e:
			aborts.post_conflict(e.orig.args, 'post user item')



# endpoints : Can be used to reference this route in fields.Url fields
api.add_resource(
	UserItem,
	'/users/<int:id>',
	endpoint=endpoints.USER_ITEM
)
api.add_resource(
	UserList,
	'/users',
	endpoint=endpoints.USER_LIST
)