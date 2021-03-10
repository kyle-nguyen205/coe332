# Homework 2                                                                                                                        
This homework focuses on containerizing the json-parser scripts in homework 1. Minor changes were made to the files to make them suitable for containerization. New functionality was added to read_animals.py that takes two animals from the animals.json file and "breed" them to create a child sharing the parents' traits. A unit testing script is provided to test the breeding function. A Dockerfile is provided to build the docker image, and a test directory is provided as a location to non-interactively test the container.
                                                                                                                                 
## Installation and Usage

 First, clone the kyle-nguyen205/coe332 repository into your desired directory and access it.           
```bash
git clone https://github.com/kyle-nguyen205/coe332
cd coe332/homework02
```
Overwrite the existing animals.json file by generating a new one.
```bash
python3 generate_animals.py animals.json
```
Read the json file and generate the child. 
```bash
python3 read_animals.py animals.json
```
The child will have one of the parent's heads, a body combination derived from one of each parent's bodies, a number of arms and legs averaged between the two parents, and the tail as the sum of the arms and legs.            
                                                                                                                                                                             
## Building the image

To build the hw2 image, use the included Dockerfile. 

```bash
docker build -t username/code:version .
```
Alternatively, you can pull my docker image from Docker Hub.
```bash
docker pull kdnguyen205/hw2:1.0
```  
You can then build the docker image and interact with it through the terminal.
```bash
docker run --rm -it kdnguyen205/hw2:1.0 /bin/bash
```                                                                                                             
## Using the container
To run the scripts inside the container, simply go the container home directory and run the following commands. Not that the python3 command is no longer needed since the scripts were made executable in the Dockerfile. Exit the container when finished.
```bash
cd /home
generate_animals.py animals.json
read_animals.py animals.json
exit
```
                                                                                                                                                                                                                                  
## Unit Testing the scripts 
To unit test the scripts, simply run the unit testing script.  
```bash
python3 test_read_animals.py
```
This will test the breed function in read_animals.py by feeding it various input types to each of its parameters and individually checking to see if the inputs raise an assertion error.
