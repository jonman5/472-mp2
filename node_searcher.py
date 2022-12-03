from time import perf_counter
from typing import Type

from helper.heuristic_helper import *
from model.node import Node
from model.prioritized_node import PrioritizedNode
from move_finder import MoveFinder
from queue import PriorityQueue
from model.search_instance import SearchInstance


class NodeSearcher(object):
    open_list: PriorityQueue
    search: SearchInstance
    solution_node: Node

    puzzle_no = 1

    def __init__(self, algo, heuristic_to_use=0):
        self.solution_node = None
        self.open_list = PriorityQueue()
        self.closed_list = []
        self.heuristic_used = heuristic_to_use
        self.algorithm = algo
        self.search = SearchInstance(algo, heuristic_to_use)
        self.search.puzzle_number = self.puzzle_no

    def execute_search(self, initial_node: Node, heuristic_to_use=None):
        self.search.initial_state = initial_node.get_state()
        match self.algorithm:
            case "UCS":
                start_time = perf_counter()
                self.open_list = PriorityQueue()
                self.solution_node = self.__uniform_cost_search(initial_node)
                self.search.execution_time = perf_counter() - start_time

            case "GBFS":
                start_time = perf_counter()
                self.open_list = PriorityQueue()
                self.solution_node = self.__greedy_best_first_search(initial_node, heuristic_to_use)
                self.search.execution_time = perf_counter() - start_time

            case "A/A*":
                start_time = perf_counter()
                self.open_list = PriorityQueue()
                self.solution_node = self.__A_Astar_search()
                self.search.execution_time = perf_counter() - start_time
        if self.solution_node is not None:
            self.__extract_solution_path()
        return self.search
        self.puzzle_no += 1

    def __uniform_cost_search(self, initial_state: Node) -> Node:
        self.open_list.put(PrioritizedNode(initial_state.get_depth(), initial_state))
        self.closed_list = []
        while not self.open_list.empty():
            node_to_search: Node = self.open_list.get().node
            self.search.search_path.append(node_to_search)

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
                        if successor.get_state() == item.node.get_state() and successor.get_depth() < item.node.get_depth():
                            self.__swap_nodes(item.node, successor)
                            successor_inserted = True
                            break
                    if not successor_inserted:
                        self.open_list.put(PrioritizedNode(successor.get_depth(), successor))
        return None

    def __greedy_best_first_search(self, initial_state: Node, heuristic_to_use) -> Node:
        initial_state.heuristic = calculate_heuristic(heuristic_to_use, initial_state)
        self.open_list.put(PrioritizedNode(initial_state.heuristic, initial_state))
        self.closed_list = []
        while not self.open_list.empty():
            node_to_search: Node = self.open_list.get().node
            self.search.search_path.append(node_to_search)

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
                    successor.heuristic = calculate_heuristic(heuristic_to_use, successor)
                    self.open_list.put(PrioritizedNode(successor.heuristic, successor))
        return None

    def __A_Astar_search(self, initial_state: Node, heuristic_to_use) -> Node:
        initial_state.heuristic = calculate_heuristic(heuristic_to_use, initial_state)
        self.open_list.put(PrioritizedNode(initial_state.heuristic + initial_state.get_depth(), initial_state))
        self.closed_list = []

        while not self.open_list.empty():
            node_to_search: Node = self.open_list.get().node
            self.search.search_path.append(node_to_search)

            if node_to_search.get_is_goal():
                return node_to_search
            self.closed_list.append(node_to_search)

            possible_moves = MoveFinder.find_moves(node_to_search.get_state())
            successors = []
            for move in possible_moves:
                successors.append(Node(move, node_to_search))
            for successor in successors:
                successor.heuristic = calculate_heuristic(heuristic_to_use, successor)
                successor_inserted = False
                visited = False
                for node in self.closed_list:
                    if successor.get_state() == node.get_state() and (successor.heuristic + successor.get_depth()) < (node.heuristic + node.get_depth()):
                        self.closed_list.remove(node)
                        break
                    elif successor.get_state() == node.get_state():
                        visited = True
                if not visited:
                    for item in self.open_list.queue:
                        if successor.get_state() == item.node.get_state() and (successor.heuristic + successor.get_depth()) < (item.node.heuristic + item.node.get_depth()):
                            self.__swap_nodes(item.node, successor)
                            successor_inserted = True
                            break
                    if not successor_inserted:
                        self.open_list.put(PrioritizedNode(successor.heuristic + successor.get_depth(), successor))
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
        if self.algorithm == "UCS":
            self.open_list.put(PrioritizedNode(new_node.get_depth(), new_node))
        else:
            self.open_list.put(PrioritizedNode(new_node.get_depth() + new_node.heuristic, new_node))

    def __extract_solution_path(self):
        current_node = self.solution_node
        self.search.solution_path.append(current_node)
        while self.solution_node.parent_node is not None:
            self.search.solution_path.append(current_node)
        self.search.solution_path.reverse()
