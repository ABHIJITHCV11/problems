class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Search over SPEEDS, not the array.
        # Range: 1 = slowest possible speed
        #        max(piles) = always works: every pile takes 1 hour, n hours total, and h >= n
        #        (any speed above max(piles) is still 1 hour per pile → no point searching higher)
        #
        # speeds:  1  2  3  4  5 ...  max
        #          T  T  T  F  F ...  F      go-right condition: hours(speed) > h (too slow)
        # Monotonic: a faster speed never takes MORE hours → all T's, then all F's.
        # Answer = first F = the minimum speed that finishes in time.

        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2

            hours = 0
            for pile in piles:
                # hours += (pile + m - 1) // m   # integer ceil(pile / m)
                hours = hours + math.ceil(pile/m)

            if hours > h:      # T: too slow, so m and everything below fails → go right
                l = m + 1 # koko should increase the eating speed
            else:              # F: m works → answer is m or a smaller speed, keep m
                r = m     # koko is atleast at the optimal speed or there is a speed below it where koko can eat 

        return l