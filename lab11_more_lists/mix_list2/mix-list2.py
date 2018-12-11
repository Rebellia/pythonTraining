#!/usr/bin/env python3

protocols = ['ssh', 'http', 'https']
protocols2 = ['ssh', 'http', 'https']


print(protocols)

protocols.append('dns')
protocols2.append('dns')

print(protocols)

proto3 = [ 22, 80, 443, 53]

protocols.extend(proto3)

print(protocols)

protocols2.append(proto3)

print(protocols2)
