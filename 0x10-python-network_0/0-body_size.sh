#!/bin/bash
# sends a GET request to the URL, and displays the size body of the response
$ curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
