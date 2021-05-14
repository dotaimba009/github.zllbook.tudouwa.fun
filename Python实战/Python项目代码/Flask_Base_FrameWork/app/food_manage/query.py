from flask import Blueprint, jsonify

blueprint = Blueprint('food_manage_query', __name__)


@blueprint.route('/api/v1/dish/getDishCount')
def getDishCount():
    errorCode = 0
    errorMessage = 'success'
    resultObj = {'cmd': 'get_dish_count', 'errorCode': errorCode, 'errorMessage': errorMessage, 'dish_count': 12}
    return jsonify(resultObj)


@blueprint.route('/api/v1/dish/getDishCount1')
def getDishCount1():
    errorCode = 0
    errorMessage = 'success'
    resultObj = {'cmd': 'get_dish_count', 'errorCode': errorCode, 'errorMessage': errorMessage, 'dish_count': 12}
    dd = []
    print("pro1---=", dd[0])
    print("pro1------2")
    return jsonify(resultObj)
