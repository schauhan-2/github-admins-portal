import requests
import json
import csv

session = requests.Session()
access_token = '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'
session.headers.update({'Authorization': f'Bearer {access_token}'})
org = 'schauhan2-test'

file = open('output.csv','w', newline='')
writer = csv.writer(file)

repoResponse = session.get(f'https://api.github.com/orgs/{org}/repos')
repos = json.loads(repoResponse.content)


for repo in repos:
    repoName = repo['name']
    ownerName = repo['owner']['login']
    collaboratorsResponse = session.get(f'https://api.github.com/repos/{ownerName}/{repoName}/collaborators')
    collaborators = json.loads(collaboratorsResponse.content)
    for collaborator in collaborators:
        userPermission = collaborator['permissions']
        if (userPermission['admin'] == True):
            writer.writerow([repoName, collaborator['login'],"admin"])
        elif (userPermission['maintain'] == True):
            writer.writerow([repoName, collaborator['login'],"maintainer"])
        else:
            writer.writerow([repoName, collaborator['login'],"not-admin"])

file.close()