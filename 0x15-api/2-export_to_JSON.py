#!/usr/bin/python3
""" gather data from API """
from sys import argv
import json
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
        json_data = []
        if user and len(user_todos_objs):
            for obj in user_todos_objs:
                json_data.append([obj.get('title'),
                                  obj.get('completed'),
                                  user])
            keys = ["task", "completed", "username"]
            dict_list = []
            for vals in json_data:
                dict_list.append(dict(zip(keys, vals)))
            json_obj = {str(argv[1]): dict_list}
            with open('{}.json'.format(argv[1]), mode='w') as json_file:
                json.dump(json_obj, json_file)
