class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use the two-pointer technique
        nums.sort()
        triplets = []

        # Iterate through the array, considering each element as a potential first element of a triplet
        for i in range(len(nums) - 2):
            # If the current value is the same as the previous one, skip it to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
        
            # Use the two-pointer technique to find the remaining two elements of the triplet
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1  # We need a larger sum, move the left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, move the right pointer to the left
    
        return triplets
