class Node:
    # constructor
    def __init__(self,key):
        self.val =  key
        self.right =  None
        self.left = None

# inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
# inserting valur in the bst tree
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right =  node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

# 
r = Node(50) 
insert(r,Node(3)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(7)) 
insert(r,Node(60)) 
insert(r,Node(80))
print('##### Solution #######')
inorder(r)
print('####### End ##########')


