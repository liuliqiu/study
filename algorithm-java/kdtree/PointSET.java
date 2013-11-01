import java.util.TreeSet;
import java.util.ArrayList;

public class PointSET {
    private TreeSet<Point2D> treeSet;
    public PointSET() {
        // construct an empty set of points
        treeSet = new TreeSet<Point2D>();
    }

    public boolean isEmpty() {
        // is the set empty?
        return treeSet.isEmpty();
    }

    public int size() {
        // number of points in the set
        return treeSet.size();
    }

    public void insert(Point2D p) {
        // add the point p to the set (if it is not already in the set)
        treeSet.add(p);
    }

    public boolean contains(Point2D p) {
        // does the set contain the point p?
        return treeSet.contains(p);
    }

    public void draw() {
        // draw all of the points to standard draw
        for (Point2D p : treeSet) {
            p.draw();
        }
    }

    public Iterable<Point2D> range(RectHV rect) {
        // all points in the set that are inside the rectangle
        ArrayList<Point2D> list = new ArrayList<Point2D>();
        for (Point2D p : treeSet) {
            if (rect.contains(p)) {
                list.add(p);
            }
        }
        return list;
    }

    public Point2D nearest(Point2D p) {
        // a nearest neighbor in the set to p; null if set is empty
        Point2D near = null;
        double near_dis = 0, dis;
        for (Point2D q : treeSet) {
            dis = q.distanceTo(p);
            if (near == null || dis < near_dis) {
                near_dis = dis;
                near = q;
            }
        }
        return near;
    }

}
