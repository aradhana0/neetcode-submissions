class Solution:
    def isPalindrome(self, s: str) -> bool:
        def stringCleanUp(s):
            cleanStr = ""
            for ch in s:
                if (ord(ch) >= ord("a")  and ord(ch) <= ord("z") ) or (ord(ch) >= ord("A")  and ord(ch) <= ord("Z")) or (ch >= "0" and ch <= "9"):
                    cleanStr += ch.lower()
            return cleanStr 

        def validatePalindrome(s):
            # print(len(s))
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True


        return validatePalindrome(stringCleanUp(s))