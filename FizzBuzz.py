"""FizzBuzz"""
#Rules:
# Display 1-20
# 'Fizz' on multiples of 3
# 'Buzz' on multiples of 5
# 'FizzBuzz' on multiples of both
# Bonus Challenge - Least number of lines possible

def ismultiple(num,mod):
    return num % mod

output = ''
for i in range(1,16):
    if ismultiple(i,3) and not ismultiple(i,5):
    
    elif not ismultiple(i,3):
        output = 'Fizz'
    elif not ismultiple(i,5):
        output = 'Buzz'
    else:
        output += str(i)
    print(output)
    output = ''

"""
FizzBuzz in 1 line
for i in range(1,16):
    print('Fizz'*(not i%3) + 'Buzz'*(not i%5) or i)
"""