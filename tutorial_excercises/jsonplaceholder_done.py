"""
{
    1 : 11
    2 : 6
    3 : 15
}

"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)
def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1
    return completedTaskFrequencyByUser

def get_keys_with_top_value(my_dict):
    return [
        key
        for key, value in my_dict.items
        if value == max(my_dict.values())
    ]


def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks=[]
    maxValueOfCompletedTask = max(completedTaskFrequencyByUser.values())          
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTasks == maxValueOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks


try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkowników o Id:", usersWithTopCompletedTasks)

          
          
          
