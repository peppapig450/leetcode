class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input list to use the two-pointer technique
        nums.sort()
        n = len(nums)

        # Initialize closest_sum to the sum of the first three numbers
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through each number in the list as a potential first number
        for i in range(n - 2):
            # Initialize two pointers for the remaining numbers
            low, high = i + 1, n - 1

            # Two-point approach to find the closet sum for the current first number
            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]
                diff = abs(current_sum - target)

                # If the current sum is exactly the target, return it immediately
                if diff == 0:
                    return current_sum

                # Update the closet sum if the current difference is smaller
                if diff < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust the pointers based on the comparison with the target
                if current_sum < target:
                    low += 1
                else:
                    high -= 1
        
        return closest_sum