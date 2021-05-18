from flask import Blueprint, request, jsonify

from house_price_predictor.predict import predict_json

app_blueprint = Blueprint(name='app_blueprint', import_name=__name__)

@app_blueprint.route('/ping', methods=['GET'])
def ping():
    return 'The house price predictor application is responding.'
    
@app_blueprint.route('/v1/predict_house_price', methods=['POST'])
def predict_house_price():
    if request.method == 'POST':
        data = request.get_json()
        results = predict_json(input_json=data)
        results['predictions'] = list(results['predictions'])
        
        return jsonify(results)