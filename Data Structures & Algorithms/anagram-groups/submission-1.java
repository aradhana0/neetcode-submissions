class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            String sorted = sort(str);
            List<String> l = map.getOrDefault(sorted, new ArrayList<String>());
            l.add(str);
            map.put(sorted, l);
        }
        return new ArrayList<>(map.values());
    }

    private String sort(String str) {
        int[] arr = new int[26];
        for (char c : str.toCharArray()) arr[c-'a']++;
        String key = Arrays.toString(arr);
        // StringBuilder sb = new StringBuilder();
        // for (int i=0; i<26; i++){
        //     while (arr[i] != 0) {
        //         sb.append((char)(i+'a'));
        //         arr[i]--;
        //     }
        // }
        // return sb.toString();
        System.out.println(key); // [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        return key;
    }
}
