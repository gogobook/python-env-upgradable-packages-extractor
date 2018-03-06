#!/usr/bin/env python
# first use "pip list --outdated --format json > update.json" to general a json file.
# Then general "update.txt" by this.
# Final use "pip install -r update.txt" to update your env.
import sys
import json

def main(u='update.txt'):
    l=[]
    with open(u,'w') as f:
        with open('update.json') as update:
            u = update.read()
            l = json.loads(u)
        for i in l:
            f.write(i['name']+"=="+i['latest_version']+'\n')

if __name__ == "__main__":
    # execute only if run as a script
    try:
        main(sys.argv[1])
    except:
        main()

