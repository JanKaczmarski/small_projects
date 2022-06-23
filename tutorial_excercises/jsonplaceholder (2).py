import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser

def get_users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []    
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks
ra = requests.get("https://jsonplaceholder.typicode.com/users")
users = ra.json()

def winning_user(list_of_users):
    for user in list_of_users:
        if (user["id"] in usersWithTopCompletedTasks):
            print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user["name"])
            usersWithTopCompletedTasks.remove(user["id"])
    return " "



try:
    tasks = r.json()
    
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTaskFrequencyByUser)
    winningUsers = winning_user(users)        

#sposob 1
    

"""
#sposob 2
for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user[0]["name"])
"""


