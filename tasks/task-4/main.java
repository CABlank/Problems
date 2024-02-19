import java.util.HashMap;
import java.util.Map;

class main {
    static class Node {
        int count;
        Map<Character, Node> children;

        public Node() {
            count = 0;
            children = new HashMap<>();
        }
    }

    static class Trie {
        private Node root;

        public Trie() {
            root = new Node();
        }

        public void insert(String word) {
            Node current = root;
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                current.children.putIfAbsent(ch, new Node());
                current = current.children.get(ch);
                current.count++;
            }
        }

        public String find(String word) {
            Node current = root;
            StringBuilder prefix = new StringBuilder();
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                prefix.append(ch);
                if (current.children.get(ch).count == 1) {
                    return prefix.toString();
                }
                current = current.children.get(ch);
            }
            return prefix.toString();
        }
    }

    public static String[] shortestUniquePrefix(String[] words) {
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }

        String[] result = new String[words.length];
        for (int i = 0; i < words.length; i++) {
            result[i] = trie.find(words[i]);
        }
        return result;
    }

public static void main(String[] args) {
    String[] words = {"joma", "john", "jack", "techlead"};
    String[] result = shortestUniquePrefix(words);
    for (String s : result) {
        System.out.println(s);
    }
}
}

       
