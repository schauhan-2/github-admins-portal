import requests
import json
import csv
import os

session = requests.Session()
access_token = os.environ.get('github')
session.headers.update({'Authorization': f'Bearer {access_token}'})
org = 'schauhan2-test'

file = open('admin-portal/_data/output.csv','w', newline='')
writer = csv.writer(file)
writer.writerow(['repository','user','role'])

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