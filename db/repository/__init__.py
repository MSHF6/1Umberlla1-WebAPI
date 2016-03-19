# -*- coding: utf-8 -*-
from sqlalchemy import exc

class GenericRepository(object):
	def __init__(self, model_class, db_session):
		self.model_class = model_class
		self.db_session = db_session

	def create(self, create_args):
		try:
			model = self.model_class(**create_args)
			self.db_session.add(model)
			# 取得 id
			self.db_session.flush()
			self.db_session.commit()
			return model
		except exc.SQLAlchemyError as e:
			raise e

	def get(self, id):
		try:
			model = self.db_session.query(self.model_class).get(id)
			return model
		except Exception as ex:
			return None


	def list(self):
		results = self.db_session.query(self.model_class).all()
		return results

	def update(self, id, update_args):
		result = self.db_session.query(self.model_class).get(id)
		if result:
			try:
				for key, value in update_args.items():
					# 透過 setattr，把參數 key 與 value 設定到 model 中的屬性值
					setattr(result, key, value)
				self.db_session.commit()
				return result
			except exc.SQLAlchemyError, e:
				# 有重複的 Key
				raise e
		else:
			return None

	def delete(self, id):
		result = self.db_session.query(self.model_class).get(id)
		if result:
			self.db_session.delete(result)
			self.db_session.commit()
			return result
		else:
			return None
