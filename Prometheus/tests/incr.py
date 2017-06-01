#!/usr/bin/env python

from prometheus_client import start_http_server, Counter
import time


def process_inc(t = 1):
    c.inc(t)
    time.sleep(t)


if __name__ == '__main__':
    start_http_server(8000)
    c = Counter('so_far', 'counting signs of life')

    while True:
      process_inc()
