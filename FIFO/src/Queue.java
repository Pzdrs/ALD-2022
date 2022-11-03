public class Queue<T> {
    private static class Node<T> {
        protected Node<T> prev;
        protected T value;
        protected Node<T> next;

        public Node(Node<T> prev, T value, Node<T> next) {
            this.prev = prev;
            this.value = value;
            this.next = next;
        }
    }

    private Node<T> head, end;

    public void push(T val) {
        final Node<T> last = end;
        final Node<T> newNode = new Node<>(last, val, null);
        this.end = newNode;
        if (last == null)
            this.head = newNode;
        else
            last.next = newNode;
    }

    public T pop() {
        if (head == null) return null;
        Node<T> oldHead = head;
        Node<T> newHead = head.next;
        if (newHead != null) {
            newHead.prev = null;
            this.head = newHead;
        } else {
            this.head = null;
            this.end = null;
        }
        return oldHead.value;
    }
}
