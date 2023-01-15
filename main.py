import os
with open('/etc/secrets/botToken.json', 'r', encoding = 'utf8') as jfile:
    botTokenJson = json.load(jfile)
jfile.close()
print(botToken)