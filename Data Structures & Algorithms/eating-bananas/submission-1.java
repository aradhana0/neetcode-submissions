class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        long hr = (long) h;
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();  
        int result = right;
        while (left<=right) {
            int mid = left + (right-left)/2;
            long hours = hours(piles, mid);
            if (hours <= hr) {
                result = mid;
                right = mid -1;
            } else left = mid+1;
        }
        return result;
    }

    private long hours(int[] arr, int rate) {
        long hours = 0;
        for (int i=0; i<arr.length; i++) hours += (arr[i]+rate-1)/rate;
        return hours;
    }
}
