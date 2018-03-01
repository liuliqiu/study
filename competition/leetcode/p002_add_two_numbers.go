/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var result *ListNode = nil
    var current *ListNode = nil
    overflow := 0
    for ;l1 != nil || l2 != nil || overflow != 0;{
        var node ListNode
        if result == nil{
            result = &node
            current = &node
        } else {
            current.Next = &node
            current = current.Next
        }
        node.Val = overflow
        if l1 != nil {
            node.Val += l1.Val
            l1 = l1.Next
        }
        if l2 != nil{
            node.Val += l2.Val
            l2 = l2.Next
        }
        if node.Val >= 10{
            overflow = node.Val / 10
            node.Val %= 10
        } else {
            overflow = 0
        }
    }
    return result
}
