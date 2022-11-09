import sys
import time
from controller.bloader import BLoader
from controller.bloader import BLoader
from view.console_v import ConsoleView


class RushHourSolver(object):
    def __init__(self):
        self.console_view = ConsoleView()
        self.run()

    def run(self):
        # Ask user which game board load
        board_name = self.console_view.load_board_prompt()
        params_name = self.console_view.load_params_prompt()

        if board_name:
            # Load game board from file
            loader = BLoader('./datatxt/%s.txt' % board_name, './datatxt/%s.txt' % params_name)
            game_board = loader.get_game_board()

            # Display game board
            self.console_view.display_loaded_grid(game_board.get_grid(), game_board.get_height(), game_board.get_width())

            """-------------TO DO.---------------------------"""

            # Find the solution to the game board
            start_time = time.perf_counter()
            solver = BLoader(game_board, self.console_view)
            # solution = solver.get_solution()
            end_time = time.perf_counter()

            # if solution:
            #     self.console_view.display_statistics(len(solution), end_time - start_time)
            # else:
            #     self.console_view.display_statistics(time_delta=end_time - start_time)
            #
            # self.console_view.display_solution(solution)

        # Exit system
        self.console_view.display_exit_message()
        sys.exit()


if __name__ == "__main__":
    RushHourSolver()

