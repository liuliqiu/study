/*************************************************************************
 * Name:
 * Email:
 *
 * Compilation:  javac Point.java
 * Execution:
 * Dependencies: StdDraw.java
 *
 * Description: An immutable data type for points in the plane.
 *
 *************************************************************************/

import java.util.Comparator;

public class Point implements Comparable<Point> {

    // compare points by slope
    public final Comparator<Point> SLOPE_ORDER = new SlopeOrder();       // YOUR DEFINITION HERE

    private class SlopeOrder implements Comparator<Point> {
        public int compare(Point p1, Point p2) {
            double s1 = slopeTo(p1);
            double s2 = slopeTo(p2);
            if (s1 < s2) {
                return -1;
            } else if (s1 > s2) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    private final int x;                              // x coordinate
    private final int y;                              // y coordinate

    // create the point (x, y)
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
    }

    // plot this point to standard drawing
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    // draw line between this point and that point to standard drawing
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // slope between this point and that point
    public double slopeTo(Point that) {
        if (this.x == that.x) {
            if (this.y == that.y) {
                return Float.NEGATIVE_INFINITY;
            } else {
                return Float.POSITIVE_INFINITY;
            }
        }
        if (that.y == this.y) {
            return 0.0;
        }
        return (that.y - this.y) / (double) (that.x - this.x);
    }

    // is this point lexicographically smaller than that one?
    // comparing y-coordinates and breaking ties by x-coordinates
    public int compareTo(Point that) {
        int c1 = this.y - that.y;
        if (c1 != 0) {
            return c1;
        }
        return this.x - that.x;
    }

    // return string representation of this point
    public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
    }

    // unit test
    public static void main(String[] args) {
        /* YOUR CODE HERE */
    }
}
