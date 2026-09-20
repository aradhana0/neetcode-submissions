class LRUCache {
    static class Node {
        int key;
        int val;
        Node prev;
        Node next;
        Node(int key, int val) {
            this.val = val;
            this.key = key;
        }
    }

    Map<Integer, Node> cache;
    int capacity;
    Node start;
    Node end;

    public LRUCache(int capacity) {
        cache = new HashMap<>();
        this.capacity = capacity;
        start = new Node(-1, -1);
        end = new Node(-1, -1);
        start.next = end;
        end.prev = start;
    }
    
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node n = cache.get(key);
            remove(n);
            insert(n);
            return n.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node n = cache.get(key);
            n.val = value;
            remove(n);
            insert(n);
            cache.put(key, n);
        } else {
            if (cache.size() == capacity) {
                Node e = end.prev;
                cache.remove(e.key);
                remove(e);
            }
            Node n = new Node(key, value);
            insert(n);
            cache.put(key, n);
        }
    }

    private void insert(Node n) {
        Node next = start.next;
        start.next = n;
        n.prev = start;
        n.next = next;
        next.prev = n;
    }

    private void remove(Node n) {
        Node prev = n.prev;
        Node next = n.next;
        n.prev = null;
        n.next = null;
        prev.next = next;
        next.prev = prev;
    }
}