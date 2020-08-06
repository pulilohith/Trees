class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=self.parent=None 
        self.color=1 
class RED_Black:
    def __init__(self):
        self.TNil=Node(0)
        self.TNil.color=0 
        self.root=self.TNil 
    def insert_fix(self,Node):
        while(Node.parent.color==1):
            if(Node.parent.parent.left==Node.parent):
                uncle=Node.parent.parent.right
                if(uncle.color==1):
                    Node.parent.color=0 
                    uncle.color=0 
                    Node.parent.parent.color=1 
                    Node=Node.parent.parent
                else:
                    if(Node.parent.right==Node):
                        Node=Node.parent
                        self.leftrotation(Node)
                    k.parent.color=0 
                    k.parent.parent.color=1 
                    self.rightrotation(Node.parent.parent)
            else:
                uncle=Node.parent.parent.left
                if(uncle==1):
                    Node.parent.color=0 
                    uncle.color=0 
                    Node.parent.parent.color=1 
                    Node=Node.parent.parent
                else:
                    if(Node.parent.left==Node):
                        Node=Node.parent
                        self.rightrotation(Node)
                    Node.parent.color=0 
                    Node.parent.parent.color=1 
                    self.leftrotation(Node.parent.parent)
            if(Node==self.root):
                break
        self.root.color=0  
    def leftrotation(self,x):
        y=x.right
        x.right=y.left 
        if(y.left!=self.TNil): 
            y.left.parent=x
        y.parent=x.parent
        if(y.parent==None):
            self.root=y 
        elif(y.parent.left==x):
            y.parent.left=y  
        else:
            y.parent.right=y 
        y.left=x 
        x.parent=y
        return y  
    def rightrotation(self,x):
        y=x.left
        x.left=y.right
        if(y.right!=self.TNil):
            y.right.parent=x 
        y.parent=x.parent
        if(y.parent==None):
            self.root=y 
        elif(y.parent.left==x):
            y.parent.left=y  
        else:
            y.parent.right=y 
        y.right=x 
        x.parent=y  
        return y
    def insertion(self,root,data):
        N1=Node(data)
        N1.left=self.TNil
        N1.right=self.TNil
        x=None
        y=root
        while(y!=self.TNil):  
            x=y
            if(data<y.data):
                y=y.left
            else:
                y=y.right
        N1.parent=x 
     
        if(x==None):
            self.root=N1
        elif(x.data<data):
            x.right=N1
        else:
            x.left=N1
        if(N1.parent==None):
            N1.color=0 
            return 
        elif(N1.parent.parent==None):
            return 
        self.insert_fix(N1) 
    def inorder(self,root):
        if(root==self.TNil):
            return 
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
            
Re1=RED_Black()
Re1.insertion(Re1.root,89)
Re1.insertion(Re1.root,97)
Re1.insertion(Re1.root,78)
Re1.insertion(Re1.root,67)
Re1.inorder(Re1.root)

            
        
