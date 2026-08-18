class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []

        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            objective = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]

                if curr == objective:
                    answer.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif curr > objective:
                    r -= 1
                else:
                    l += 1

            i += 1

        return answer