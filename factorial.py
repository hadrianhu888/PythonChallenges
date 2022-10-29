import math
def factorial(n):
    if n == 0 or n == 1:
        fact = 1             
    else:               
        fact = n * factorial(n - 1)         
    return fact           

def main():
    for i in range(1,10):
        print(factorial(i))        

if __name__ == "__main__":
    main()

