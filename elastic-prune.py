#!/usr/bin/env python

import requests, json
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--elastic', help='Elastic URL (e.g. https://elastic.mysite.org)', default = '', required = True)
parser.add_argument('-d', '--days', help='Age in days to delete from (default 3)', type=int, default = 3, required = False)
parser.add_argument('-b', '--bogus', help='If present, delete records newer than today', action='store_true')
args = parser.parse_args()

print(args)

to_be_deleted = []
today = datetime.datetime.now()

r = requests.get('%s/_stats/store' % args.elastic)
for index in r.json()['indices']:
    try:
        index_date = datetime.datetime.strptime(index, "logstash-%Y.%m.%d")
        age = (today - index_date).days
        print("%20s %s [age=%u]" % (index, r.json()['indices'][index]['primaries']['store']['size_in_bytes'], age))
        if (age > args.days):
            to_be_deleted.append(index)
        if args.bogus and age < 0:
            to_be_deleted.append(index)
    except ValueError:
        # e.g. .kibana index has no date
        pass

for index in to_be_deleted:
    print("Delete index: <<%s>>" % index)
    r = requests.delete('%s/%s' % (args.elastic, index))

if len(to_be_deleted):
    r = requests.put('%s/_all/_settings' % args.elastic, json={"index.blocks.read_only_allow_delete": None})

r = requests.get('%s/_stats/store' % args.elastic)
for index in r.json()['indices']:
    r = requests.put('%s/%s/_settings' % (args.elastic, index), json={"index.blocks.read_only_allow_delete": None})

