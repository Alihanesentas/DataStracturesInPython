class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
firstNode = Node(2)
secondNode = Node(4)
thirdNode = Node(3)
fourthNode = Node(5)
firstNode.left = secondNode
firstNode.right = thirdNode
firstNode.left = fourthNode


'''
Terminologies in Binary Tree
Nodes: The fundamental part of a binary tree, where each node contains data and link to two child nodes.
Root: The topmost node in a tree is known as the root node. It has no parent and serves as the starting point for all nodes in the tree.
Parent Node: A node that has one or more child nodes. In a binary tree, each node can have at most two children.
Child Node: A node that is a descendant of another node (its parent).
Leaf Node: A node that does not have any children or both children are null.
Internal Node: A node that has at least one child. This includes all nodes except the leaf nodes.
Depth of a Node: The number of edges from a specific node to the root node. The depth of the root node is zero.
Height of a Binary Tree: The number of nodes from the deepest leaf node to the root node.
'''
'''
Properties of Binary Tree
The maximum number of nodes at level L of a binary tree is 2L
The maximum number of nodes in a binary tree of height H is 2H – 1
Total number of leaf nodes in a binary tree = total number of nodes with 2 children + 1
In a Binary Tree with N nodes, the minimum possible height or the minimum number of levels is Log2(N+1)
A Binary Tree with L leaves has at least | log₂(L) |+ 1 level
'''
# Preorder Traversal of BT
'''
The root node of the subtree is visited first.
Next, the left subtree is recursively traversed.
Finally, the right subtree is recursively traversed.
'''

'''
f the root is NULL, return; 
Process the root node (e.g., print its value); 
Recursively traverse the left subtree; 
Recursively traverse the right subtree.'''



def printPreorder(node):
        if node is None:
            return
        print(node.data, end=' ')
        printPreorder(node.left)
        printPreorder(node.right)

# Inorder Traversal of BT
'''
Left subtree is visited first.
Root node is processed next.
Right subtree is visited last.
'''
def printInorder(node):
      if node is None:
            return 
      printInorder(node.left)
      print(node.data, end =' ')
      printInorder(node.right)

# PostOrder Traversal of BT
'''
The left subtree is visited first.
The right subtree is visited next.
The root node is processed last.'''

def printPostorder(node):
      if node is None:
            return
      printPostorder(node.left)
      printPostorder(node.right)
      print(node.data,end=' ')  

#Level-order-tree-traversal
'''
How does level order ?
- Recursion
-Queue(Itarative)
'''
def levelOrderRec(root,level,res):
      if root is None:
            return
      if len(res) <= level:
            res.append([])
      res[level].append(root.data)
      levelOrderRec(root.left, level+1,res)    
      levelOrderRec(root.right,level+1,res)
def levelOrder(root):
      res = []
      levelOrderRec(root,0,res)
      return res

if __name__ == '__main__':
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(6)
        printPreorder(root)
        print("\n")
        printInorder(root)
        printPostorder(root)
        res = levelOrder(root)
        for level in res:
              print(f'[{', '.join(map(str,level))}]',end=' ')
        