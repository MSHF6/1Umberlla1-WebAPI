# -*- coding: utf-8 -*-
from db.repository import GenericRepository
from db.user import User
from database import db

class UserRepository(GenericRepository):
	"""
	docstring for UserRepository
	"""

	def __init__(self, cls, db_session):
		super(UserRepository, self).__init__(cls, db_session)

	def get_by_phone_and_password(self, cellphone, password):
		result = self.db_session.query(self.model_class) \
			.filter_by(
				cellphone=cellphone,
				password=password) \
			.first()
		return result
# 初始化
user_repository = UserRepository(User, db.session)
