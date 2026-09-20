class Solution {

    public int characterReplacement(String s, int k) {
        int left = 0;
        int right = 0;
        int max = 0;
        while (right < s.length()) {
            String str = s.substring(left, right+1);
            //System.out.println(str);
            if (str.length() - mostFrequent(str) <= k) max = Math.max(str.length(), max);
            else left++;
            right++;
        }
        return max;
    }

    private int mostFrequent(String str) {
        int[] arr = new int[26];
        int max = 0;
        for (char c : str.toCharArray()) {
            arr[c-'A']++;
            max = Math.max(max, arr[c-'A']);
        }
        return max;
    }
}
