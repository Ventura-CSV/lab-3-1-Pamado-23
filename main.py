def main():
    ##################################################
    # Comlete your code here
    ##################################################
    number = int(input('Enter your input: '))

    """
    Make your code here
    """
    
    # If the number is less than 50, set the variable range to 1

    if number < 50:
        range = 1 

    # If the number is greater than or equal to 50 and less than 100, set the variable range to 2

    elif 50 <= number < 100:
        range = 2

    # If the number is greater than or equal to 100, set the variable range to 3

    else:
        range = 3



    print(f'Range is {range}')
    ########################################
    # Do not delete the return statement
    ########################################
    return range


if __name__ == '__main__':
    main()
