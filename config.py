import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRETE_KEY = os.environ.get('XUEJIAO-BLOG-SECRET-KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_163_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_163_PASSWORD')
    BLOG_MAIL_SUBJECT_PREFIX = "[XUEJIAO'S BLOG]"
    BLOG_MAIL_SENDER = 'Xue Jiao <m13488699851@163.com>'
    BLOG_ADMIN = os.environ.get('XUEJIAO-BLOG-ADMIN')

    @staticmethod
    def init_app(app):
        pass
    

class DevelopmentConfig(Config):
    DEBUT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHMEY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
    }
