class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://sasa:123@localhost:5432/flask_d2'


config_options = {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig,
}