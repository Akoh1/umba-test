import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Common configurations
    """
    # SECRET_KEY = os.urandom(16)
    SECRET_KEY = "4@4_#h83h2vp3@9f-c-e1y#-oc*=s4#iwkppvf)9kk6(u3tdj^"
    ASSETS_DEBUG = True
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    """
    Configurations
    """
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_ECHO = True
    # test_directory_path = os.path.dirname(os.path.realpath(__file__))
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(test_directory_path, 'intron_db.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_BINDS = {
    #     "test": 'sqlite:///' + os.path.join(test_directory_path, 'intron_db.db')
    # }
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "./main/database/github_users.db")

class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'config': DevelopmentConfig
}
