class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res={}
        for i in strs:
            key=" ".join(sorted(i))
            if key  not in res:
                res[key]=[]
            res[key].append(i)
        return list(res.values())
