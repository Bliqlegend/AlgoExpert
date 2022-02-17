from bst import BST
import sys
def findclosestBST(root,target,closest):
    if root is None:
        return 
    if abs(target - closest) > abs(target - root.value):
        ans = root.value
    if root.value < target:
        findclosestBST(root.right,target,closest) 
    if root.value > target:
        findclosestBST(root.left,target,closest)
    return closest


root = BST(10)
one = BST(5)
root.left = one
two = BST(15)
root.right = two
# map = hashmaker(root,12)
map = {
    13:1,
    14:2,
    15:3,
}
