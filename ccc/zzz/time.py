import time

print('Please type seconds:')
l = int(input())

while l > 0:
  print('   There are %d seconds left' % (l))
  time.sleep(1)
  l = l - 1