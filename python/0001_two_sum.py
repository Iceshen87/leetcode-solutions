from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # [1, 2]
    print(sol.twoSum([3, 3], 6))          # [0, 1]