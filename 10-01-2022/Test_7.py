'''1. The program will recieve 3 English words inputs from STDIN

These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by *
The second word should be changed like all consonants should be replaced by @
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
Other than these concatenated word, no other characters/string should or message should be written to STDOUT

For example if you print how are you then output should be h*wa@eYOU.

You can assume that input of each word will not exceed more than 5 chars

Test Cases
Case 1
Input

how
are
you
Expected Output : h*wa@eYOU

Case 2
Input

how
999
you
Expected Output : h*w999YOU
'''

def word(ip1, ip2, ip3):
    vowels = ["a", "e", "i", "o" ,"u"]
    res = " "
    for letters in ip1:
        if letters in vowels:
            letters = "*"
        res += letters
    # print(res)
    if not str(ip2).isdigit():
        for letters in ip2:
            if letters not in vowels:
                letters = "@"
            res += letters
    else:
        res += str(ip2)
    # print(res)
    str3 = ip3.upper()
    res += str3
    print(res)






word("how",999,"you")
word("how","are","you")
