def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celcius = int(input("What is the temperature in Celcius? "))

    fahrenheit = ((9/5)*celcius) + 32 

    print("The temperature in Celcius is " +str(celcius))
    print(f"The tempature in Fahrenheit is {fahrenheit:.2f}")

    return celcius, fahrenheit


if __name__ == '__main__':
    main()
