import java.util.Iterator;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] list;
    private int length = 0;
    private int capacity = 2;

    public RandomizedQueue() {
        // construct an empty randomized queue
        list = (Item[]) new Object[capacity];
    }

    private int randIndex() {
        return (int) (Math.random() * length);
    }
    private void exch(int i, int j) {
        Item temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
    private void resize(int newCapacity) {
        Item[] newList = (Item[]) new Object[newCapacity];
        for (int i = 0; i < length; i++) {
            newList[i] = list[i];
        }
        capacity = newCapacity;
        list = newList;
    }

    public boolean isEmpty() {
        // is the queue empty?
        return length == 0;
    }
    public int size() {
        // return the number of items on the queue
        return length;
    }
    public void enqueue(Item item) {
        if (item == null) {
            throw new java.lang.NullPointerException();
        }
        // add the item
        if (length == capacity) {
            resize(2 * capacity);
        }
        list[length++] = item;
        exch(length - 1, randIndex());
    }
    public Item dequeue() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        // delete and return a random item
        if (length > 0 && length * 4 < capacity) {
            resize(capacity / 2);
        }
        return list[--length];
    }
    public Item sample() {
        if (isEmpty()) {
            throw new java.util.NoSuchElementException();
        }
        // return (but do not delete) a random item
        exch(length - 1, randIndex());
        return list[length - 1];
    }
    public Iterator<Item> iterator() {
        // return an independent iterator over items in random order
        RandomizedQueue<Item> rq = new RandomizedQueue<Item>();
        rq.resize(capacity);
        for (int i = 0; i < length; i++) {
            rq.enqueue(list[i]);
        }
        return new InnerItr(rq);
    }

    private class InnerItr implements Iterator<Item> {
        private RandomizedQueue<Item> data;
        public InnerItr(RandomizedQueue<Item> rq) {
            data = rq;
        }
        public boolean hasNext() {
            return !data.isEmpty();
        }
        public Item next() {
            return data.dequeue();
        }
        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

    }
}
