# Midterm Project                                                                                                                        
This midterm project pulls together everything from COE332 up until now. A flask server and redis database is set up and containerized. The flask app from homework 3 is modified to read the animals.json file (now renamed to data_file.json) and output to a redis database. New routes are established that expand the functionality of the flask app, which now interacts only with the redis database.
                                                                                                                                 
## Installation

 First, clone the kyle-nguyen205/coe332 repository into your desired directory and access it.           
```bash
git clone https://github.com/kyle-nguyen205/coe332
cd coe332/midterm
```                                                                                                                                                            
## Building the image

The app is designed to only operate inside a container. Begin by spinning up the services with docker-compose.

```bash
docker-compose -p <project_name> up --build
```
This will bring up the flask server and redis database, but you will need a second terminal window to interact with it


## Using the container
A animal_consumer.py script is provided to easily test out the container. Run the script on the second terminal window.
```bash
python3 ./flask/animal_consumer.py
```
You can also curl the URL's and interact with the container manually, if you prefer. Once you are done, exit out of the container and tear them down.

```bash
docker-compose -p <project_name> down
```
