import requests
import json

session = requests.Session()
access_token = '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'
session.headers.update({'Authorization': f'Bearer {access_token}'})
org = 'schauhan2-test'

repoResponse = session.get(f'https://api.github.com/orgs/{org}/repos')
repos = json.loads(repoResponse.content)

for repo in repos:
    repoName = repo['name']
    ownerName = repo['owner']['login']
    collaboratorsResponse = session.get(f'https://api.github.com/repos/{ownerName}/{repoName}/collaborators')
    collaborators = json.loads(collaboratorsResponse.content)
    print("======" + repoName + "======")
    for collaborator in collaborators:
        userPermission = collaborator['permissions']
        if (userPermission['admin'] == True):
            print(collaborator['login'] + "    admin")
        elif (userPermission['maintain'] == True):
            print(collaborator['login'] + "    maintainer")
        else:
            print(collaborator['login'] + "    not-admin")