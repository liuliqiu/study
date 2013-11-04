import java.util.ArrayList;

public class KdTree {
    private TreeNode root;
    private int nodeNumber;
    private Point2D near;
    private double nearDis;

    private class TreeNode {
        private Point2D point;
        private TreeNode left;
        private TreeNode right;
        private int deepth;
        public TreeNode(Point2D point, int deepth, TreeNode left, TreeNode right) {
            this.point = point;
            this.deepth = deepth;
            this.left = left;
            this.right = right;
        }
    }
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
            int c;
            while (n != null) {
                c = compair(p, n.point, n.deepth);
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
        iterDraw(root);
    }
    private void iterDraw(TreeNode n) {
        if (n == null) {
            return;
        }
        iterDraw(n.left);
        n.point.draw();
        iterDraw(n.right);
    }

    public Iterable<Point2D> range(RectHV rect) {
        // all points in the set that are inside the rectangle
        ArrayList<Point2D> list = new ArrayList<Point2D>();
        ArrayList<TreeNode> nodeToCheckout = new ArrayList<TreeNode>();
        nodeToCheckout.add(root);
        int i = 0;
        double x, y;
        while (i < nodeToCheckout.size()) {
            TreeNode n = nodeToCheckout.get(i);
            i++;
            if (n == null) continue;
            x = n.point.x();
            y = n.point.y();
            if (n.deepth % 2 == 0) {
                if (x > rect.xmax()) {
                    nodeToCheckout.add(n.left);
                } else if (x < rect.xmin()) {
                    nodeToCheckout.add(n.right);
                } else {
                    if (y >= rect.ymin() && y <= rect.ymax()) {
                        list.add(n.point);
                    }
                    nodeToCheckout.add(n.right);
                    nodeToCheckout.add(n.left);
                }
            } else {
                if (y > rect.ymax()) {
                    nodeToCheckout.add(n.left);
                } else if (y < rect.ymin()) {
                    nodeToCheckout.add(n.right);
                } else {
                    if (x >= rect.xmin() && x <= rect.xmax()) {
                        list.add(n.point);
                    }
                    nodeToCheckout.add(n.right);
                    nodeToCheckout.add(n.left);
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
        nearDis = p.distanceTo(near);
        searchNearest(root, p);
        return near;
    }

    private void searchNearest(TreeNode n, Point2D p) {
        double dis = p.distanceTo(n.point);
        if (dis < nearDis) {
            nearDis = dis;
            near = n.point;
        }
        double dx = p.x() - n.point.x();
        double dy = p.y() - n.point.y();
        if (needCheckLeft(n, dx, dy)) {
            searchNearest(n.left, p);
        }
        if (needCheckRight(n, dx, dy)) {
            searchNearest(n.right, p);
        }
    }

    private boolean needCheckLeft(TreeNode n, double dx, double dy) {
        if (n.left == null) {
            return false;
        }
        if (n.deepth % 2 == 0) {
            return dx <= nearDis;
        } else {
            return dy <= nearDis;
        }
    }
    private boolean needCheckRight(TreeNode n, double dx, double dy) {
        if (n.right == null) {
            return false;
        }
        if (n.deepth % 2 == 0) {
            return -dx <= nearDis;
        } else {
            return -dy <= nearDis;
        }
    }
    public static void main(String[] args) {
        String filename = args[0];
        In in = new In(filename);

        StdDraw.show(0);

        // initialize the two data structures with point from standard input
        KdTree kdtree = new KdTree();
        while (!in.isEmpty()) {
            double x = in.readDouble();
            double y = in.readDouble();
            Point2D p = new Point2D(x, y);
            kdtree.insert(p);
        }

        kdtree.draw();
    }

}
