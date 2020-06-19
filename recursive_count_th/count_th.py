'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    print(f"word before: {word}")

    instances = 0

    if len(word) == 1:
        return 0
    if len(word) > 2:
        instances = count_th(word[1:])
    print(f"word after: {word}")
    if word[0:2] == "th":
        print("found it")
        instances += 1
    return instances

    
    
