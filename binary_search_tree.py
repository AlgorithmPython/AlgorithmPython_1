
class Node:
    def __init__(self, value): # data만 입력시 next 초기 값은 None 이다.
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def search(self, key):

