from flask import Blueprint, jsonify

blueprint = Blueprint('food_manage_manage', __name__)


@blueprint.route('/api/v1/dish/modifyDishInfo', endpoint='modifyDishInfo')
def modifyDishInfo():
    errorCode = 0
    errorMessage = 'success'
    resultObj = {'cmd': 'modifyDishInfo', 'errorCode': errorCode, 'errorMessage': errorMessage}
    return jsonify(resultObj)
