import java.util.List;
import java.util.ArrayList;

public class Board {
    private int dim;
    private int[][] data;
    private int blankX;
    private int blankY;

    public Board(int[][] blocks) {
        // construct a board from an N-by-N array of blocks
        // (where blocks[i][j] = block in row i, column j)
        dim = blocks.length;
        data = new int[dim][dim];
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                data[i][j] = blocks[i][j];
                if (blocks[i][j] == 0) {
                    blankX = i;
                    blankY = j;
                }
            }
        }
    }

    public int dimension() {
        // board dimension N
        return dim;
    }

    public int hamming() {
        // number of blocks out of place
        int ham = 0;
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                if (data[i][j] != 0 && data[i][j] != i * dim + j + 1) {
                    ham += 1;
                }
            }
        }
        return ham;
    }

    public int manhattan() {
        // sum of Manhattan distances between blocks and goal
        int mht = 0;
        int p, q;
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                if (data[i][j] != 0 && data[i][j] != i * dim + j + 1) {
                    p = (data[i][j] - 1) / dim;
                    q = (data[i][j] - 1) % dim;
                    mht += Math.abs(p - i) + Math.abs(j - q);
                }
            }
        }
        return mht;
    }

    public boolean isGoal() {
        // is this board the goal board?
        return hamming() == 0;
    }

    public Board twin() {
        // a board obtained by exchanging two adjacent blocks in the same row
        int i;
        if (blankX == 0) {
            i = 1;
        } else {
            i = 0;
        }
        int[][] newData = copyExch(i, 0, i, 1);
        return new Board(newData);
    }

    public boolean equals(Object y) {
        // does this board equal y?
        if (this == y) {
            return true;
        }
        if (y == null) {
            return false;
        }
        if (this.getClass() != y.getClass()) {
            return false;
        }
        Board that = (Board) y;
        if (this.dim != that.dim) {
            return false;
        }
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                if (this.data[i][j] != that.data[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public Iterable<Board> neighbors() {
        // all neighboring boards
        List<Board> list = new ArrayList<Board>();
        if (blankX > 0) {
            Board b = new Board(copyExch(blankX, blankY, blankX - 1, blankY));
            list.add(b);
        }
        if (blankX < dim - 1) {
            Board b = new Board(copyExch(blankX, blankY, blankX + 1, blankY));
            list.add(b);
        }
        if (blankY > 0) {
            Board b = new Board(copyExch(blankX, blankY, blankX, blankY - 1));
            list.add(b);
        }
        if (blankY < dim - 1) {
            Board b = new Board(copyExch(blankX, blankY, blankX, blankY + 1));
            list.add(b);
        }
        return list;
    }


    public String toString() {
        // string representation of the board (in the output format specified below)
        StringBuilder sb = new StringBuilder();
        sb.append(dim).append("\n");
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                if (j != 0) {
                    sb.append(" ");
                }
                sb.append(String.format("%2d", data[i][j]));
            }
            sb.append("\n");
        }

        return sb.toString();
    }
    private int[][] copyExch(int x1, int y1, int x2, int y2) {
        int[][] newData = new int[dim][dim];
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                newData[i][j] = data[i][j];
            }
        }
        newData[x1][y1] = data[x2][y2];
        newData[x2][y2] = data[x1][y1];
        return newData;
    }

}

