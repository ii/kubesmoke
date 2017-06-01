#!/usr/bin/env python
import time
import requests

timeout = 5
while True:

  try:
    r = requests.get("http://172.0.0.1:8000", timeout=timeout)
    print(r.ok)
    print(r.content)
  except requests.exceptions.Timeout:
    print ("Timed out")

  time.sleep(timeout)
