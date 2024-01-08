##OPEN API STUFF
OPENAI_API_KEY = "-your-secret-key"

#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

## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "-your-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}