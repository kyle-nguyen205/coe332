import json, requests

def main():
    print('version 1.0')
    print('initializing data')
    response = requests.get(url='http://localhost:5022/init')
    print('data initialized \n')
    
    print('getting all animals')
    response = requests.get(url='http://localhost:5022/animals')
    print(response.json())

    print('\nquerying animals by date')
    print('start = 2021-04-04 01:29:18.993')
    print('end = 2021-04-04 01:29:18.994')
    response = requests.get(url='http://localhost:5022/animals/dates?start=2021-04-04_01:29:18.993&end=2021-04-04_01:29:18.994')
    print(response.json())

    print('\nselecting animal by uid 9756a5c8-3171-406e-9064-de2864729788')
    response = requests.get(url='http://localhost:5022/animals/uid/9756a5c8-3171-406e-9064-de2864729788')
    print(response.json())

    print('\nediting animal uid 9756a5c8-3171-406e-9064-de2864729788 with raven head')
    response = requests.get(url = 'http://localhost:5022/animals/edit?uid=9756a5c8-3171-406e-9064-de2864729788&field=head&change=raven')
    print(response.json())

    print('\ndeleting animals by date')
    print('start = 2021-04-04 01:29:18.993')
    print('end = 2021-04-04 01:29:18.994')
    response = requests.get(url='http://localhost:5022/animals/delete?start=2021-04-04_01:29:18.993&end=2021-04-04_01:29:18.994')
    print(response.json())

    print('\naverage legs of remaining animals')
    response = requests.get(url='http://localhost:5022/animals/legs')
    print(response.json())

    print('\ntotal animals remaining')
    response = requests.get(url='http://localhost:5022/animals/total_count')
    print(response.json())

#    query_date()
#    select_uid()
#    edit_creature()
#    delete_animals()
#    avg_legs()
#    total_count()

if __name__ == '__main__':
    main()
