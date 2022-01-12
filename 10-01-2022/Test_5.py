''''
https://prepinsta.com/tcs-coding-question-4/
break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var

Write a program to find if the given word is a keyword or not

Test cases
Case 1
Input – defer
Expected Output – defer is a keyword
Case 2
Input – While
Expected Output – while is not a keyword
'''

def matching(word):
    all_words = ["break", "case", "continue", "default", "defer", "else", "for", "func", "goto", "if", "map", "range", "return", "struct", "type", "var"]
    # pass
    
    if word in all_words:
        print(f"{word} is a keyword")
    else:
        print(f"{word} is not a keyword")  





matching("defer")
matching("while")