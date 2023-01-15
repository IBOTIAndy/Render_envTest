import os
import glob
path = './**/*.*'
for file in glob.glob(path, recursive=True):
    print(file)

#with open('/etc/secrets/botToken.json', 'r', encoding = 'utf8') as jfile:
#    botTokenJson = json.load(jfile)
#jfile.close()
#print(botToken)