from flask import Blueprint, request, jsonify
import json

requests = Blueprint('requests',__name__)

@requests.route('/tag', methods = ['GET'])
def tag_retrieve():
    if methods == 'GET':
        return jsonify()

@requests.route('/categories', methods = ['GET'])
def categories_retrieve():
    if methods == 'GET':
        return jsonify()