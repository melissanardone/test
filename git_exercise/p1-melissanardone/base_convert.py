
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    num_list = ['A', 'B', 'C', 'D', 'E', 'F']

    if num//b != 0:
        if num % b < 10:
            return  convert(num // b, b) + str(num % b)
        else:
            return  convert(num // b, b) + num_list[(num % b)%10]
    else:
        if num % b < 10: #check to see if the number needs to be replaced with a letter
            return str(num % b)
        else:
            return num_list[(num % b)%10]