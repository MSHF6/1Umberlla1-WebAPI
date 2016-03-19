# -*- coding:utf-8 -*-

"""
設定檔
"""


DATABASE_URL = {
	'DEV_MYSQL': 'mysql://root:pass@word1@localhost/shareUmbrellaDB',
	'TEST_MYSQL': 'mysql://root:pass@word1@localhost/tshareUmbrellaDB'
}


class Config(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = DATABASE_URL["DEV_MYSQL"]
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = DATABASE_URL["TEST_MYSQL"]

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig,
	'testing': TestingConfig
}