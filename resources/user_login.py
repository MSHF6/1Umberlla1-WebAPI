# -*- coding:utf-8 -*-
import httplib
from sqlalchemy import exc
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with
from resources import blueprints, endpoints
from resources.extension import aborts
from db.repository.user import user_repository
from resources.validators import user_login


blueprint = Blueprint(
	blueprints.USER_PSD_BP, __name__)

api = Api(blueprint, prefix='/v1.0')


post_get_user_location_fields = {
	'id': fields.String,
	'uri': fields.Url(
		blueprints.USER_BP +
		'.' +
		endpoints.USER_ITEM)
}


class UsersLogin(Resource):
	@marshal_with(post_get_user_location_fields, envelope='resource')
	def post(self):
		# 驗贈參數
		post_user_psd = user_login.PostValidator()
		post_user_args = post_user_psd.parser.parse_args()
		# 檢查
		print 'post:', post_user_args
		result = None
		if post_user_args['cellphone'] and post_user_args['password']:
			result = user_repository \
				.get_by_phone_and_password(
					post_user_args['cellphone'],
					post_user_args['password'])
			if result:
				return {'id': result.id}, httplib.CREATED
		return aborts.not_correct("cellphone or password", "check user")


api.add_resource(
	UsersLogin,
	'/users/login',
	endpoint=endpoints.USER_PSD_ITEM
)