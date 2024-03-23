class Pizza:
    def __init__(self, customers, ingredients):
        self.customers = customers
        self.ingredients = ingredients
        self.solution = set()
        self.score = 0

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self
