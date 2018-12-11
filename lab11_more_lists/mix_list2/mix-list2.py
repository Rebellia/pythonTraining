#!/usr/bin/env python3

protocols = ['ssh', 'http', 'https']
protocols2 = ['ssh', 'http', 'https']

print("protocols is: ", protocols)

print("The first item in protocols is: ", protocols[1])

protocols.extend('dns')

print("protocols after extending dns is: ", protocols)

protocols.append('dns')
protocols2.append('dns')

print("protocols after appending dns is: ", protocols)

proto3 = [ 22, 80, 443, 53]

#extend will put the individual list items inside of protocols
protocols.extend(proto3)

print("protocols after extending proto3 is: ", protocols)

#append will put the list itself as an individual list item
protocols2.append(proto3)

print("protocols2 after appending dns and proto3 is: ", protocols2)
