class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if curr in complements:
                return [complements[curr], i]
            else:
                complements[complement] = i


    def bruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

