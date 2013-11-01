public class Percolation {
    private int[][] M;
    private int len;
    private WeightedQuickUnionUF Q;
    public Percolation(int N) {
        // create N-by-N grid, with all sites blocked
        M = new int[N][N];
        Q = new WeightedQuickUnionUF(N * N + 2);
        len = N;
    }
    public void open(int i, int j) {
        // open site (row i, column j) if it is not already
        int pos = (i - 1) * len + j - 1;
        if (!isOpen(i, j)) {
            M[i - 1][j - 1] = 1;
            if (i == 1) {
                Q.union(pos, len * len);
            }
            if (i > 1 && isOpen(i - 1, j))
                Q.union(pos - len, pos);
            if (j > 1 && isOpen(i, j - 1))
                Q.union(pos - 1, pos);
            if (i < len && isOpen(i + 1, j))
                Q.union(pos + len, pos);
            if (j < len && isOpen(i, j + 1))
                Q.union(pos + 1, pos);
        }
    }
    public boolean isOpen(int i, int j) {
        // is site (row i, column j) open?
        return M[i - 1][j - 1] == 1;
    }
    public boolean isFull(int i, int j) {
        // is site (row i, column j) full?
        return isOpen(i, j) && Q.connected(len * len, (i - 1) * len + j - 1);
    }
    public boolean percolates() {
        // does the system percolate?
        for (int i = 0; i < len; i++) {
            if (Q.connected(len * len, (len - 1) * len + i)) {
                return true;
            }
        }
        return false;
    }
}
