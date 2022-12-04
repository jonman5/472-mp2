import curses

class ConsoleView(object):

    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.scrollok(True)
        self.stdscr.idlok(True)
        self.stdscr.syncok(True)
        curses.setupterm()

    def display_loaded_grid(self, grid, height, width):
        """Display loaded game board and wait for user response to solve the puzzle."""
        self.display_grid(grid, height, width)

        # Wait for user input
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Press any key to find solution. \n')
        self.stdscr.getch()

    def display_grid(self, grid, height, width):
        """Display the loaded game board."""
        self.stdscr.clear()

        # Display game board
        self.stdscr.addstr('The Puzzle: \n', curses.A_BOLD)
        self.stdscr.addstr('\n')
        for row in range(height):
            for column in range(width):
                vehicle = grid[row][column]
                if vehicle:
                    self.stdscr.addstr('%s ' % vehicle)
                else:
                    self.stdscr.addstr('. ')

                if column == width - 1:
                    self.stdscr.addstr('\n')
        self.stdscr.refresh()

    def load_board_prompt(self):
        """Ask the user which board to load."""
        self.stdscr.clear()
        self.stdscr.addstr('Which board do you want to use? (filename without extension ".txt") \n')
        self.stdscr.addstr('Make sure the board file is in the directory "datatxt". \n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Filename ', curses.A_BOLD)
        self.stdscr.addstr('(excl. extension ".txt"): ')
        self.stdscr.refresh()
        curses.echo()
        return self.stdscr.getstr(50).decode()

    def display_exit_message(self):
        """Display the exit message."""
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Thank you for using the rush hour solver. \n')
        self.stdscr.addstr('Press any key to exit. \n')
        self.stdscr.getch()
        curses.endwin()
