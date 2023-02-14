#13/02/2023
"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring( s: str) -> int:
    char_set = set()
    max_len, start = 0, 0
    for i, c in enumerate(s):
        while c in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(c)
        max_len = max(max_len, i - start + 1)
    return max_len




if __name__ == "__main__":
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring('abcabcbb')))
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring('bbbbb')))
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring('pwwkew'))) 
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring(" ")))
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring("c"))) 
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring("au"))) 
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring("aab")))
    print("\t El tamaño de la subcadena más grande es: "+str(lengthOfLongestSubstring("dvdf")))  