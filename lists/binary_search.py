"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    mid = len(nums)//2
    end = len(nums)-1
   
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binary_search(nums, 0, mid-1, target)
    else:
        
        return binary_search(nums, mid+1, end, target)


def binary_search(arr, low, high, x) -> int:
    if high >= low:
        mid = (high+low)//2 
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:

            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1





if __name__ == "__main__":
    print("Búsqueda binaria de "+str([-1,0,3,5,9,12])+" y el target "+str(9)+" es: "+str(search([-1,0,3,5,9,12], 9)) )
    print("Búsqueda binaria de "+str([-1,0,3,5,9,12])+" y el target "+str(2)+" es: "+str(search([-1,0,3,5,9,12], 2)) )
