import json
import random

def main():

    with open('animals.json', 'r') as f:
        animal_list = json.load(f)
        animal = random.choice(animal_list)
        print(animal)


if __name__ == '__main__':
    main()
