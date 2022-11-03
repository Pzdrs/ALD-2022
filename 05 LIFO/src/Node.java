public class Node<T> {
    protected final T value;

    protected final Node<T> neighbor;

    public Node(T value, Node<T> neighbor) {
        this.value = value;
        this.neighbor = neighbor;
    }

    public void print() {
        System.out.println(capitalize(String.valueOf(value)));
        if (neighbor != null)
            neighbor.print();
    }

    private static String capitalize(final String s) {
        String[] words = s.split(" ");
        StringBuilder builder = new StringBuilder();
        for (String word : words) {
            builder.append(word.substring(0, 1).toUpperCase()).append(word.substring(1)).append(" ");
        }
        return builder.toString();
    }
}
