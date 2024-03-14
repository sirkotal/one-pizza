from dataclasses import dataclass

@dataclass
class Customer:
    likes: set[str]
    dislikes: set[str]
