#!/usr/bin/python3
""" gather data from API """
from sys import argv
import csv
import requests

if __name__ == '__main__':
    if len(argv) > 1 and argv[1] and argv[1].isdigit():
        todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
        users = requests.get('https://jsonplaceholder.typicode.com/users/')
        todos_json_data = todos.json()
        users_json_data = users.json()
        user_todos_objs = []
        for obj in todos_json_data:
            if obj.get('userId') == int(argv[1]):
                user_todos_objs.append(obj)
        user = None
        for obj in users_json_data:
            if obj.get('id') == int(argv[1]):
                user = obj.get('username')
        csv_data = []
        if user and len(user_todos_objs):
            for obj in user_todos_objs:
                csv_data.append([argv[1], user,
                                 obj.get('completed'),
                                 obj.get('title')])
        with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

            for data in csv_data:
                writer.writerow(data)
