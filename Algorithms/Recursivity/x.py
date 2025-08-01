#  Describe a recursive algorithm for finding the maximum element in a se
# quence, S,ofn elements. What is your running time and space usage?

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(5))