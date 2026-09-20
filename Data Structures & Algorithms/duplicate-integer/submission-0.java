class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> has = new HashSet<>();
        for (int num : nums) {
            if(has.contains(num)) return true;
            has.add(num);
        }
        return false;
    }
}
