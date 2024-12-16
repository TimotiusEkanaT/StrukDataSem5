def expandExternal(self, value):
    node = self.binarySearch(self._root, value)
    if node is not None and node.isExternal():
        node.insert(node.operator()-1)
        node.insert(node.operator()+1)
        self._size+=2
def removeAboveExternal(self, value):
    node = self.binarySearch(self._root, value)
    if node is not None:
        sibling = node.parent().left() if node == node.parent().right() else node.parent().14 if node.parent() == self._root:
        self._root = sibling
        sibling.setParent(None)
    else:
        if node.parent() == node.parent().parent().left():
            node.parent().parent().setLeft(sibling)
        else:
            node.parent().parent().setRight(sibling)
            self._size-=2
