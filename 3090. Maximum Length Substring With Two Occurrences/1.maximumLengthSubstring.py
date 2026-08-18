class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Brute force: for every window [i, j], re-scan with a 3rd pointer k
        to count occurrences. O(n^3).
        """
        curr_max = 0
        for i in range(len(s)):
            s1 = 0
            for j in range(i + 1, len(s)):
                k = i
                d1 = {}
                while k <= j:
                    if s[k] not in d1:
                        d1[s[k]] = 1
                        curr_max = max(curr_max, k - i + 1)
                    elif d1[s[k]] == 1:
                        d1[s[k]] += 1
                        curr_max = max(curr_max, k - i + 1)
                    else:
                        s1 = 1
                        d1[s[k]] += 1
                        break
                    k += 1
                if s1 == 1:
                    break
        return curr_max
