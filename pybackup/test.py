class Solution:
    def twoSum(self, nums, target):
        test = {}

        for i in range(len(nums)):
            if nums[i] not in test:
                test[nums[i]] = [i]
            else:
                test[nums[i]].append(i)
        for key in test:
            diff = target - key
            if diff in test:
                return test[diff]
                

        #return test
sol = Solution()
print(sol.twoSum([2,5,5,11],10))


