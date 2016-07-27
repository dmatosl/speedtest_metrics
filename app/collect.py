#!/usr/bin/env python

from subprocess import Popen, PIPE
from time import gmtime, strftime
from influxdb import InfluxDBClient
import re
import os

out = Popen(
        ["speedtest-cli", "--simple" ],
        stdout=PIPE
    ).communicate()[0]

out_list = out.split('\n')

# Mock sucessfull result
# out_list = ['Ping: 10.231 ms', 'Download: 0.74 Mbit/s', 'Upload: 2.40 Mbit/s', '']

# sample output: ['Ping: 10.231 ms', 'Download: 0.74 Mbit/s', 'Upload: 2.40 Mbit/s', '']
# sucessfull test: len = 4

if len(out_list) == 4:
    match_ping = re.match(r'Ping\:\s(.+)\sms', out_list[0])
    match_download = re.match(r'Download\:\s(.+)\sMbit\/s', out_list[1])
    match_upload = re.match(r'Upload\:\s(.+)\sMbit\/s', out_list[2])

    _ping = match_ping.group(1)
    _download = match_download.group(1)
    _upload = match_upload.group(1)

    json_body = [
        {
            "measurement" : "speedtest_metrics" ,
            "tags": {
                "host": "iron.lan",
                "region": "home"
            },
            "fields": {
                "ping": _ping,
                "download" : _download,
                "upload": _upload
            }
        }
    ]

    client = InfluxDBClient(
        os.environ['INFLUXDB_HOST'],
        os.environ['INFLUXDB_PORT'],
        os.environ['INFLUXDB_USER'],
        os.environ['INFLUXDB_PASSWORD'],
        os.environ['INFLUXDB_DATABASE']
    )

    client.create_database(os.environ['INFLUXDB_DATABASE'])
    client.create_retention_policy("speedtest_policy", "30d",1, default=True)
    
    # writing points
    print "===> writing points"
    client.write_points(json_body)

else:
    print "failed to retrieve data"
