class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.children= []
        self.data = data

    def addChild(self, child):
        
        self.children.append(child)


