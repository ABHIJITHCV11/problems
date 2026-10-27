class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # Search over CAPACITIES, not the array.
        # Range: max(weights) = smallest capacity that can carry the heaviest package
        #                       (anything smaller → that package never fits)
        #        sum(weights) = ship everything in one day, always works
        #
        # capacity:  max ... ... ... sum
        #            T   T   F   F   F      go-right condition: days_needed(cap) > days (too small)
        # Monotonic: a bigger ship never needs MORE days → all T's, then all F's.
        # Answer = first F = the smallest capacity that ships in time.

        def days_needed(cap: int) -> int:
            # Greedy: load packages in order; if the next one doesn't fit,
            # ship today's load and start a new day with it.
            
            # Safe because cap >= max(weights): every package fits in an empty ship.
            day_count, load = 1, 0
            for w in weights:
                if load + w > cap:
                    day_count += 1
                    load = 0
                load += w
            return day_count

        l, r = max(weights), sum(weights)
        # max(weights) is the smallest capacity that can carry the heaviest package
        # sum(weights) ships everything in one day

        while l < r:
            m = l + (r - l) // 2
            if days_needed(m) > days:   # T: too small → go right
                l = m + 1
            else:                       # F: m works → answer is m or smaller, keep m
                r = m

        return l