class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] mem = new int[text1.length()+1][text2.length()+1];
        for (int r=0; r<text1.length(); r++) {
            for (int c=0; c<text2.length(); c++) {
                if (text1.charAt(r) == text2.charAt(c)) {
                    mem[r+1][c+1] = 1 + mem[r][c];
                } else mem[r+1][c+1] = Math.max(mem[r][c+1], mem[r+1][c]);
            }
        }
        return mem[text1.length()][text2.length()];
    }
}
