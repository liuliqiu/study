import java.util.TreeSet;
import java.util.ArrayList;
import java.util.Stack;

public class KdTree {
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
        if (root == null) {
            root = new TreeNode(p, 0, null, null);
        } else {
            TreeNode n = root;
            int c = compair(n.point, p, n.deepth);
            while (n != null) {
                if (c == -1) {
                    if (n.left == null) {
                        n.left = new TreeNode(p, n.deepth + 1, null, null);
                        break;
                    } else {
                        n = n.left;
                    }
                } else if (c == 1) {
                    if (n.right == null) {
                        n.right = new TreeNode(p, n.deepth + 1, null, null);
                        break;
                    } else {
                        n = n.right;
                    }
                } else {
                    throw new IllegalArgumentException("The node is already in the set");
                }
            }
        }
        nodeNumber++;
    }

    public int compair(Point2D p, Point2D q, int d) {
        if (d % 2 == 0) {
            if (p.x() < q.x() || (p.x() == q.x() && p.y() < q.y())) {
                return -1;
            } else if (p.x() > q.x() || (p.x() == q.x() && p.y() > q.y())) {
                return 1;
            } else {
                return 0;
            }
        } else {
            if (p.y() < q.y() || (p.y() == q.y() && p.x() < q.x())) {
                return -1;
            } else if (p.y() > q.y() || (p.y() == q.y() && p.x() > q.x())) {
                return 1;
            } else {
                return 0;
            }
        }
    }


    public boolean contains(Point2D p) {
        // does the set contain the point p?
        TreeNode n = root;
        int c;
        while (n != null) {
            c = compair(n.point, p, n.deepth);
            if (c == -1) {
                n = n.left;
            } else if (c == 1) {
                n = n.right;
            } else {
                return true;
            }
        }
        return false;
    }

    public void draw() {
        // draw all of the points to standard draw
        // TODO 
    }

    public Iterable<Point2D> range(RectHV rect) {
        // all points in the set that are inside the rectangle
        ArrayList<Point2D> list = new ArrayList<Point2D>();
        ArrayList<TreeNode> node_to_checkout = new ArrayList<TreeNode>();
        node_to_checkout.add(root);
        int i = 0;
        double x, y;
        while (i < node_to_checkout.size()) {
            TreeNode n = node_to_checkout.get(i);
            i++;
            if (n == null) continue;
            x = n.point.x();
            y = n.point.y();
            if (n.deepth % 2 == 0) {
                if (x > rect.xmax()) {
                    node_to_checkout.add(n.left);
                } else if (x < rect.xmin()) {
                    node_to_checkout.add(n.right);
                } else {
                    if (y >= rect.ymin() && y <= rect.ymax()) {
                        list.add(n.point);
                    }
                    node_to_checkout.add(n.right);
                    node_to_checkout.add(n.left);
                }
            } else {
                if (y > rect.ymax()) {
                    node_to_checkout.add(n.left);
                } else if (y < rect.ymin()) {
                    node_to_checkout.add(n.right);
                } else {
                    if (x >= rect.xmin() && x <= rect.xmax()) {
                        list.add(n.point);
                    }
                    node_to_checkout.add(n.right);
                    node_to_checkout.add(n.left);
                }
            }
        }
        return list;
    }

    public Point2D nearest(Point2D p) {
        // a nearest neighbor in the set to p; null if set is empty
        if (isEmpty()) {
            return null;
        }
        near = root.point;
        dis_near = p.distanceTo(near);
        StdOut.println(p);
        search_nearest(root, p);
        return near;
    }

    private Point2D near;
    private double dis_near;
    private void search_nearest(TreeNode n, Point2D p) {
        double dis = p.distanceTo(n.point);
        if (dis < dis_near) {
            dis_near = dis;
            near = n.point;
        }
        double dx = p.x() - n.point.x();
        double dy = p.y() - n.point.y();
        if (need_check_left(n, dx, dy)){
            search_nearest(n.left, p);
            StdOut.println("need_check_left:");
            StdOut.println(n.point);
            StdOut.println(n.deepth);
            StdOut.println(need_check_left(n, dx, dy));
            StdOut.println(near);
        }
        if (need_check_right(n, dx, dy)) {
            search_nearest(n.right, p);
            StdOut.println("need_check_right:");
            StdOut.println(n.point);
            StdOut.println(n.deepth);
            StdOut.println(need_check_right(n, dx, dy));
            StdOut.println(near);
        }
    }

    private boolean need_check_left(TreeNode n, double dx, double dy) {
        if (n.left == null) {
            return false;
        }
        if (n.deepth % 2 == 0) {
            return dx <= dis_near;
        } else {
            return dy <= dis_near;
        }
    }
    private boolean need_check_right(TreeNode n, double dx, double dy) {
        if (n.right == null) {
            return false;
        }
        if (n.deepth % 2 == 0) {
            return -dx <= dis_near;
        } else {
            return -dy <= dis_near;
        }
    }

}
