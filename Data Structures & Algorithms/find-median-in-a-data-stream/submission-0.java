class MedianFinder {

    PriorityQueue<Integer> max;
    PriorityQueue<Integer> min;

    public MedianFinder() {
        max = new PriorityQueue<Integer>(Collections.reverseOrder());
        min = new PriorityQueue<Integer>();
    }
    
    public void addNum(int num) {
        if (max.size() == 0) max.add(num);
        else if (num < max.peek()) {
            max.add(num);
            if (max.size() > min.size()+1) min.add(max.poll());
        } else {
            min.add(num);
            if (min.size() > max.size()+1) max.add(min.poll());
        }
    }
    
    public double findMedian() {
        if (max.size() == 0) return 0;
        if (max.size() > min.size()) return (double)max.peek();
        if (min.size() > max.size()) return (double)min.peek();
        return (double)((double)max.peek()+(double)min.peek())/(double)2;
    }
}
