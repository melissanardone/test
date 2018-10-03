def perm_gen_lex(a): 
    """returns all possible combinations of the characters in a string in a list"""

    if a == '':
        return []
    elif len(a) == 1:
        return [a]
    else:
        perm_list = []
        """For each character in the input string"""
        for i in range(len(a)):

            """Form a simpler string by removing the character from the input string
            Generate all permutations of the simpler string recursively"""
            if i == len(a)-1:
                simple_string = a[:i]
            else:
                simple_string = a[:i] + a[(i+1):]

            simple_string_list = perm_gen_lex(simple_string)

            """Add the removed character to the front of each permutation of the simpler string, and
               add the resulting permutation to the list"""
            for val in simple_string_list:
                perm_list.append(a[i] + val)

        return perm_list 
