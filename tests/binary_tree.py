class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None


    def __find(self, node, parent, value):
        if node is None:
            return None, parent, value

        if value == node.data:
            return node, parent, value

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False # узел, к которому добавляем новый узел, родительский узел, False

    def my_append(self, obj: Node):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node: Node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.right = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)

        if s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


# v = [10, 5, 7, 16, 13, 2, 20]
v = [1,2,2,3,4,4,3]
t = Tree()

for x in v:
    t.my_append(Node(x))

t.show_tree(t.root)

# t.del_node(5)

t.show_tree(t.root)

t.show_wide_tree(t.root)
