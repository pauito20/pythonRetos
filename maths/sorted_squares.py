"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
        """
        Usando sorted:
        
        def sortedSquares(self, nums: List[int]) -> List[int]:
            return sorted([x*x for x in nums])
        """
        #Calculamos los cuadrados de los elementos del vector
        for i in range(0, len(nums)):
            nums[i] = nums[i]*nums[i]
        nums = mergeSort(nums)
        return nums

def mergeSort(nums: List[int]) -> List[int]:  
        if len(nums) < 2:
            return nums
        else:
            middle = len(nums) // 2
            right = mergeSort(nums[:middle])
            left = mergeSort(nums[middle:])
            return merge(right, left)
        
def merge(lista1: List[int], lista2: List[int]) -> List[int]:
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado
 
        # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1
        
        # Agregamos los resultados a la lista
        result += lista1[i:]
        result += lista2[j:]
        
        # Retornamos el resultados
        return result





if __name__ == "__main__":
    print(sortedSquares([-7,-3,2,3,11]))
    print(sortedSquares([-4,-1,0,3,10]))