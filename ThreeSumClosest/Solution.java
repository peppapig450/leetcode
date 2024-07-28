class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums); // Sort the array
        int closestSum = nums[0] + nums[1] + nums[2]; // Initialize the closest sum

        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1; // Left pointer
            int right = nums.length - 1; // Right pointer

            while (left < right) {
                int currentSum = nums[i] + nums[left] + nums[right]; // Calculate the current sum

                // If the current sum is closer to the target than the closest sum, update closest sum
                if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
                    closestSum = currentSum;
                }

                // Move the pointers baed on the comparison between current sum and target
                if (currentSum < target) {
                    left++;
                } else if (currentSum > target) {
                    right--;
                } else {
                    // If the current sum is the exactly the target, return it
                    return currentSum;
                }
            }
        }
        
        return closestSum;
    }
}