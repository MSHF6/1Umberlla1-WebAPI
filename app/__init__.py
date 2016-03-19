
# -*- coding:utf-8 -*-
import os
from flask import Flask
from database import db



def create_app(config):
	app = Flask(__name__)
	app.config.from_object(config)
	# 載入 db model

	from db.common import *
	from db.user import *
	from db.share import *
	db.init_app(app)

	# # 安裝 JSGlue
	# jsglue = JSGlue()
	# jsglue.init_app(app)

	# # Session Secret Key
	app.secret_key = os.urandom(24).encode('hex')
	print app.secret_key

	# # 擴充 url map
	# app.url_map.converters['regex'] = RegexConverter
	# # # 安裝 Session 強化擴充
	# # sess = Session()
	# # sess.init_app(app)

	# Blueprint Resources
	from resources import users, user_login
	app.register_blueprint(users.blueprint, url_prefix='/api')
	app.register_blueprint(user_login.blueprint, url_prefix='/api')
	return app
