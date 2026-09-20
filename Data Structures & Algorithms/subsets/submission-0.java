class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<Integer>());
        helper(nums, new ArrayList<Integer>(), ans, 0);
        return ans;
    }

    private void helper(int[] nums, List<Integer> arr, List<List<Integer>> ans, int index) {
        if (index >= nums.length) return;
        for (int i = index; i<nums.length; i++) {
            arr.add(nums[i]);
            ans.add(new ArrayList<Integer>(arr));
            helper(nums, arr, ans, i+1);
            arr.remove(arr.size()-1);
        }
    }
}
