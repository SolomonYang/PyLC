from builtins import str

class solution:
   def wordBreak(self, s, wordDict) -> bool:
      if not s:
         return True
      
      if not wordDict:
         return False
      
      dp = [True] + [False] * len(s)
      
      minL = min(map(len, wordDict))
      maxL = max(map(len, wordDict))
      
      for i in range(len(s) - minL + 1):
         for j in range(minL, maxL + 1):
            if dp[i] and s[i:i+j] in wordDict:
               dp[i + j] = True
               break
      
      return dp[len(s)]

print(solution().wordBreak('aaaaaaa', ['aaaa', 'aaa']))