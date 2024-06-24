import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure  # Importe sua classe FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member', methods=['POST'])
def add_member():
    try:
        data = request.json
        new_member = {
            "first_name": data["first_name"],
            "last_name": jackson_family.last_name,
            "age": data["age"],
            "lucky_numbers": data["lucky_numbers"]
        }
        response = jackson_family.add_member(new_member)
        return jsonify(response), 200
    except KeyError as e:
        return jsonify({"error": f"Missing key in request body: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": f"Member with ID {member_id} not found"}), 404


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        if jackson_family.delete_member(member_id):
            return jsonify({"done": True}), 200
        else:
            return jsonify({"error": f"Member with ID {member_id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
