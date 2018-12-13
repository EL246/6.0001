# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: 1:25

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # if sequence has one character, return that character
    if len(sequence)<2:
        return sequence
    perms = []
    # get permutations of sequence minus first character
    prev_seq = get_permutations(sequence[1:len(sequence)])
    # add first character in sequence into permutations
    for p in prev_seq:
        #print("p:", p)
        for l in range(len(p)):
        #for l in range(len(sequence)):
            #new_perm = list(p)
            #new_perm.insert(l,sequence[0])
            #new_perm = "".join(new_perm)
            new_perm = p[:l]+sequence[0]+p[l:]
            #print("p[:l]", p[:l])
            #print("sequence[0]", sequence[0])
            #print("p[l+1:]", p[l+1:])
            #print("new_perm", new_perm)
            # if permutation already exists, do not add to list
            if new_perm not in perms:
                perms.append(new_perm)
    return perms


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    exp_out = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    act_out = get_permutations(example_input)
    print('Actual Output:', get_permutations(example_input))
    if any(perm in exp_out for perm in act_out):
        print("SUCCESS!!!!!")
    else: print("FAILURE!!!")


#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

#   test 1
    print("TEST 1")
    example_input= "pea"
    print("Input:", example_input)
    exp_out = ["pea", "pae", "eap", "epa", "ape", "aep"]
    print('Expected Output:', exp_out)
    act_out = get_permutations(example_input)
    print('Actual Output:', get_permutations(example_input))
    if any(perm in exp_out for perm in act_out):
        print("SUCCESS!!!!!")
    else: print("FAILURE!!!")
    
    #   test 2
    print("TEST 2")
    example_input= ""
    print("Input:", example_input)
    exp_out = ""
    print('Expected Output:', exp_out)
    act_out = get_permutations(example_input)
    print('Actual Output:', get_permutations(example_input))
    if exp_out == act_out:
        print("SUCCESS!!!!!")
    else: print("FAILURE!!!")
    
    #   test 3
    print("TEST 3")
    example_input= "eee"
    print("Input:", example_input)
    exp_out = ["eee"]
    print('Expected Output:', exp_out)
    act_out = get_permutations(example_input)
    print('Actual Output:', get_permutations(example_input))
    if any(perm in exp_out for perm in act_out):
        print("SUCCESS!!!!!")
    else: print("FAILURE!!!")
