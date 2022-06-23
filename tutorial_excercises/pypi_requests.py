import requests

def webFilter(listOfSites):
    workingPages = []
    notWorkingPages = []
    for page in listOfSites:
        response = requests.get(page)
        response_code = response.status_code
        if response_code == 200:
            workingPages.append(page)
        else:
            notWorkingPages.append(page)
    print("Działające strony: ", workingPages)
    print("Nie działające strony: ", notWorkingPages)
    return "\n"


        
listOfSites = ["https://videokurs.pl/", "https://videokurs.pl/asfasdsa", "https://dostepy.pl/pl/"]
    
print(webFilter(listOfSites))



