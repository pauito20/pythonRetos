#14/02/2023
"""
Given two arrays nums1 and nums2 of size m and n respectively, 
return the median of the two  arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from heapq import merge
from typing import List

def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    """
    1. Fusionar "Merge" entre los dos arrays dado de forma ordenada
    2. Si es impar el array resultante, el resultado es el valor de la mitad de su longitud (centro), por otro lado, si
       es par el array, el resultado es la media de los dos valores centrales (a+b)/2
    """
    
    arr = nums1+nums2
    arr = mergeSort(arr)
    print("El vector ordenado es: "+str(arr))
    if len(arr)%2 != 0: 
        return arr[len(arr)//2]
    else:
        return ((arr[(len(arr)//2)-1] + arr[(len(arr)//2)]) / 2)

       


# Función merge_sort
def mergeSort(lista):
 
   """
   Lo primero que se ve en el psudocódigo es un if que
   comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
   ¿Por que? Ya esta ordenada. 
   """
   if len(lista) < 2:
      return lista
    
    # De lo contrario, se divide en 2
   else:
        middle = len(lista) // 2
        right = mergeSort(lista[:middle])
        left = mergeSort(lista[middle:])
        return merge(right, left)
    
# Función merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
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
    print(findMedianSortedArrays([1,3], [2]))
    print(findMedianSortedArrays([1,3,0], [2,5,-2]))
    print(findMedianSortedArrays([1,3,-1,-5], [2,6,2,3]))
    print(findMedianSortedArrays([1,3,5,7], [2,4,6]))