class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        rem = []
        r = 0
        index = 0

        while r<len(arr2) and arr2[r] in arr1:
        
            res+=[arr2[r]]*arr1.count(arr2[r])
            
            r+=1

        
        for each in arr1:
            if each not in arr2:
                rem.append(each)
            

        res+=sorted(rem)
        return res

