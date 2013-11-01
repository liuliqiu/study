import java.util.Arrays;

public class Brute {
    private static void show(Point[] ps) {
        Arrays.sort(ps);
        StringBuilder build = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            if (i != 0) {
                build.append(" -> ");
            }
            build.append(ps[i].toString());
        }
        StdOut.println(build.toString());
        ps[0].drawTo(ps[3]);
    }
    private static void slove(Point[] points, int n) {
        Point p, q, r, s;
        double slope1, slope2, slope3;
        for (int i = 0; i < n; i++) {
            p = points[i];
            for (int j = i + 1; j < n; j++) {
                q = points[j];
                slope1 = p.slopeTo(q);
                for (int k = j + 1; k < n; k++) {
                    r = points[k];
                    slope2 = p.slopeTo(r);
                    if (slope1 != slope2) continue;
                    for (int l = k + 1; l < n; l++) {
                        s = points[l];
                        slope3 = p.slopeTo(s);
                        if (slope1 == slope3) {
                            Point[] ps = new Point[]{p, q, r, s};
                            show(ps);
                        }
                    }

                }
            }
        }
    }
    public static void main(String[] args) {
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        In in = new In(args[0]);
        int n = in.readInt();
        int x, y;
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            x = in.readInt();
            y = in.readInt();
            points[i] = new Point(x, y);
            points[i].draw();
        }
        slove(points, n);
    }
}
