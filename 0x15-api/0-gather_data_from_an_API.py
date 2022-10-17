#!/usr/bin/python3
""" Return information about TODO list progress for a given employee ID. """
import requests as request
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usage = "Usage: ./0-gather_data_from_an_API.py <employee_id>"

    try:
        if len(sys.argv) != 2:
            raise ValueError(usage)

        employee_id = int(sys.argv[1])
        number_of_tasks = 0
        number_of_done_tasks = 0
        titles = []
        employee = request.get(url + "users/{}".format(employee_id)).json()

        params = {"userId": employee_id}
        tasks = request.get(url + "todos", params=params).json()

        for task in tasks:
            number_of_tasks += 1
            if task.get("completed"):
                number_of_done_tasks += 1
                titles.append(task.get("title"))

        print("Employee {} is done with tasks({}/{}):"
              .format(employee.get("name"),
                      number_of_done_tasks, number_of_tasks))

        for title in titles:
            print("\t {}".format(title))
    except Exception:
        exit
