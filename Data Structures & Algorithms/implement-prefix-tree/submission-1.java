

class PrefixTree {

    Trie root;

    public PrefixTree() {
        root = new Trie('X');
    }

    public void insert(String word) {
        Trie curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c-'a'] == null) {
                Trie node = new Trie(c);
                curr.children[c-'a'] = node;
                curr = curr.children[c-'a'];
            } else curr = curr.children[c-'a'];
        }
        curr.isWord = true;
    }

    public boolean search(String word) {
        Trie curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c-'a'] != null) {
                curr = curr.children[c-'a'];
            } else return false;
        }
        return curr.isWord;
    }

    public boolean startsWith(String prefix) {
        Trie curr = root;
        for (char c : prefix.toCharArray()) {
            if (curr.children[c-'a'] != null) {
                curr = curr.children[c-'a'];
            } else return false;
        }
        return true;
    }
}

class Trie {
    char val;
    Trie[] children;
    //Map<Character, Trie> children = new HashMap<>();
    boolean isWord = false;
    public Trie(char c) {
        this.val = c;
        this.children = new Trie[26];
    }
}
