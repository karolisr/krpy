class TreeNode(object):

    def __init__(self, name, parent=None):

        self._name = name
        self._children = []
        self._parent = parent

        if parent is not None:
            parent.add_child(self)

#     def typeInfo(self):
#         return "NODE"

    def add_child(self, child):
        self._children.append(child)

#     def insertChild(self, position, child):
#
#         if position < 0 or position > len(self._children):
#             return False
#
#         self._children.insert(position, child)
#         child._parent = self
#         return True

#     def removeChild(self, position):
#
#         if position < 0 or position > len(self._children):
#             return False
#
#         child = self._children.pop(position)
#         child._parent = None
#
#         return True

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def child(self, row):
        return self._children[row]

    def children_count(self):
        return len(self._children)

    def parent(self):
        return self._parent

    def row(self):
        if self._parent is not None:
            return self._parent._children.index(self)

    def log(self, tabLevel=-1):

        output = ""
        tabLevel += 1

        for i in range(tabLevel):
            output += "\t"

        output += "|------" + self._name + "\n"

        for child in self._children:
            output += child.log(tabLevel)

        tabLevel -= 1
        output += "\n"

        return output

    def __repr__(self):
        return self.log()
