class Customer:
    def __init__(self, likes, dislikes):
        self.likes = set(likes)
        self.dislikes = set(dislikes)