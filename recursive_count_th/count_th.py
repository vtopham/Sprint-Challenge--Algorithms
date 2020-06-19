'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    instances = 0
    #when we cut down the string to just one character, return 0 since there's no possible "th" in that
    if len(word) == 1:
        return 0
    #if it's more than 2 characters long then we'll want to cut it down until we get to the last two characters so we can start from the end and pass up the number of occurrances of "th"
    if len(word) > 2:
        instances = count_th(word[1:])
    #now that we're moving backwards from the end of the array, check to see if we have a "th"
    if word[0:2] == "th": 
        instances += 1
    #return up the number of instances so far
    return instances

    
    
