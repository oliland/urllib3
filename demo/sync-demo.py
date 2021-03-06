# This should work on all versions of Python 2 and 3

from __future__ import print_function

import urllib3

URL = "http://httpbin.org/uuid"

print("--- urllib3 using synchronous sockets ---")
with urllib3.PoolManager() as http:
    print("URL:", URL)
    r = http.request("GET", URL, preload_content=False)
    print("Status:", r.status)
    print("Data: {!r}".format(r.data))
