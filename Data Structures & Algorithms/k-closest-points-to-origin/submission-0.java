class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->Integer.compare(b[0], a[0]));
        for (int i=0; i<points.length; i++) {
            int[] co = points[i];
            int dist = co[0]*co[0] + co[1]*co[1];
            if (pq.size() < k) pq.add(new int[]{dist, i});
            else if(dist < pq.peek()[0]){
                pq.add(new int[]{dist, i});
                pq.poll();
            }
        }
        int[][] result = new int[k][2];
        int index = 0;
        while (pq.size() > 0) result[index++] = points[pq.poll()[1]];
        return result;
    }
}
