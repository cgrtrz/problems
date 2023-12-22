def factorial(x):
    result=1
    for number in range(2, x+1):
        result*=number
    return result

print(factorial(5))