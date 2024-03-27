#!/usr/bin/python3
'''get data from an api'''

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # send a GET request to retrieve user info
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # send a GET request to retrive the TODO list
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # filter completed TODO list and store titles in a list
    completed = [task.get("title") for task in todos if task.get("completed") is True]

    # print employee's name, completed tasks & total no of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # print the titles of completed tasks with indentation
    [print("\t {}".format(c)) for c in completed]
