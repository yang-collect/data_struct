# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from collections import defaultdict
        res={}

        for s in strs:
            alpha_s=str(sorted(s))
            if alpha_s in res:
                res[alpha_s].append(s)
            else:
                res[alpha_s]=[s]
        
        return list(res.values())
        
