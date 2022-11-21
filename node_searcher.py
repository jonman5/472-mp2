from typing import Type

from helper.heuristic_helper import *
from model.node import Node
from model.prioritized_node import PrioritizedNode
from move_finder import MoveFinder
from queue import PriorityQueue


class NodeSearcher(object):
    open_list: Type[PriorityQueue]

    def __init__(self, algo, heuristic_to_use=0):
        self.open_list = PriorityQueue()
        self.closed_list = []
        self.heuristic_used = heuristic_to_use
        self.algorithm = algo

    def execute_search(self, initial_node: Node, heuristic_to_use=None):
        match self.algorithm:
            case "UCS":
                self.open_list = PriorityQueue()
                return self.__uniform_cost_search(initial_node)
            case "GBFS":
                self.open_list = PriorityQueue()
                return self.__greedy_best_first_search(initial_node, heuristic_to_use)
            case "A/A*":
                self.open_list = PriorityQueue()
                pass

    def __uniform_cost_search(self, initial_state: Node) -> Node:
        self.open_list.put(PrioritizedNode(initial_state.get_depth(), initial_state))
        self.closed_list = []
        while not self.open_list.empty():
            node_to_search: Node = self.open_list.get().node
            if node_to_search.get_is_goal():
                return node_to_search
            self.closed_list.append(node_to_search)
            possible_moves = MoveFinder.find_moves(node_to_search.get_state())
            successors = []
            for move in possible_moves:
                successors.append(Node(move, node_to_search))
            for successor in successors:
                visited = False
                for node in self.closed_list:
                    if successor.get_state() == node.get_state():
                        visited = True
                        break
                if not visited:
                    successor_inserted = False
                    for item in self.open_list.queue:
                        if successor.get_state() == item.node.get_state():
                            if successor.get_depth() < node.get_depth():
                                self.__swap_nodes(node, successor)
                                successor_inserted = True
                                break
                    if not successor_inserted:
                        self.open_list.put(PrioritizedNode(successor.get_depth(), successor))
        return None

    def __greedy_best_first_search(self, initial_state: Node, heuristic_to_use) -> Node:
        self.open_list.put(PrioritizedNode(calculate_heuristic(heuristic_to_use, initial_state), initial_state))
        self.closed_list = []
        while not self.open_list.empty():
            node_to_search: Node = self.open_list.get().node
            if node_to_search.get_is_goal():
                return node_to_search
            self.closed_list.append(node_to_search)
            possible_moves = MoveFinder.find_moves(node_to_search.get_state())
            successors = []
            for move in possible_moves:
                successors.append(Node(move, node_to_search))
            for successor in successors:
                visited = False
                for node in self.closed_list:
                    if successor.get_state() == node.get_state():
                        visited = True
                        break
                if not visited:
                    self.open_list.put(PrioritizedNode(calculate_heuristic(heuristic_to_use, initial_state), successor))
        return None

    def __swap_nodes(self, old_node: Node, new_node: Node):
        popped = []
        while True:
            item: PrioritizedNode = self.open_list.get()
            if item.node == old_node:
                break
            popped.append(item)
        for item in popped:
            self.open_list.put(item)
        self.open_list.put(PrioritizedNode(new_node.get_depth(), new_node))
