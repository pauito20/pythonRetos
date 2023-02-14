#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#12/02/22
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

if __name__ == "__main__":
    #Pruebas
    nums1 = [2,7,11,15]
    target1 = 9
    print("Prueba 1: " + str(twoSum(nums1, target1)))

    nums2 = [3,2,4]
    target2 = 6
    print("Prueba 2: " + str(twoSum(nums2, target2)))

    


