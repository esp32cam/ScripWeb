# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         count = 0
        

#         for i in range(len(x) // 2):
#             if x[i] == x[len(x) - i - 1]:
#                 count += 1
#             else:
#                 count -= 1

        
#         if count == len(x) // 2:
#             print('True')
#             return True
#         else:
#             print('False')
#             return False
# Solution.isPalindrome(Solution, 11234567899876543211)


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        pre_value = 0
        for char in s:
            value = symbol[char]
            if pre_value < value:
                count += value - 2 * pre_value
Solution.romanToInt(Solution, 'MCMXCIV')
