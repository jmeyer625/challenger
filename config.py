import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you could never find this out'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	CHALLENGER_MAIL_SUBJECT_PREFIX = '[Challenger]'
	CHALLENGER_MAIL_SENDER = 'Challenger Admin <challengerapplication@gmail.com>'
	CHALLENGER_ADMIN = os.environ.get('CHALLENGER_ADMIN')
	MANDRILL_API_KEY = os.environ.get('MANDRILL_API_KEY')
	MANDRILL_DEFAULT_FROM = os.environ.get('MANDRILL_DEFAULT_FROM')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:////' + os.path.join(basedir, 'challenger.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:////' + os.path.join(basedir, 'challenger.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:////' + os.path.join(basedir, 'challenger.sqlite')

config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,

	'default' : DevelopmentConfig
}