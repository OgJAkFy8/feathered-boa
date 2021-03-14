#! python3
# phoneAndemail.py

import re
import pyperclip

# Create phone Regex
phoneRegex = re.compile(r'''(
    (?:\(|/-)??(\d{3})?(?:\))??(?:\s+|-|\.)?(\d{3})(?:\s|-|\.)?(\d{4})</span></div>
    )''', re.VERBOSE)
# (?:\s|\D)+(?:ext|x|ext.)?(?:\s*)(\d{2,5})?

bizName = re.compile(r'(eName=)["]([A-Z]+[^\.!?"]*)["]')

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in bizName.findall(text):
    matches.append(groups[1])

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[3]])
    # if groups[4] != '':
    #    phoneNum += ' x' + groups[4]
    matches.append(phoneNum)

# Copy to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
