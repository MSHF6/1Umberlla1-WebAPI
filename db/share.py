# -*- coding: utf-8 -*-
from database import db
from db.common import SystemInfo

class SharerRecord(SystemInfo):
	"""
	共享雨傘的紀錄
	"""
	__tablename__ = 'sharer_record'
	# 同時作為 Shape 的路徑編號
	id = db.Column(db.Integer, primary_key=True)
	# 共享雨傘人
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	# 時間部分由 SystemInfo 處理

	# 使用者所在經緯度
	location_lat = db.Column(db.Numeric(9, 6), nullable=True)
	location_lng = db.Column(db.Numeric(9, 6), nullable=True)
	# 預設建立是開啟中 False
	switch = db.Column(db.Boolean, default=True)

	# 虛擬關聯外鍵，多筆使用此雨傘資源的紀錄與人
	using_resource_records = db.relationship(
		'UsedShareRecord',
		backref='using_share_record'
	)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<SharerRecord: id='%d', \
				switch='%s',location_lat='%s', location_lng='%s', \
				sharer_user_id='%d'>" % (
			self.id, self.switch, self.location_lat,
			self.location_lng, self.sharer_user_id,
		)


class UsedShareRecord(SystemInfo):
	"""
	使用共享雨傘資源的人
	"""
	__tablename__ = 'used_share_record'
	id = db.Column(db.Integer, primary_key=True)
	# 起始經緯度
	begin_location_lat = db.Column(db.Float, nullable=True)
	begin_location_lng = db.Column(db.Float, nullable=True)
	begin_address_description = db.Column(db.String(255), nullable=True)

	# 目的地經緯度
	end_location_lat = db.Column(db.Float, nullable=True)
	end_location_lng = db.Column(db.Float, nullable=True)
	end_address_description = db.Column(db.String(255), nullable=True)
	# 使用的人的外鍵 id
	used_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	# 共享雨傘的紀錄外鍵 id
	sharer_record_id = db.Column(db.Integer, db.ForeignKey('sharer_record.id'))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<UsedShareRecord: id='%d', used_user_id='%d', \
				begin_location_lat='%s', \
				begin_location_lng='%s', \
				begin_address_description='%s', \
				end_location_lat='%s', \
				end_location_lng='%s', \
				end_address_description='%s'>" % (
			self.id,
			self.used_user_id,
			self.begin_location_lat,
			self.begin_location_lng,
			self.begin_address_description,
			self.end_location_lat,
			self.end_location_lng,
			self.end_address_description
		)
