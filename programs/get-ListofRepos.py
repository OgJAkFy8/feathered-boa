import pyperclip
import requests

repo = ''
repolist = []
outputdict = {
    1: 'Markdown Name w/Link',
    2: 'Project Name',
    3: 'Project URL',
    4: 'Project Name and URL'
}

for i in outputdict:
    print('{0}) {1}'.format(i, outputdict[i]))

outputFormat = eval(input('Select the output format: '))
username = 'OgJAkFy8'  # input("Enter the github username:")
userURL = 'https://api.github.com/users/{0}/repos'.format(username)

print(userURL)
print(outputdict[outputFormat])

request = requests.get(userURL)
json = request.json()
for i in range(0, len(json)):
    if outputFormat == 1:
        repo = '[{0}]({1})  '.format(json[i]['name'], json[i]['svn_url'])
    elif outputFormat == 2:
        repo = '{0}'.format(json[i]['name'])
    elif outputFormat == 3:
        repo = '{0}'.format(json[i]['svn_url'])
    elif outputFormat == 4:
        repo = '{0} - {1}'.format(json[i]['name'], json[i]['svn_url'])
    else:
        print(repo)

    repolist.append(repo)

print('Total public repos:', len(repolist))
print('Copied to the clipboard.  Press "CTRL+V" to paste the results.')
if len(repolist) > 0:
    pyperclip.copy('\n'.join(repolist))
