# first 8                         # last 8
l, r = 0, len(nums)               l, r = 0, len(nums)
while l < r:                      while l < r:
    m = l + (r - l) // 2              m = l + (r - l) // 2
    if nums[m] >= target:             if nums[m] > target:
        r = m                             r = m
    else:                             else:
        l = m + 1                         l = m + 1
return l                          return l - 1
