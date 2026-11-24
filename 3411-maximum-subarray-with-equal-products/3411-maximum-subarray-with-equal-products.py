import math

class Solution:
    def maxLength(self, nums):
        n = len(nums)
        max_length = 0

        for left in range(n):
            product = 1
            g = 0
            l = 1

            for right in range(left, n):
                x = nums[right]

                product *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)

                if product == l * g:
                    max_length = max(max_length, right - left + 1)

        return max_length