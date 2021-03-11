# Homework 2                                                                                                                       

This homework focuses on creating a flask app that reads data from the animals.json file created in previous homeworks. The app contains routes to the data that either returns all of the animals, animals with matching bodies, or animals with matching number of tails depending on the URL parameters. Additionally, an animal_consumer script is created that can request animals.json data from other flask servers. These apps are all containerized and the corresponding image can be pulled off of Dockerhub.

## Installation

 First, clone the kyle-nguyen205/coe332 repository into your desired directory and access it.           
```bash
git clone https://github.com/kyle-nguyen205/coe332
cd coe332/homework03
```
You can access the flask app in two ways, directly or through a docker container. The direct method involves running flask, which will require two terminal windows. Start the flask app on one terminal window, and reserve the second window for the usage section.
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -h localhost -p <port number>
```
Note that the port number will correspond to your assigned port number.

The alternative method involves downloading the docker image and running the flask app in a container. This will not require two terminal windows since the flask server will run inside the container. As long as the container is running, the flask server will be active. 
```
docker pull kdnguyen205/hw3:1.0
docker run --name <container name> -d -p <port number>:5000 kdnguyen205/hw3:1.0
```        

## Usage

You can interact with the app in two ways, either manually through curl or automatically with animal_consumer.py. Use curl if you want to experiment with different parameters.
```
curl localhost:5022/animals
curl localhost:5022/animals/body/kodiak
curl localhost:5022/animals/tails/5
```
The first command will output a list of all the animals and their properties. The second command will output all animals with a kodiak body. Replacing kodiak with a different animal will search for animals that match the input body. Similarly, the third function will search for all animals with the same amount of tails, and the amount can be adjusted as desired.

Alternatively, you can use animal_consumer.py, which automatically requests the URL's in the script. The script by default accesses port 5025, but can be modified to access the URL's curled above. It also gets the status code and headers for each request. 
```
python3 animal_consumer.py
```      
The curl and animal_consumer.py URL's can all be modified to access routes from other flask servers.
