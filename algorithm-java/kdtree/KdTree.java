import java.util.TreeSet;
import java.util.ArrayList;

public class KdTree {
    private TreeSet<Point2D> treeSet;
    private class TreeNode{
        public TreeNode(Point2D point, int deepth, TreeNode left, TreeNode right) {
            this.point = point;
            this.deepth = deepth;
            this.left = left;
            this.right = right;
        }
        private Point2D point;
        private TreeNode left;
        private TreeNode right;
        private int deepth;
    }
    private TreeNode root;
    private int nodeNumber;
    public KdTree() {
        // construct an empty set of points
        root = null;
        nodeNumber = 0;
    }

    public boolean isEmpty() {
        // is the set empty?
        return nodeNumber == 0;
    }

    public int size() {
        // number of points in the set
        return nodeNumber;
    }

    public void insert(Point2D p) {
        // add the point p to the set (if it is not already in the set)
        if (root = null) {
            root = TreeNode(p, 0, null, null);
        } else {
            TreeNode n = root;
        }
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
        double near_dis = 0, dis = 0;
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
