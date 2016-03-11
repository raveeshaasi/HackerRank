#Program that prints Fizz which is divisible by 3, Buzz which is divisible by 5 and by both of them then FizzBuzz
#HackerRank - https://www.hackerrank.com/challenges/fizzbuzz

for i in range(1,101):
    if i%15==0:
        print 'FizzBuzz'
    elif i%5==0:
        print 'Buzz'
    elif i%3==0:
        print 'Fizz'
    else:
        print i
