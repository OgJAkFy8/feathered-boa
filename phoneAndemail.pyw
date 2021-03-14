#! python3
# phoneAndemail.py

import pyperclip
import re

# Create phone Regex
phoneRegex = re.compile(r'''(
    (?:\(|/-)??(\d{3})?(?:\))??(?:\s+|-|\.)?(\d{3})(?:\s|-|\.)?(\d{4})</span></div>
    )''', re.VERBOSE)
    #(?:\s|\D)+(?:ext|x|ext.)?(?:\s*)(\d{2,5})?


# Create email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # Username
    @                                   # @ Separator
    [a-zA-Z0-9.-]+                      # Domain name
    (\.[a-zA-Z]{2,4})                   # dot Something
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[3]])
    #if groups[4] != '':
    #    phoneNum += ' x' + groups[4]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
