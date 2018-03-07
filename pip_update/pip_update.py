#!/usr/bin/env python
# first use "pip list --outdated --format json > update.json" to general a json file.
# Then general "update.txt" by this.
# Final use "pip install -r update.txt" to update your env.
from __future__ import print_function

import json, subprocess, os
from datetime import date

CMD = 'pip list --outdated --format json'


def extract(cmd, folder='pip-update'):

    try:
        pipjson = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print("pip list execute fail")
    ulist = json.loads((pipjson.stdout.decode()).strip())
    today = date.today().strftime('%Y%m%d')
    update = './' + folder + '/update' + '.txt'
    current = './' + folder + '/current' + today + '.txt'
    os.makedirs(folder, exist_ok=True)

    try:
        with open(update, 'w') as f:
            with open(current, 'w') as c:
                for i in ulist:
                    f.write(i['name'] + "==" + i['latest_version'] + '\n')
                    c.write(i['name'] + "==" + i['version'] + '\n')
    except:
        print("Can not write files!")
