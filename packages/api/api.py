from api import app_factory, config


app = app_factory.create_app(settings = config.dev_config)

if __name__ == '__main__':
    app.run()



"""

@app.route('/predict', methods=['GET', 'PUT'])
def predict():
    if request.method == 'PUT':
        return 'put'
    elif request.method == 'GET':
        return 'get'
"""