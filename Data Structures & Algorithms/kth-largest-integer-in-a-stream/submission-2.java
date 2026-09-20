class KthLargest {

    int k;
    PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<Integer>();
        for (int i=0; i<nums.length; i++){
            if (pq.size() < k) pq.add(nums[i]);
            else if (nums[i] > pq.peek()){
                pq.poll();
                pq.add(nums[i]);
            }
        }
    }
    
    public int add(int val) {
        if (pq.size() < k) pq.add(val);
        else if (val > pq.peek()){
            pq.poll();
            pq.add(val);
        }
        return pq.peek();
    }
}
