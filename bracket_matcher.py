# Write a Python function that takes a string input. This string represents code. 
# It may have any number of characters in it, and the characters may be anything. 
# For our purposes, we'll ignore anything that isn't one of the following: [, ], {, }, (, ). 
# Your function definition looks like this:

# def bracket_matcher(input):
# The return value is a boolean. You should return True if the brackets are properly matched and nested, 
# otherwise False.

# Test Cases:
# Think you got it figured out? Run through the test cases below to make sure!


def bracket_matcher(str):
  # code goes here
  return 



print(bracket_matcher('abc(123)'))
# returns true

print(bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print(bracket_matcher('a[bc(123)]'))
# returns true

print(bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print(bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print(bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print(bracket_matcher('()'))
# returns true

print(bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print(bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched