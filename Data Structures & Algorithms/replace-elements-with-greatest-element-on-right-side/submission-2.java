class Solution {
    public int[] replaceElements(int[] arr) {
        int current = arr[arr.length-1];
        arr[arr.length-1] = -1;
        int max = current;

        for(int i = arr.length-2; i >=0; i--){
            current = arr[i];
            arr[i] = max;
            if (current > max){
                max = current;
            }
            
        }

        return arr;
    }
}