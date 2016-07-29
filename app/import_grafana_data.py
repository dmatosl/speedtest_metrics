#!/usr/bin/env python

import requests
import os

s = requests.Session()
s.headers['Content-Type'] = "Application/json"

if os.environ["GRAFANA_API_KEY"] != "null":
    s.headers['Authorization'] = "Bearer %s" % (os.environ["GRAFANA_API_KEY"])

# grafana endpoints
grafana_login_endpoint = "%s://%s:%s/login" % (
    os.environ["GRAFANA_PROTO"],
    os.environ["GRAFANA_HOST"],
    os.environ["GRAFANA_PORT"]
)
print "grafana_login_endpoint: %s" % (grafana_login_endpoint)

grafana_datasource_endpoint = "%s://%s:%s/api/datasources" % (
    os.environ["GRAFANA_PROTO"],
    os.environ["GRAFANA_HOST"],
    os.environ["GRAFANA_PORT"]
)
print "grafana_datasource_endpoint: %s" %(grafana_datasource_endpoint)

grafana_dashboard_endpoint = "%s://%s:%s/api/dashboards/import" % (
    os.environ["GRAFANA_PROTO"],
    os.environ["GRAFANA_HOST"],
    os.environ["GRAFANA_PORT"]
)
print "grafana_dashboard_endpoint: %s" % (grafana_dashboard_endpoint)

# grafana payloads
grafana_login_payload = '{"user":"%s","email":"","password":"%s"}' % (
    os.environ["GRAFANA_ADMIN_USER"],
    os.environ["GRAFANA_ADMIN_PASS"]
)
print "grafana_login_payload: %s" % (grafana_login_payload)

grafana_datasource_payload = '{"name":"influxdb","type":"influxdb","url":"http://influxdb:8086/","access":"proxy","jsonData":{},"isDefault":true,"database":"speedtest_metrics","user":"admin","password":"admin"}'
grafana_dashboard_payload_file = open('./dashboard.json','r')
grafana_dashboard_payload = grafana_dashboard_payload_file.read().strip()

# grafana login
if os.environ["GRAFANA_API_KEY"] == "null":
    login = s.post(url=grafana_login_endpoint, data=grafana_login_payload)
    if login.status_code == 200:
        print "grafana --> login successful"

# load grafana datasource
datasource =  s.post(url=grafana_datasource_endpoint, data=grafana_datasource_payload)
if datasource.status_code == 200:
    print "grafana --> datasource import successful"

# load grafana dashboard
dashboard = s.post(url=grafana_dashboard_endpoint, data=grafana_dashboard_payload)
if dashboard.status_code == 200:
    print 'grafana --> dashboard import successful'
