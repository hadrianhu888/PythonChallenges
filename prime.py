def check_prime(n):
    """Checks if a number is a prime or not"""
    flag = False
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                flag = True
                break            
    if flag:
        print(n, " is not a prime number.\n")
    else:
        print(n, " is a prime number.\n")
        
def main():        
    check_prime(2)
    for i in range(2,100):
        check_prime(i)
        
if __name__ == "__main__":
    main()