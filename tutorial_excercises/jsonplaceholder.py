"""
JSONplaceholder - miejsce zastępcze na Twoj przyszly json

"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")


def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry['userId']] += 1                
            except KeyError:
                completedTaskFrequencyByUser[entry['userId']] = 1
    return completedTaskFrequencyByUser

def get_user_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIdWithMaxCompletedAmountOfTasks = []
    MaxAmountOfCompletedTaskUser = max(completedTaskFrequencyByUser.values())
    for userId , numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTasks == MaxAmountOfCompletedTaskUser):
            userIdWithMaxCompletedAmountOfTasks.append(userId)
    return userIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_user_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Wygrywają pracownicy z Id:", usersWithTopCompletedTasks)








