class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds = {}
        dt = {}
        for i in range(0, len(s)):
            sc = s[i]
            tc = t[i]
            if ds.has_key(sc):
                if tc != ds[sc]:
                    return False
                if dt.has_key(tc):
                    if sc != dt[tc]:
                        return False

        ds[sc] = tc
        dt[tc] = sc
        return True

