# -*- coding: utf-8 -*-
from database import db
from db.common import SystemInfo


class User(SystemInfo):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	cellphone = db.Column(db.String(20))
	address = db.Column(db.Unicode(255), nullable=True)
	password = db.Column(db.String(45))

	# 虛擬關聯外鍵，對應到共享此傘的紀錄
	share_records = db.relationship(
		'UsingShareRecord',
		backref='users'
	)
	# 虛擬關聯外鍵，紀錄多筆使用此雨傘資源的紀錄
	using_resource_records = db.relationship(
		'UsingShareRecord',
		backref='users'
	)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', name='%s',  password='%s', cellphone='%s', address='%s'>" % (
			self.id, self.name, self.password, self.cellphone, self.address
		)