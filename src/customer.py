from dataclasses import dataclass

@dataclass
class Customer:
    """
    Class to represent a customer with liked and disliked ingredients

    likes : set[str]
        Set of ingredients that the customer likes
    dislikes : set[str]
        Set of ingredients that the customer dislikes
    likes_bitstring : int
        Bitstring representation of the ingredients that the customer likes
    dislikes_bitstring : int
        Bitstring representation of the ingredients that the customer dislikes
    """
    likes: set[str]
    dislikes: set[str]
    likes_bitstring: int = 0
    dislikes_bitstring: int = 0
