class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        
        string = ""
        for c in s:
            if c in valid:
                string += c.lower()

        l = 0
        r = len(string) - 1

        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True