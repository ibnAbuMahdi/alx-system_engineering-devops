#!/usr/bin/python3
""" gather data from API """
from sys import argv
import json
import requests

if __name__ == '__main__':
	if len(argv) > 1 and argv[1] and isinstance(int(argv[1]), int):
		r = requests.get('https://jsonplaceholder.typicode.com/todos/')
		json_data = r.json()
		user_objs = []
		for obj in json_data:
			if obj.get('userId') == int(argv[1]):
				print('{}\t{}'.format(obj['id'], obj['title']))


