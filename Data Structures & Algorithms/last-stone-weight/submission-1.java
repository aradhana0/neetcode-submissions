class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int stone : stones) pq.add(stone);
        while (pq.size() > 1) {
            int s1 = pq.poll();
            int s2 = pq.poll();
            pq.add(Math.abs(s1-s2));
        }
        return pq.size() == 0 ? 0 : pq.peek();
    }
}
