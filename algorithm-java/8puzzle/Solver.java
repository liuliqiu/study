import java.util.List;
import java.util.ArrayList;

public class Solver {
    private Board init;
    private boolean solvable;
    private int m;
    private List<Board> sol;
    public Solver(Board initial) {
        // find a solution to the initial board (using the A* algorithm)
        init = initial;
        solvable = false;
        m = -1;
        sol = null;
        solve();
    }

    private class SearchNode implements Comparable<SearchNode> {
        private Board board;
        private int moves;
        private SearchNode prev;
        private SearchNode(Board b, int m, SearchNode p) {
            moves = m;
            board = b;
            prev = p;
        }
        public int compareTo(SearchNode that) {
            return this.board.hamming() + this.moves - that.board.hamming() - that.moves;
        }
    }

    private void solve() {
        if (init.isGoal()) {
            trackBack(new SearchNode(init, 0, null));
            return;
        }
        Board twin = init.twin();
        if (twin.isGoal()) {
            return;
        }
        MinPQ<SearchNode> pq1 = new MinPQ<SearchNode>();
        pq1.insert(new SearchNode(init, 0, null));
        MinPQ<SearchNode> pq2 = new MinPQ<SearchNode>();
        pq2.insert(new SearchNode(twin, 0, null));
        while (!pq1.isEmpty() || !pq2.isEmpty()) {
            if (!pq1.isEmpty()) {
                SearchNode a = pq1.delMin();
                for (Board b : a.board.neighbors()) {
                    if (b.isGoal()) {
                        trackBack(new SearchNode(b, a.moves + 1, a));
                        return;
                    }
                    if (a.prev == null || !b.equals(a.prev.board)) {
                        pq1.insert(new SearchNode(b, a.moves + 1, a));
                    }
                }
            }
            if (!pq2.isEmpty()) {
                SearchNode a2 = pq2.delMin();
                for (Board b : a2.board.neighbors()) {
                    if (b.isGoal()) {
                        return;
                    }
                    if (a2.prev == null || !b.equals(a2.prev.board)) {
                        pq2.insert(new SearchNode(b, a2.moves + 1, a2));
                    }
                }
            }
        }
    }
    private void trackBack(SearchNode a) {
        sol = new ArrayList<Board>();
        m = a.moves;
        solvable = true;
        SearchNode n = a;
        while (n != null) {
            sol.add(0, n.board);
            n = n.prev;
        }
    }

    public boolean isSolvable() {
        // is the initial board solvable?
        return solvable;
    }

    public int moves() {
        // min number of moves to solve initial board; -1 if no solution
        return m;
    }

    public Iterable<Board> solution() {
        // sequence of boards in a shortest solution; null if no solution
        return sol;
    }

    public static void main(String[] args) {
        // solve a slider puzzle (given below)
        In in = new In(args[0]);
        int N = in.readInt();
        int[][] blocks = new int[N][N];
        for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
        blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        //StdOut.println(initial);
        //StdOut.println(initial.twin());

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}
