#!/usr/bin/python3
""" gather data from API """
from sys import argv
import json
import requests

if __name__ == '__main__':
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    todos_json_data = todos.json()
    users_json_data = users.json()
    users_all_dict = {}
    for user in users_json_data:
        u_id = user.get('id')
        username = user.get('username')
        json_data = []
        for obj in todos_json_data:
            if u_id == obj.get('userId'):
                json_data.append([username, obj.get('title'),
                                  obj.get('completed')])
        keys = ["username", "task", "completed"]
        dict_list = []
        for vals in json_data:
            dict_list.append(dict(zip(keys, vals)))
        users_all_dict.update({str(u_id): dict_list})
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(users_all_dict, json_file)
