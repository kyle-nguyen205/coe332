import json
from flask import Flask

app = Flask(__name__)

def get_data():
    with open('animals.json', 'r') as json_file:
        userdata = json.load(json_file)
        return userdata

#list all animals
@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps(get_data()) + '\n'

#lists all animals that have the input body type
@app.route('/animals/body/<body>', methods=['GET'])
def get_animals_body(body):
    data = get_data()
    output = [x for x in data if body in x['body']]
    return json.dumps(output) + '\n'

#lists all animals that have the input number of tails
@app.route('/animals/tails/<tails>', methods=['GET'])
def get_animals_tails(tails):
    data = get_data()
    output = [x for x in data if x['tails'] == int(tails)]
    return json.dumps(output) + '\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
