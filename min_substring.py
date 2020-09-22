# Min Substring
# Have the function min_substring(str_lst) take the list of strings stored in str_lst, 
# which will contain only two strings, the first parameter being the container_string and the 
# second parameter being the inside_string of some characters.

# Your goal is to determine the smallest substring of the container_string that 
# contains all the characters in the inside_string. 
# Both strings will only contains lowercase alphabetic characters.

# For example: if str_lst is ["aaabaaddae", "aed"] then the smallest substring of container_string that 
# contains the characters a, e, and d is "dae" located at the end of the string. 
# So for this example your program should return the string "dae".


# Examples
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse

def min_substring(str_lst):
    # code goes here
    return

print(min_substring(["aaffhkksemckelloe", "fhea"]))
# should print fhea

print(min_substring(["ahffaksfajeeubsne", "jefaa"]))
# should print fhea

print(min_substring(["aaabaaddae", "aed"]))
# should print dae

