class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None  
        self.height=0
class AVLBST:
    def insertion(self,data,root):
        if(not root):
            return Node(data) 
        if(root.data>data):
            root.left=self.insertion(data,root.left)
        else:
            root.right=self.insertion(data,root.right)
        root.height=max(self.height(root.left),self.height(root.right))+1 
        balance=self.height(root.left)-self.height(root.right)
        if(balance>1 and data<root.left.data):
            return self.rightrotation(root)
        if(balance>1 and data>root.left.data):
            root.left=self.leftrotation(root.left)
            return self.rightrotation(root)
        if(balance<-1 and data>root.right.data):
            return self.leftrotation(root)
        if(balance<-1 and data<root.right.data):
            root.right=self.rightrotation(root.right)
            return self.leftrotation(root)
        return root
    def height(self,root):
        if(not root):
            return 0 
        return root.height  
    def leftrotation(self,x):
        y=x.right
        f=y.left 
        y.left=x 
        x.right=f 
        x.height=1+max(self.height(root.left),self.height(root.right))
        y.height=1+max(self.height(root.left),self.height(root.right))
        return y
    def rightrotation(self,x):
        y=x.left
        f=y.right 
        y.right=x 
        x.left=f 
        x.height=1+max(self.height(root.left),self.height(root.right))
        y.height=1+max(self.height(root.left),self.height(root.right))
        return y 
    def inorder(self,root):
        if(not root):
            return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    def deletion(self,root,data):
        if(not root):
            return 
        if(data<root.data):
            root.left=self.deletion(root.left,data)
        elif(data>root.data):
            root.right=self.deletion(right.right,data)
        else:
            if(not root.left):
                temp=root.right
                root=None
                return temp
            elif(not root.right):
                temp=root.left
                root=None 
                return temp 
            else:
                parent=root
                sucessor=root.right
                while(sucessor.left):
                    parent=sucessor
                    sucessor=sucessor.left
                if(parent==sucessor):
                    parent.right=sucessor.right
                else:
                    parent.left=sucessor.right
                root.data,sucessor.data=sucessor.data,root.data 
                return root 
        if(not root):
            return None 
        root.height=max(self.height(root.left),self.height(root.right))+1 
        balance=self.height(root.left)-self.height(root.right)
        if(balance>1 and data<root.left.data):
            return self.rightrotation(root)
        if(balance>1 and data>root.left.data):
            root.left=self.leftrotation(root.left)
            return self.rightrotation(root)
        if(balance<-1 and data>root.right.data):
            return self.leftrotation(root)
        if(balance<-1 and data<root.right.data):
            root.right=self.rightrotation(root.right)
            return self.leftrotation(root)
        return root
                
AVL1=AVLBST()
root=None
root=AVL1.insertion(90,root) 
root=AVL1.insertion(76,root)
root=AVL1.insertion(43,root)
root=AVL1.insertion(23,root) 
root=AVL1.deletion(root,23)
AVL1.inorder(root)

                    
                
