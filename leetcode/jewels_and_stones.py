class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

        Letters are case sensitive, so "a" is considered a different type of stone from "A".

        Example 1:

        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
        Example 2:

        Input: jewels = "z", stones = "ZZ"
        Output: 0
        
        Constraints:

        1 <= jewels.length, stones.length <= 50
        jewels and stones consist of only English letters.
        All the characters of jewels are unique.
        """
        # Create a dictionary to keep track of jewels
        # increment the count for each jewel as we loop through the stones

        jewels_dict = {}
        count = 0

        for jewel in jewels:
            if jewel in jewels_dict:
                jewels_dict[jewel] += 1
            else:
                jewels_dict[jewel] = 1

        for stone in stones:
            if stone in jewels_dict:
                jewels_dict[stone] += 1
                count += 1

        return jewels_dict, count


if __name__ == "__main__":
    solution = Solution()
    print(solution.numJewelsInStones("aA", "aAAbbbb"))
    print(solution.numJewelsInStones("z", "ZZ"))
            