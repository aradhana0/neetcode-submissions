class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> pos = new HashMap<>();
        int max = 0;
        int left = 0;
        int right = 0;
        while (right < s.length()) {
            char c = s.charAt(right);
            if (pos.containsKey(c) && pos.get(c) >= left) left = pos.get(c) + 1;
            pos.put(c, right);
            max = Math.max(max, right-left+1);
            right++;
        }
        return max;
    }
}
