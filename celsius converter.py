celsius = int(input())

def conv(c):
    c=celsius * 9 / 5 + 32
    return c

fahrenheit = conv(celsius)
print(fahrenheit)