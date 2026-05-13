"""
Recursion
Student Name: Jackson Lieberman
Date: 5/13
Description: 
Run the following functions through recursion
 1.  Factorial
 2.  Summation 
 3.  Exponential 
 4.  Fibonacci
 5.  Sum of digits
 6.  Product of digits
 7.  Product of ints 
 8.  Sum of range 
 9.  Reverse digits
 10. Euclid GCD
 11. Compound interest
Bonuses:
Bugs: 
Log: 1.1
"""


def factorial (n):
    """
    Description: Calculate the factorial of n
    Parameters: 
        n(int):the number to calculate the factorial of
    returns: 
        int: the factorial of n
    """
    if n == 0:
        return 1
    return n * factorial(n-1)                       

def summation (n):
    """
    Description: Calculate the summation of n
    Parameters: 
        n(int):the number to calculate the summation of
    returns: 
        int: the summation of n
    """
    if n == 0:
        return 0
    return n + summation(n-1)

def exponential (a,n):
    """
    Description: Calculate the exponential of n
    Parameters: 
        n(int):the number in the exponential 
        a(int):the base of the exponential
    returns: 
        int: the exponental of n
    """
    if n == 0:
        return 1
    return a*exponential(a, n-1)

def fibonacci (n):
    """
    Description: Calculate the fibonacci of n
    Parameters: 
        n(int):the number to calculate the fibonacci of
    returns: 
        int: the fibonacci of n
    """
    if n <= 0:                              #if n is less or equal to zero because we need to check multiple possible occurences
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  

def sum_of_digits (n):
    """
    Description: Calculate the sum of the digits of n
    Parameters: 
        n(int):the number to calculate the the sum of the digits of
    returns: 
        int: the sum of the digits of n
    """
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)            #splits into digits (remander when dividing by ten is last digit)


def product_of_digits (n):
    """
    Description: Calculate the product of the digits of n
    Parameters: 
        n(int):the number to calculate the the product of the digits of
    returns: 
        int: the product of the digits of n
    """
    if n == 0:
        return 1
    return (n % 10) * product_of_digits(n // 10)            


def product_of_ints (n,a):
    """
    Description: Calculate the product of two whole numbers
    Parameters: 
        n(int):the 2nd number to calculate the product of two whole numbers
        a(int):the 1st number to calculate the product of 
    returns: 
        int:  the product of two whole numbers a and n
    """
    if n == 0:
        return 0
    return a + product_of_ints(n-1, a)              


def sum_of_range (a,n):
    """
    Description: sum of numbers in a range (a-n)
    Parameters: 
        a(int): starting number in range to calculate the sum of numbers in a range
        n(int): final number in range to calculate the sum of numbers in a range
    returns: 
        int: the sum of numbers in a range (a-n)
    """
    if n < a:                                   #until n is less than a
        return 0        
    return sum_of_range(a, n-1) + n            

def reverse_digits (a):
    """
    Description: reverse the digits of a number
    Parameters: 
        a(int): the number to reverse the digits of
    returns: 
        int: the number with its digits reversed
    """
    if a == 0:
        return 0
    return (a % 10) * (10 ** (len(str(a)) - 1)) + reverse_digits(a // 10)          #takes the last digit and then shifts it, then the next

def euclid_GCD (a, b):
    """
    Description: find the GCD of a number
    Parameters: 
        a(int): the number to find the GCD of
        b (int): second number to find GCD of
    returns: 
        int: the GCD
    """
    if b == 0:
        return a
    return euclid_GCD(b, a % b)         

def compound_interest(a, r, n):
    """
    Description: Calculate a compound interest balance after n periods
    Parameters:
        a (float): the initial principal balance
        r (float): the interest rate per period (as a decimal, e.g. 0.05 for 5%)
        n (int): the number of compounding periods
    Returns:
        float: the balance after n periods of compounding
    """
    if n == 0:
        return a
    return compound_interest(a * (1 + r), r, n - 1)


def main():


    menu = """
Recursion Menu
 1.  Factorial
 2.  Summation 
 3.  Exponential 
 4.  Fibonacci
 5.  Sum of digits
 6.  Product of digits
 7.  Product of ints 
 8.  Sum of range 
 9.  Reverse digits
 10. Euclid GCD
 11. Compound interest
 0.  Quit
"""
 
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        
        try:
            if choice == "0":
                print("Goodbye.")
                break
            elif choice == "1":
                n = int(input("n: "))
                print(f"factorial({n}) = {factorial(n)}")
            elif choice == "2":
                n = int(input("n: "))
                print(f"summation({n}) = {summation(n)}")
            elif choice == "3":
                a = int(input("base a: "))
                n = int(input("exponent n: "))
                print(f"exponential({a}, {n}) = {exponential(a, n)}")
            elif choice == "4":
                n = int(input("n: "))
                print(f"fibonacci({n}) = {fibonacci(n)}")
            elif choice == "5":
                n = int(input("n: "))
                print(f"sum_of_digits({n}) = {sum_of_digits(n)}")
            elif choice == "6":
                n = int(input("n: "))
                print(f"product_of_digits({n}) = {product_of_digits(n)}")
            elif choice == "7":
                n = int(input("multiplier n: "))
                a = int(input("value a: "))
                print(f"product_of_ints({n}, {a}) = {product_of_ints(n, a)}")
            elif choice == "8":
                a = int(input("start a: "))
                n = int(input("end n: "))
                print(f"sum_of_range({a}, {n}) = {sum_of_range(a, n)}")
            elif choice == "9":
                a = int(input("number: "))
                print(f"reverse_digits({a}) = {reverse_digits(a)}")
            elif choice == "10":
                a = int(input("a: "))
                b = int(input("b: "))
                print(f"euclid_GCD({a}, {b}) = {euclid_GCD(a, b)}")
            elif choice == "11":
                a = float(input("principal: "))
                r = float(input("rate (decimal, e.g. 0.05): "))
                n = int(input("periods: "))
                print(f"compound_interest({a}, {r}, {n}) = {compound_interest(a, r, n):.2f}")
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid input. Numbers only.")


if __name__== "__main__":
    main()



