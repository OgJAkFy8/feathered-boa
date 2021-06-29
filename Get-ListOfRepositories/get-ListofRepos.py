import time
import requests
import os

repo = ''
repolist = []
outfilename = 'RepositoryList.txt'
Outfile = open(outfilename, 'a')

# username = 'OgJAkFy8'  
username = input("Enter the github username: ")
userURL = 'https://api.github.com/users/{0}/repos'.format(username)

print(userURL)

request = requests.get(userURL)
json = request.json()
for i in range(0, len(json)):
    repo = '"{0}","{1}" \n'.format(json[i]['name'], json[i]['svn_url'])
    Outfile.write(repo)
    repolist.append(repo)

Outfile.close()

if len(repolist) > 0:
    # File Name
    timestamp = time.strftime("%d%M%S")
    name = '-' + timestamp + username + 'x.txt'
    filename = outfilename.replace('.txt', name)
    print(filename)
    os.rename(outfilename, filename)

print('Total public repos:', len(repolist))

