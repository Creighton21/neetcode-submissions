class Solution {
    public int removeElement(int[] nums, int val) {
        int numberOfElements = 0;
        for(int i = 0; i < nums.length; i++) {
            if (nums[i] == val){
                continue;
            }

            nums[numberOfElements] = nums[i];
            numberOfElements++;
        }

        return numberOfElements;
    }
}