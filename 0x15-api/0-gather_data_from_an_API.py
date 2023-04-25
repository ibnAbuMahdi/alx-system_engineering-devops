#!/usr/bin/python3
""" gather data from API """
import json
import requests
from sys import argv

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
        done = 0
        for obj in user_todos_objs:
            if obj.get('completed'):
                done += 1
        user = None
        for obj in users_json_data:
            if obj.get('id') == int(argv[1]):
                user = obj.get('name')
        if user and len(user_todos_objs):
            print('Employee {} is done with \
tasks ({}/{}):'.format(user, done, len(user_todos_objs)))
            for obj in user_todos_objs:
                if obj.get('completed'):
                    print('\t {}'.format(obj.get('title')))
