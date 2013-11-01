import java.util.Arrays;
import java.util.ArrayList;

public class Fast {
    private static class Line {
        private Point p;
        private double slope;
    }
    private static void show(Point[] ps) {
        StringBuilder build = new StringBuilder();
        for (int i = 0; i < ps.length; i++) {
            if (i != 0) {
                build.append(" -> ");
            }
            build.append(ps[i].toString());
        }
        ps[0].drawTo(ps[ps.length - 1]);
        StdOut.println(build.toString());
    }

    private static void slove(Point[] points, int n) {
        ArrayList<Line> records = new ArrayList<Line>();
        for (int i = 0; i < n - 2; i++) {
            Point p = points[i];
            Arrays.sort(points, i + 1, n, p.SLOPE_ORDER);
            int begin = i + 1;
            double slope, nextSlope;
            nextSlope = p.slopeTo(points[i + 1]);
            for (int j = i + 1; j < n; j++) {
                slope = nextSlope;
                if (j < n - 1) {
                    nextSlope = p.slopeTo(points[j + 1]);
                }
                if (slope != nextSlope || j == n - 1) {
                    if (j - begin > 1) {
                        boolean repeat = false;
                        for (Line record : records) {
                            if (slope == record.slope && slope == p.slopeTo(record.p)) {
                                repeat = true;
                            }
                        }
                        if (!repeat) {
                            Line line = new Line();
                            line.p = p;
                            line.slope = slope;
                            records.add(line);
                            Point[] ps = new Point[j - begin + 2];
                            ps[0] = p;
                            for (int k = 0; k < j - begin + 1; k++) {
                                ps[k + 1] = points[begin + k];
                            }
                            Arrays.sort(ps);
                            show(ps);
                        }
                    }
                    begin = j + 1;
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
        Arrays.sort(points);
        slove(points, n);
    }
}
