#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email:' argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    r = request.Request.post(argv[1], data)
    with request.urlopen(r) as re:
        print(r.read().decode('utf-8'))
