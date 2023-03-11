class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Given an array of integers nums, return the number of good pairs.

        A pair (i, j) is called good if nums[i] == nums[j] and i < j.

        Example 1:

        Input: nums = [1,2,3,1,1,3]
        Output: 4
        Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
        Example 2:

        Input: nums = [1,1,1,1]
        Output: 6
        Explanation: Each pair in the array are good.
        Example 3:

        Input: nums = [1,2,3]
        Output: 0
        

        Constraints:

        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        """
        
        output = 0
        dict_number = dict()
        for n in nums:
            if n in dict_number:
                output += dict_number[n]
                dict_number[n] += 1
            else:
                dict_number[n] = 1
        return output





if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1,1,3]
    print(solution.numIdenticalPairs(nums))