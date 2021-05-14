class dev_config:
    ENV = 'development'
    TESTING = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SERVER_PORT = 5000

class prod_config:
    ENV = 'production'
    TESTING = False
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SERVER_PORT = 5000