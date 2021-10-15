# Get list using range and xrange functions

primes = [1,3,5,7]
for prime in primes:
  print(prime)

print('Using Range')  
for x in range(5):
  print(x)
print('Using Range 1,10,5')  
for x in range(1,10,5):
  print(x)

print('Using break and continue')
count = 0
while(count < 5):
  print(count)
  count+=1
else:
  print('Loop ended')