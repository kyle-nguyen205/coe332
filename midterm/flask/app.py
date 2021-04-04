import json, redis, uuid, datetime
from flask import Flask, request

app = Flask(__name__)
rd = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
num_animals = 20

###############################
### Commonly Used Functions ###
###############################
def get_data():
    animals = [{}] * num_animals
    for i in range(0, num_animals):
        output = rd.hgetall(str(i))
        animals[i] = output
    return animals

def get_dates(start, end):
    start_date = datetime.datetime.strptime(start, '%Y-%m-%d_%H:%M:%S.%f')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d_%H:%M:%S.%f')

    animals = get_data()
    output = [x for x in animals if \
            datetime.datetime.strptime(x['created_on'], '%Y-%m-%d %H:%M:%S.%f') >= start_date and \
            datetime.datetime.strptime(x['created_on'], '%Y-%m-%d %H:%M:%S.%f') <= end_date] 
    return output

def get_uid(uid):
    animals = get_data()
    output = [x for x in animals if uid in x['uid']]
    return output

##############
### Routes ###
##############
@app.route('/init', methods=['GET'])
def init():
    with open('/data_file.json', 'r') as data_file:
        animals = json.load(data_file)
        for i in range(0, 20):
            rd.hmset(str(i), animals[i])
    return 'db initialized\n' 

@app.route('/animals', methods=['GET'])
def get_animals():
    output = get_data()
    return json.dumps(output) + '\n'

#REMINDER: URL needs to be in quotes when you curl, since it contains the & symbol which messes things up
# ex: curl "localhost:5022/animals/dates?start=2021-03-28_18:22:41.00&end=2021-03-28_18:22:45.00"
@app.route('/animals/dates', methods=['GET'])
def query_dates():
    start = request.args.get('start')
    end = request.args.get('end')
    output = get_dates(start, end)
    return json.dumps(output) + '\n'

@app.route('/animals/uid/<uid>', methods=['GET'])
def select_uid(uid):
    output = get_uid(uid)
    return json.dumps(output) + '\n'

@app.route('/animals/edit', methods=['GET'])
def edit_animal():
    uid = request.args.get('uid')
    field = request.args.get('field')
    change = request.args.get('change')

    animals = get_data()
    animal = get_uid(uid)
    index = animals.index(animal[0])
    output = rd.hset(str(index), field, change)
    new_animal = get_uid(uid)
    return json.dumps(new_animal) + '\n'

@app.route('/animals/delete', methods=['GET'])
def delete_animal():
    start = request.args.get('start')
    end = request.args.get('end')
    deleted_animals = get_dates(start, end)

    animals = get_data()
    for i in range(0, len(deleted_animals)):
        index = animals.index(deleted_animals[i])
        output = rd.delete(str(index))
    return json.dumps(get_data()) + '\n'

@app.route('/animals/legs', methods=['GET'])
def avg_legs():
    animals = get_data()
    total_count = 0
    leg_count = 0
    for i in range(0, num_animals):
        if animals[i] == {}:
            continue
        else:
            total_count = total_count + 1
            leg_count = leg_count + int(animals[i]['legs'])
    return str(float(leg_count)/total_count) + '\n'

@app.route('/animals/total_count', methods=['GET'])
def total_count():
    animals = get_data()
    count = 0
    for i in range(0, num_animals):
        if animals[i] == {}:
            continue
        else:
            count = count + 1
    return str(count) + '\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
