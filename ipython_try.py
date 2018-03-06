# coding: utf-8
import subprocess
cmd = 'ls -l'
cmd = 'pip list'
piplist = subprocess.call(cmd, shell=True)
cmd = 'pip list --outdated --format json'
pipjson = subprocess.call(cmd, shell=True)
pipjson
pipjson = subprocess.Popen(cmd, shell=True,stdout=PIPE,stderr=PIPE)
pipjson = subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
pipjson
pipjson = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
pipjson
pipjson.communicate()
jsonb = pipjson.communicate()
bstring = pipjson.communicate()
bstring = pipjson.communicate().decode()
stdout
stdout=''
pipjson = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout
pipjson = subprocess.run(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout
pipjson
ustring=pipjson.encode()
ustring=pipjson.__dict__
ustring
pipjson.__dict__
pipjson.output
pipjson.stdout
ustring=pipjson.stdout.encode()
ustring=pipjson.stdout.decode()
ustring
ulist = ustring.strip()
ulist
import json
jstring = json.loads(ustring)
jstring
ustring=pipjson.stdout.decode
jstring = json.loads(ustring)
ustring=pipjson.stdout.decode.strip
ustring=pipjson.stdout.decode.strip()
import datetime
today = datetime.date
today
today = datetime.date()
today = datetime.date.today()
today
today.isoformat()
today.strftime('%y%m%d)
today.strftime('%y%m%d")
today.strftime('%y%m%d')
today.strftime('%Y%m%d')
# lsmagic 可檢視可用的魔術指令