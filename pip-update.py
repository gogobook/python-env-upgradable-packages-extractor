#!/usr/bin/env python
# first use "pip list --outdated --format json > update.json" to general a json file.
# Then general "update.txt" by this.
# Final use "pip install -r update.txt" to update your env.
import sys, json, subprocess
from datetime import date


def main(u='update.txt'):
    cmd = 'pip list --outdated --format json'
    pipjson = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ulist = json.loads((pipjson.stdout.decode()).strip())
    today = date.today().strftime('%Y%m%d')
    update = 'update' + today + '.txt'
    current = 'current' + today + '.txt'

    with open(update, 'w') as f:
        with open(current, 'w') as c:
            for i in ulist:
                f.write(i['name'] + "==" + i['latest_version'] + '\n')
                c.write(i['name'] + "==" + i['version'] + '\n')


if __name__ == "__main__":
    # execute only if run as a script
    try:
        main(sys.argv[1])
    except:
        main()
