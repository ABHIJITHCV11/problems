class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frq = {}
        l,r = 0,0
        max_len = 0
        max_frq = 0

        while r < len(s):
            frq[s[r]] = frq.get(s[r],0) + 1
            # r-l+1 - max(frq.value()) <= k: # then the window is valid
            max_frq = max(frq[s[r]],max_frq)

            while r-l+1 - max_frq > k: # invalid
                frq[s[l]] = frq[s[l]] - 1
                l+=1

            cur_len = r-l+1
            max_len = max(cur_len,max_len)
            r+=1

        return max_len

        # AACBCBBB
        # k=1

        # A       1-1 > 1 ? F -->r+1
        # AA      2-2 > 1 ? F -->r+1
        # AAC     3-2 > 1 ? F -->r+1
        # AACB    4-2 > 1 ? T -->l+1 (not valid will enter while loop)
        # ACB     3-2 > 1 ? F -->r+1 window not valid here ! but formula allows it | as max_frq is not updated
        # CB      2-2 > 1 ? F -->r+1
        # CBB     3-2 > 1 ? F -->r+1
        # CBBB    4-3 > 1 ? F -->r+1
        # Loop ends
