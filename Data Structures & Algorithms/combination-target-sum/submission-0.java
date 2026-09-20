class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        helper(nums, target, new ArrayList<>(), result, 0);
        return result;
    }

    private void helper(int[] nums, int target, List<Integer> arr, List<List<Integer>> ans, int i) {
        
        if (i >= nums.length || target < 0) return;
        
        if (target == 0) {
            ans.add(new ArrayList<Integer>(arr));
            return;
        }

        arr.add(nums[i]);
        helper(nums, target-nums[i], arr, ans, i);
        arr.remove(arr.size()-1);
        helper(nums, target, arr, ans, i+1);
    }

}
