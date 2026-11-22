class Solution:
    def isPalindrome(self, x: int) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)
        # x = str(x)
        # return x == x[::-1]

        # time complexity: O(n)
        # space complexity: O(1)
        if x < 0:
            return False
        elif x != 0 and x%10 == 0:
            return False
        elif x/10 < 1:
            return True
        else:
            rev_to_forward = 0
            while rev_to_forward < x:
                d = x%10
                rev_to_forward = rev_to_forward * 10 + d
                x = x//10
            return x == rev_to_forward or rev_to_forward//10 == x
