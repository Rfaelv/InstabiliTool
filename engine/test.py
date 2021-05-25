import sys, json

input1 = sys.stdin.readlines()
value = json.loads(input1[0])

input2 = sys.stdin.readlines()
value2 = json.loads(input2[0])

print(value + value2)