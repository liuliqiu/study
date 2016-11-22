public class PercolationStats {
    private double[] result;
    public PercolationStats(int N, int T) {
        // perform T independent computational experiments on an N-by-N grid
        if (N <= 0 || T <= 0)
            throw new java.lang.IllegalArgumentException();
        int count, i, j;
        double N_2 = N * N;
        result = new double[T];
        Percolation p;
        for (int k = 0; k < T; k++) {
            p = new Percolation(N);
            count = 0;
            while (!p.percolates()) {
                i = (int) (Math.random() * N) + 1;
                j = (int) (Math.random() * N) + 1;
                if (!p.isOpen(i, j)) {
                    p.open(i, j);
                    count++;
                }
            }
            result[k] = count / N_2;
        }
    }
    public double mean() {
        // sample mean of percolation threshold
        double sum = 0;
        for (int i = 0; i < result.length; i++) {
            sum += result[i];
        }
        return sum / result.length;
    }
    public double stddev() {
        // sample standard deviation of percolation threshold
        double m = mean();
        double sum = 0;
        double temp;
        for (int i = 0; i < result.length; i++) {
            temp = result[i] - m;
            sum += temp * temp;
        }
        return Math.pow(sum / (result.length - 1), 0.5);
    }
    public double confidenceLo() {
        // returns lower bound of the 95% confidence interval
        return mean() - (1.96 * stddev()) / Math.pow(result.length, 0.5);
    }
    public double confidenceHi() {
        // returns upper bound of the 95% confidence interval
        return mean() + (1.96 * stddev()) / Math.pow(result.length, 0.5);
    }
    public static void main(String[] args) {
        // test client, described below
        int N, T;
        N = Integer.parseInt(args[0]);
        T = Integer.parseInt(args[1]);
        PercolationStats ps = new PercolationStats(N, T);
        String s;
        s = String.format("mean                    = %.16f", ps.mean());
        System.out.println(s);
        s = String.format("stddev                  = %.16f", ps.stddev());
        System.out.println(s);
        s = "95%% confidence interval = %.16f, %.16f";
        s = String.format(s, ps.confidenceLo(), ps.confidenceHi());
        System.out.println(s);
    }
}
