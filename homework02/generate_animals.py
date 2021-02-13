#!/usr/bin/env python3

#import required libraries
import json
import random
import petname
import sys

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
    with open(sys.argv[1], 'w') as out:
        json.dump(animal_list, out, indent=2)

if __name__ == '__main__':
	main()












