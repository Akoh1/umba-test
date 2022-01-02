import os
from decouple import config
basedir = os.path.abspath(os.path.dirname(__file__))

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     # SECRET_KEY = '\xec,\x1aK2RA\x05\x04\x89\x04-P\xda\xb9\xec\x04xcm\x8e\xfc\xcf,'
#     SECRET_KEY = config('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "./main/database/github_users.db")

    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
  
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = '\xec,\x1aK2RA\x05\x04\x89\x04-P\xda\xb9\xec\x04xcm\x8e\xfc\xcf,'
    # SECRET_KEY = "4@4_#h83h2vp3@9f-c-e1y#-oc*=s4#iwkppvf)9kk6(u3tdj^"
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "./main/database/github_users.db")

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True