#!/usr/bin/python3
"""
A scripts that takes in a URL and sends a request to the URL
then displays the value of the X-Request_Id variable found in
the header of the response
"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
