from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql_interface import MysqlInterface

app = Flask(__name__)
CORS(app)

mysql_interface = MysqlInterface()

@app.route('/patients', methods=['POST'])
def create_patient():
    data = request.json
    id = data['id']
    name = data['name']
    gender = data['gender']
    age = data['age']
    contact_number = data['contact_number']

    mysql_interface.create_patient(id, name, gender, contact_number, age)

    return jsonify({"message": "Patient record created successfully"})

@app.route('/patients/<int:id>', methods=['GET'])
def retrieve_patient(id):
    patient = mysql_interface.retrieve_patient(id)
    if patient:
        return jsonify({
            "id": patient[0],
            "name": patient[1],
            "gender": patient[2],
            "age": patient[3],
            "contact_number": patient[4]
        })
    else:
        return jsonify({"message": "Patient record not found"})

@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.json
    name = data['name']
    gender = data['gender']
    age = data['age']
    contact_number = data['contact_number']

    updated_data = {
        "name": name,
        "gender": gender,
        "age": age,
        "contact_number": contact_number
    }
    mysql_interface.update_patient(id, updated_data)

    return jsonify({"message": "Patient record updated successfully"})

@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    mysql_interface.delete_patient(id)

    return jsonify({"message": "Patient record deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
