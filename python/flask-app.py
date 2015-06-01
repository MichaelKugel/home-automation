#!python
#Author: mkugel (c) 2015
#FortiGate CLI via expect to REST API using a flask app.

from flask import Flask, jsonify, abort, make_response, request
import paho.mqtt.publish as publish


app = Flask(__name__)

#Default Policies in JSON format.

policies = [
    {
        'id': 1,
        'title': u'Whitelist Facebook',
        'description': u'Whitelist all Facebook APIs', 
        'active': False
    },
    {
        'id': 2,
        'title': u'Whitelist YouTube',
        'description': u'Whitelist all YouTube APIs', 
        'active': False
    }
]

@app.route('/filter/api/v1.0/policies', methods=['POST'])
def create_policy():
    if not request.json or not 'title' in request.json:
        abort(400)
    policy = {
        'id': policies[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'active': False
    }
    policies.append(policy)
    return jsonify({'policy': policy}), 201

@app.route('/filter/api/v1.0/policies', methods=['GET'])
def get_policies():
    return jsonify({'policies': policies})

@app.route('/filter/api/v1.0/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    policy = [policy for policy in policies if policy['id'] == policy_id]
    if len(policy) == 0:
        abort(404)
    return jsonify({'policy': policy[0]})

@app.route('/filter/api/v1.0/policies/<int:policy_id>', methods=['PUT'])
def update_policy(policy_id):
    policy = [policy for policy in policies if policy['id'] == policy_id]
    if len(policy) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'active' in request.json and type(request.json['active']) is not bool:
        abort(400)
    policy[0]['title'] = request.json.get('title', policy[0]['title'])
    policy[0]['description'] = request.json.get('description', policy[0]['description'])
    policy[0]['active'] = request.json.get('active', policy[0]['active'])
    return jsonify({'policy': policy[0]})

@app.route('/filter/api/v1.0/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    policy = [policy for policy in policies if policy['id'] == policy_id]
    if len(policy) == 0:
        abort(404)
    policies.remove(policy[0])
    return jsonify({'result': True})

@app.route("/message/<path:argument>", methods=["GET"])
def foo(argument):
    msgs = [{'topic': argument, 'payload':"REST to MQTT"},
    (argument, "second message", 0, False)]
    publish.multiple(msgs, hostname="10.37.85.223")
    return "GOT: %s" % argument

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

