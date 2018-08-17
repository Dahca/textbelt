#! /usr/bin/env python3

import requests, sys

def main():
  addr = 'http://localhost:9090/text/'
  post = {'number': sys.argv[1], 'message': sys.argv[2]}
  res = requests.post(addr, post)
  print(res.content.decode('utf-8'))

if __name__ == '__main__':
  main()

