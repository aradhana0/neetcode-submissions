class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        int[] cache = new int[amount+1];
        Arrays.fill(cache, amount+1);
        cache[0] = 0;
        for (int amt = 1; amt <= amount; amt++) {
            for (int i=0; i<coins.length; i++) {
                int remaining = amt-coins[i];
                if (remaining>=0){
                    cache[amt] = Math.min(cache[amt], 1+ cache[remaining]);
                }
            }
        }
        return cache[amount] == amount+1 ? -1 : cache[amount];
    }
}
