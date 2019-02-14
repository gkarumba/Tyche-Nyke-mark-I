import os

class Config():
    """
        Parent Configuration Class
    """
    DEBUG = False
    CSRF_ENABLED = True
    TEST = False

class DevelopmentConfig(Config):
    """
        Class for the development configuration
    """
    DEBUG  = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """
        Class for the testing configuration
    """
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv('TEST_DB_URL')

class ProductionConfig(Config):
    """
        Class for the production configuration
    """
    DEBUG = False
    TEST = False

config = {
    "development_config" : DevelopmentConfig,
    "testing_config" : TestingConfig,
    "production_config" : ProductionConfig
}

