class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        total = 0

        for word in words:
            total+=len(word)
            for c in word:
                if c in freq:
                    freq[c]+=1
                else:
                    freq[c]=1


        if total%len(words)!=0:
            return False

        if all(v%len(words)==0 for v in freq.values()):
            return True
        else:
            return False



