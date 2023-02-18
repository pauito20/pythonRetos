"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)
    
    while low < high:
        mid = low + (high - low)//2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low
    


if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 5))
    print(searchInsert([1,3,5,6], 2))
    print(searchInsert([1,3,5,6], 7))
    print(searchInsert([1,3,5,6], 0)) 
    print(searchInsert([1,3], 2))