"""
Assignment Five: Recursion Lab
Submitted by Clara Manolache
Submitted: May 11, 2026

This program is to practice list comprehensions, slicing, concatenation, and basic recursion. We will reverse the
direction of alphabet list in the reverse_a_list() function to practice these skills. Not part of long term project.
"""
def reverse_a_list(my_list):
    """ reverse the order of my_list """
    length = len(my_list)
    print(f"The length of my_list is now: {length}")
    if len(my_list) == 1: # checking for base case
        return my_list
    ret_value = my_list.copy() # copy to prevent alterations to the original list
    elem = ret_value.pop(0)  # Removing the first element, will be added back after all later letters added
    ret_value = reverse_a_list(ret_value)  # recursive call
    ret_value.append(elem)  # adding back letter after recursive chain finished
    return ret_value

def main():
    """
    Performs the unit-tests provided by profesor
    """
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()

'''
Sample Run
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/Week 5/lab_assigment#5.py 
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
The length of my_list is now: 26
The length of my_list is now: 25
The length of my_list is now: 24
The length of my_list is now: 23
The length of my_list is now: 22
The length of my_list is now: 21
The length of my_list is now: 20
The length of my_list is now: 19
The length of my_list is now: 18
The length of my_list is now: 17
The length of my_list is now: 16
The length of my_list is now: 15
The length of my_list is now: 14
The length of my_list is now: 13
The length of my_list is now: 12
The length of my_list is now: 11
The length of my_list is now: 10
The length of my_list is now: 9
The length of my_list is now: 8
The length of my_list is now: 7
The length of my_list is now: 6
The length of my_list is now: 5
The length of my_list is now: 4
The length of my_list is now: 3
The length of my_list is now: 2
The length of my_list is now: 1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Process finished with exit code 0
'''
