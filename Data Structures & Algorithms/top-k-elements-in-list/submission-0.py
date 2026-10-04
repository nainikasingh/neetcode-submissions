class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count the frequency of each element in nums
        count = {}
        # List of empty lists to store numbers by their frequency
        frequency = [[] for _ in range(len(nums) + 1)]

        # Count the frequency of each number in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Place the numbers into the frequency list based on their count
        for num, freq in count.items():
            frequency[freq].append(num)

        # Result list to store the k most frequent elements
        result = []

        # Iterate over the frequency list from high to low frequency
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                # If we have found k elements, return the result
                if len(result) == k:
                    return result
