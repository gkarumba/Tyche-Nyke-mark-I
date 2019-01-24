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
    TEST = True
    DATABASE_URL = os.getenv('TEST_DB_URL')

config = {
    "development_config" : DevelopmentConfig,
    "testing_config" : TestingConfig
}

