import json
from django.test import TestCase


data = ["{\"slot\":\"1\",\"player\":\"1\",\"pos\":\"CF\"}","{\"slot\":\"2\",\"player\":\"2\",\"pos\":\"RF\"}","{\"slot\":\"3\",\"player\":\"3\",\"pos\":\"1B\"}","{\"slot\":\"4\",\"player\":\"4\",\"pos\":\"DH\"}","{\"slot\":\"5\",\"player\":\"5\",\"pos\":\"SS\"}","{\"slot\":\"6\",\"player\":\"6\",\"pos\":\"2B\"}","{\"slot\":\"7\",\"player\":\"7\",\"pos\":\"LF\"}","{\"slot\":\"8\",\"player\":\"8\",\"pos\":\"3B\"}","{\"slot\":\"9\",\"player\":\"9\",\"pos\":\"C\"}"]

print(data)
data_dicts = []
for record in data:
    print(record)
    data_dicts.append(json.loads(record))

print(data_dicts)


'''
x = junk[0]

y = json.loads(x)

print(x)
print("is a " + str(type(x)))
print(y)
print("is a " + str(type(y)))

'''


