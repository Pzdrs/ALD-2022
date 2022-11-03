public class Stack<T> {
    private Node<T> head;

    public void push(T val) {
        Node<T> currentHead = this.head;
        this.head = new Node<>(val, currentHead);
    }

    public T pop() {
        if (head == null) return null;
        Node<T> popped = head;
        this.head = popped.neighbor;
        return popped.value;
    }

    public void print() {
        head.print();
    }
}
