#!/usr/bin/env python
import os
import time
import requests

host, port = os.environ.get('PROMETHEUS_SERVICE_HOST'), os.environ.get('PROMETHEUS_SERVICE_PORT')

timeout = 5
while True:
  try:
    r = requests.get("http://{}:{}".format(host, port), timeout=timeout)
    print(r.ok)
    print(r.content)
  except requests.exceptions.Timeout:
    print ("Timed out")

  time.sleep(timeout)
