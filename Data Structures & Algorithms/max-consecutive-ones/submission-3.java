class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_count = 0;
        int current_count = 0;
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            if (current == 0) {
                current_count = 0;
                continue;
            }
            else if (current == 1) {
                current_count += 1;
            }

            if (max_count < current_count) {
                max_count = current_count;
            }
            
        }

        return max_count;
    }
}

/*
Trace [1,1,0,1,1,1] by hand
Test all zeros, all ones, and a single element
Explain your time and space complexity
*/