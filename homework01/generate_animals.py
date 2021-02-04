#Create 20 animals and dump them into a json file
#Each animal will have a:
	#head: randomly chosen from snake, bull, lion, raven, bunny
	#body: 2 animals randomly chosen using petname library
	#arms: random # of arms, must be an even number b/w 2-10 inclusive
	#legs: random # of legs, must be a multiple of 3 and between 3-12, inclusive
	#tails: equal to sum of arms and legs
#Each of the 20 animals should be accessible from a list of dictionaries. Use json library to dump your data structure into an animals json
#Then, create a new python script to read in animals.json and print the details of one animal at random to screen
#Need to submit 3 files in folder homework01: generate_animals.py, animals.json (output), and read_animals.py

#START OUTLINE

#import required libraries
import json
import random
import petname

#functions:
def choose_head():
    head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']
    return random.choice(head_list)


def choose_body():
    name1 = petname.name()
    name2 = petname.name()

    return name1 + '-' + name2


def choose_arms():
    return random.randrange(2, 11, 2)


def choose_legs():
    return random.randrange(3, 13, 3)


def choose_tails(arms, legs):
    return arms + legs


def main():
    num_animals = 20
    animal_list = [{}]*num_animals

    for i in range(0, num_animals):
        head = choose_head()
        body = choose_body()
        arms = choose_arms()
        legs = choose_legs()
        tails = choose_tails(arms, legs)

        animal = {
            'head': head,
            'body': body,
            'arms': arms,
            'legs': legs,
            'tails': tails
        }
        animal_list[i] = animal
  
    #print(animal)
    with open('animals.json', 'w') as out:
        json.dump(animal_list, out, indent=2)

if __name__ == '__main__':
	main()












