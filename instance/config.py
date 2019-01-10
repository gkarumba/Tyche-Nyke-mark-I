
class Config():
    """
        Parent Configuration Class
    """
    DEBUG = True
    CSRF_ENABLED = True
    TEST = False

class DevelopmentConfig(Config):
    """
        Class for the development configuration
    """
    DEBUG  = True

class TestingConfig(Config):
    DEBUG = True
    TEST = True
    """
        Class for the testing configuration
    """

config = {
    "development_config" : DevelopmentConfig,
    "testing_config" : TestingConfig
}
