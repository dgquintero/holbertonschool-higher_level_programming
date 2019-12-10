#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str[39:-13] + str[:6]
str = str[:28] + str[68:73] + str[-6:]
print(str)
