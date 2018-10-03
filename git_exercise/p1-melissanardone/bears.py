def bears(n):
    """returns the result to the teddy bear 
    game and if 42 is reachable or not"""

    #base case
    if n == 42:
        return True
    elif n < 42:
        return False
   
    state = False
    if n % 5 == 0:
        state = bears(n - 42)
        if state:
            return state

    if (n % 3 == 0) or (n % 4 == 0):
        digit1 = n % 10
        digit2 = (n % 100)//10
        if digit1 != 0 and digit2 != 0:
            state = bears(n - (digit1 * digit2))
            if state:
                return state

    if n % 2 == 0:
        state = bears(n/2)
        if state:
            return state

    return state

