#!/usr/bin/env python3

import json
import random
import sys

#new functionality: animal breeding
#head: randomly choose 1 of the 2 heads of the parents
#body: 2x2 comparison, pick 1st and 2nd set like head, then bring them together
#arms: average, round up to even num
#legs: average, round up to even num
#tail: average, round up to even num

def breed(animal_1, animal_2):

    assert isinstance(animal_1, dict), 'Input 1 to this function should be a dictionary'
    assert isinstance(animal_2, dict), 'Input 2 to this function should be a dictionary'

    head = random.choice( [ animal_1['head'], animal_2['head'] ] )
    
    body_1 = random.choice( animal_1['body'].split('-') )
    body_2 = random.choice( animal_2['body'].split('-') )
    body = body_1 + '-' + body_2

    arms = ( animal_1['arms'] + animal_2['arms'] ) / 2
    arms = int(arms)

    legs = animal_1['legs'] + animal_2['legs']

    tails = arms + legs

    child = {
            'head': head,
            'body': body,
            'arms': arms,
            'legs': legs,
            'tails': tails
            }

    return child

def main():
    with open(sys.argv[1], 'r') as f:
        animal_list = json.load(f)
        animal_1 = random.choice(animal_list)
        animal_2 = random.choice(animal_list)
        
        animal_child = breed(animal_1, animal_2)
        
        print(f'\n Parent 1: \n {animal_1} \n\n Parent 2: \n {animal_2} \n\n Child: \n {animal_child}')
       

if __name__ == '__main__':
    main()
