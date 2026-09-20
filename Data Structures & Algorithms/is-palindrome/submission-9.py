class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValidChar(ch):
            return ch.isalnum()
            # if (ord(ch) >= ord("a")  and ord(ch) <= ord("z") ) or (ord(ch) >= ord("A")  and ord(ch) <= ord("Z")) or (ord(ch) >= ord("0") and ord(ch) <= ord("9")):
            #     return True
            # return False
  
        i = 0
        j = len(s) - 1

        while j > i:
            while i < j and not isValidChar(s[i]):
                i += 1
            while i < j and not isValidChar(s[j]):
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True