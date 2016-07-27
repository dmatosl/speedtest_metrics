#!/usr/bin/env python

import requests

s = requests.Session()
s.headers['Content-Type'] = "Application/json"

# grafana endpoints
grafana_login_endpoint = 'http://grafana:3000/login'
grafana_datasource_endpoint = 'http://grafana:3000/api/datasources'
grafana_dashboard_endpoint = 'http://grafana:3000/api/dashboards/import'

# grafana payloads
grafana_login_payload = '{"user":"admin","email":"","password":"admin"}'
grafana_datasource_payload = '{"name":"influxdb","type":"influxdb","url":"http://influxdb:8086/","access":"proxy","jsonData":{},"isDefault":true,"database":"speedtest_metrics","user":"admin","password":"admin"}'
grafana_dashboard_payload_file = open('./dashboard.json','r')
grafana_dashboard_payload = grafana_dashboard_payload_file.read().strip()

# grafana login
login = s.post(url="http://grafana:3000/login", data=grafana_login_payload)
if login.status_code == 200:
    print "grafana --> login successful"

# load grafana datasource
datasource =  s.post(url="http://grafana:3000/api/datasources", data=grafana_datasource_payload)
if datasource.status_code == 200:
    print "grafana --> datasource import successful"
        
# load grafana dashboard
dashboard = s.post(url="http://grafana:3000/api/dashboards/import", data=grafana_dashboard_payload)
if dashboard.status_code == 200:
    print 'grafana --> dashboard import successful'
