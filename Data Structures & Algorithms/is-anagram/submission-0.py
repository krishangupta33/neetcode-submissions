class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            counts1=[0]*26
            counts2=[0]*26

            for i,j in zip(s,t):
                counts1[ord(i)-ord('a')] +=1
                counts2[ord(j)-ord('a')] +=1
            
            if counts1==counts2:
                return True

            else:
                return False

        else:
            return False
