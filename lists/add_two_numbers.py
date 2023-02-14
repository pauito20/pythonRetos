#12/02/22
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional, List


def addTwoNumbers(l1: Optional[List], l2: Optional[List]) -> Optional[List]:
    res = []
    num1 = ''
    num2 = ''

    for i in range(0, len(l1)):
        num1 += str(l1[i])
    for i in range(0, len(l2)):
        num2 += str(l2[i]) 
        
    num_res = str(int(num1)+int(num2))
    for e in reversed(num_res):
        res.append(int(e))
    return res




if __name__ == "__main__":
    l1_1 = [2,4,3]
    l2_1 = [5,6,4]
    print(addTwoNumbers(l1_1, l2_1))

    l1_2= [0]
    l2_2 = [0]
    print(addTwoNumbers(l1_2, l2_2))


    l1_3 = [9,9,9,9,9,9,9]
    l2_3 = [9,9,9,9]
    print(addTwoNumbers(l1_3, l2_3))




