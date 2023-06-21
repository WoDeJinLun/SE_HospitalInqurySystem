from flask import Flask, request, jsonify
from flask_cors import CORS
from mysql_interface import MysqlInterface
from use import AiQuery
app = Flask(__name__)
cors = CORS(app,supports_credentials=True)
# CORS(app, resources=r'/*', supports_credentials=True)
mysql_interface = MysqlInterface()
ai_interface = AiQuery()
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

@app.route('/ai/',methods =['get'])
def GetAiPrompt():
    sentence = request.values.get('message')
    
    prompt = ai_interface.query(sentence)
    return jsonify({"message":"{}".format(prompt)})

@app.route('/medical_records', methods=['POST'])
def create_medical_record():
    data = request.json
    patient_id = data['patient_id']
    patient_name = data['patient_name']
    gender = data['gender']
    age = data['age']
    diagnosis = data['diagnosis']
    treatment_plan = data['treatment_plan']

    mysql_interface.create_medical_record(patient_id, patient_name, gender, age, diagnosis, treatment_plan)

    return jsonify({"message": "Medical record created successfully"})

@app.route('/drug_receipts', methods=['POST'])
def create_drug_receipt():
    data = request.json
    patient_id = data['patient_id']
    patient_name = data['patient_name']
    drug_name = data['drug_name']
    unit_price = data['unit_price']
    quantity = data['quantity']

    mysql_interface.create_drug_receipt(patient_id, patient_name, drug_name, unit_price, quantity)

    return jsonify({"message": "Drug receipt created successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
