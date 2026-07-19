class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> hm = new HashMap<>();

        for (String s : strs) {
            int[] counts = new int[26];
            
            for (char c : s.toCharArray()){
                counts[c - 'a']++;
            }
            
            List<Integer> key = new ArrayList<>(26);
            for (int count : counts) {
                key.add(count);
            }
            
            hm.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(hm.values());
    }
}