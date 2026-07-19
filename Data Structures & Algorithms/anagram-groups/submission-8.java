class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Use a String as the key instead of a List<Integer>
        Map<String, List<String>> hm = new HashMap<>();

        for (String s : strs) {
            int[] counts = new int[26];
            for (char c : s.toCharArray()) {
                counts[c - 'a']++;
            }
            
            // Build a lightweight unique string signature for the counts
            // Example: [1, 2, 0...] becomes "1#2#0..."
            StringBuilder sb = new StringBuilder();
            for (int count : counts) {
                sb.append(count).append('#');
            }
            String key = sb.toString();
            
            hm.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(hm.values());
    }
}