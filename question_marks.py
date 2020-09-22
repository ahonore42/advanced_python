# Have the function question_marks(stri) take the stri string parameter, which will contain 
# single digit numbers, letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers that add up to 10. 

# If so, then your function should return True, otherwise it should return False. 
# If there aren't any two numbers that add up to 10 in the string, then your function should return false as well.

# For example: if stri is "arrb6???4xxbl5???eee5" then your function should return True because there are 
# exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

# Input: "aa6?9"          Input: "acc?7??sss?3rr1??????5"
# Output: False           Output: True

# Test your function with the test cases below!

def question_marks(stri):
    # code goes here
    return

print(question_marks('aa6?9'))
# should return False

print(question_marks('acc?7??sss?3rr1??????5'))
# should return True

print(question_marks('arrb6???4xxbl5???eee5'))
# should return True

print(question_marks('fal291?se4?rep?u?6kd5??2g9??asdg?1'))
# should return False

print(question_marks('fal21?se4?rep?u?6kd5??2g9??asdg?1al'))
# should return True

print(question_marks('5??aaaaaaaaaaaaaaaaaaa?5?5'))
# should return False

print(question_marks('9???1???9???1???9'))
# should return True
