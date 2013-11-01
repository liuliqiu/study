import java.util.Iterator;

public class Deque<Item> implements Iterable<Item> {
    private Node first;
    private Node last;
    private int length;
    private class Node {
        private Item data;
        private Node next;
        private Node prev;
    }
    public Deque() {
        // construct an empty deque
        first = new Node();
        last = new Node();
        first.next = last;
        last.prev = first;
        length = 0;
    }
    public boolean isEmpty() {
        // is the deque empty?
        return first.next == last;
    }
    public int size() {
        // return the number of items on the deque
        return length;
    }
    public void addFirst(Item item) {
        // insert the item at the front
        if (item == null) {
            throw new java.lang.NullPointerException();
        }
        Node n = new Node();
        first.next.prev = n;
        n.data = item;
        n.next = first.next;
        n.prev = first;
        first.next = n;
        length++;
    }
    public void addLast(Item item) {
        // insert the item at the end
        if (item == null) {
            throw new java.lang.NullPointerException();
        }
        Node n = new Node();
        last.prev.next = n;
        n.data = item;
        n.next = last;
        n.prev = last.prev;
        last.prev = n;
        length++;
    }
    public Item removeFirst() {
        // delete and return the item at the front
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        Node temp = first.next;
        first.next.next.prev = first;
        first.next = first.next.next;
        length--;
        return temp.data;
    }
    public Item removeLast() {
        // delete and return the item at the end
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        Node temp = last.prev;
        last.prev.prev.next = last;
        last.prev = last.prev.prev;
        length--;
        return temp.data;
    }
    public Iterator<Item> iterator() {
        // return an iterator over items in order from front to end
        return new InnerItr();
    }
    private class InnerItr implements Iterator<Item> {
        private Node current;
        public InnerItr() {
            current = first;
        }
        public boolean hasNext() {
            return current.next != last;
        }
        public Item next() {
            if (current.next == last) {
                throw new java.util.NoSuchElementException();
            }
            current = current.next;
            return current.data;
        }
        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }
    }
}

