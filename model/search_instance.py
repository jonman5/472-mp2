import string

from model.game_board import GameBoard
from model.node import Node


class SearchInstance(object):
    algorithm: string
    heuristic: string
    execution_time: int
    search_path: list[Node]
    solution_path: list[Node]
    initial_state: GameBoard
    solved_state: GameBoard
    puzzle_number: int

    def __init__(self, algo, heuristic):
        self.algorithm = algo
        self.heuristic = heuristic
        self.execution_time = 0
        self.search_path = []
        self.solution_path = []
        self.initial_state = None
        self.solved_state = None
        self.puzzle_number = 0
