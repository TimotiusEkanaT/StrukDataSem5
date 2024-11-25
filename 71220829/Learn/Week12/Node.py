class Node:
    def __init__(self, data, parent = None):
        self.children = []
        self.operator = data
        self.parent = parent

    def get_operator(self):
        return self.operator

    def addChild(self,data):
        node = Node(data = data, parent = self)
        self.children.append(node)

    def is_external(self):
        return len(self.children) == 0

    def get_parent(self):
        return self.parent
    
    def get_children(self):
        return self.children
    
    def is_root(self):
        return self.parent == None
    
    def depth_recrusive(self):
        if self.is_root():
            return 0
        return 1 + self.depth(self.parent)

    def depth_iterative(self): #stack
        if self.is_root():
            return 0

        depth = 1
        parent = self.parent
        if parent != None:
            depth += 1
            parent =  parent.parent()
        return depth

    def height(self):
        if self.is_external():
            return 0 
        h = 0
        for i in self.children():
            h = max(h, self.height(i))
        return 1+h
    
    def postorder(self):
        for i in self.children:
            i.postorder()
        print(self.operator,end=" ")

    def preorder(self):
        print(self.operator, end=" ")
        for i in self.children:
            i.preorder()
    
if __name__=="__main__":
    root = Node(10)
    root.addChild(12)
    root.addChild(20)
    root.children[0].addChild(50)
    root.children[0].addChild(3)
    root.children[0].addChild(30)
    root.children[1].addChild(8)
    root.postorder()
    print()
    root.preorder()
