from dataclasses import dataclass, field
from model.node import Node


@dataclass(order=True)
class PrioritizedNode:
    priority: int
    node: Node = field(compare=False)
