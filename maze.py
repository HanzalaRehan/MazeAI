"""
Author(s):  1. Hanzala B. Rehan
            2. Amna Akhtar Nawabi
            3. Abdullah Janjua
Description: This script defines a class `Maze` which generates a random,
            solvable maze using Depth-First Search (DFS) algorithm.
Date created: November 15th, 2024
Date last modified: November 18th, 2024
"""


import random
from util import Node


class Maze:
    # Constructor to initialize the maze with given rows and columns.
    def __init__(self, rows, cols):
        """
        Desc: Initializes the maze with the specified number of rows and columns.
        Parameters:
            rows (int): Number of rows in the maze.
            cols (int): Number of columns in the maze.
        """
        self.goal = None
        self.start = None
        self.rows = rows  # Number of rows in the maze
        self.cols = cols  # Number of columns in the maze
        self.maze = self.generate_solvable_maze()  # Generates a solvable maze upon initialization

    def generate_solvable_maze(self):
        """
        Desc: Generates a solvable maze using Depth-First Search (DFS) algorithm.
        returns:
        (list): A 2D list representing the maze layout with 'S' as the start, 'G' as the goal,
                and '#' as the walls.
        """
        # Initialize maze with walls ('#')
        maze = [['#' for _ in range(self.cols)] for _ in range(self.rows)]

        # Randomly select a starting point ('S')
        start_row, start_col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        maze[start_row][start_col] = 'S'  # Set the start point on the maze
        self.start = (start_row, start_col)

        # Stack to perform DFS for maze generation
        stack = [(start_row, start_col)]

        # Directions to move in the maze: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # DFS to carve paths in the maze
        while stack:
            r, c = stack.pop()

            # Shuffle directions to randomize the maze creation
            random.shuffle(directions)
            for dr, dc in directions:
                # Calculate the new row and column two steps ahead (to carve a path)
                nr, nc = r + dr * 2, c + dc * 2

                # Check if the new position is within bounds and is a wall ('#')
                if 0 <= nr < self.rows and 0 <= nc < self.cols and maze[nr][nc] == '#':
                    maze[r + dr][c + dc] = ' '  # Open the path between cells
                    maze[nr][nc] = ' '  # Open the next cell
                    stack.append((nr, nc))  # Add the new position to the stack for further exploration

        # Place the goal point ('G') in a random open space
        goal_row, goal_col = start_row, start_col
        # Ensure goal is not placed at the start and is on an open space
        while (goal_row, goal_col) == (start_row, start_col) or maze[goal_row][goal_col] == '#':
            goal_row, goal_col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        maze[goal_row][goal_col] = 'G'  # Set the goal point
        self.goal = (goal_row, goal_col)

        return maze  # Return the generated maze

    def print_maze(self):
        """
        Desc: Prints the maze in a visually clear format.
        """
        for row in self.maze:
            print("".join(row))  # Join each row list and print as a string

    def get_maze(self):
        """
        Desc: Returns the maze layout.
        returns:
        (list): The maze as a 2D list.
        """
        return self.maze

    def get_goal(self):
        """
        Desc: Returns the maze layout.
        returns:
        (tuple): x, y coordinates of the goal
        """
        return self.goal

    def is_goal(self, node):
        """
        Desc: Returns the maze layout.
        Parameters:
            node (Node): the node to check
        returns:
        (bool): True if node is at goal.
        """
        if node.state == self.goal:
            return True
        return False

    def get_next(self, node):
        """
        Desc: Returns the next nodes available through legal moves
        Parameters:
            node (Node): the node to check
        returns:
        (list): A list of tuples representing the next valid states and actions.
                Each tuple contains (action, next_state), where:
                    action (str): The move direction ('left', 'right', 'up', 'down').
                    next_state (tuple): The (row, col) coordinates of the next position.
        """
        # Define possible moves and their corresponding actions
        moves = {
            'left': (0, -1),
            'right': (0, 1),
            'up': (-1, 0),
            'down': (1, 0)
        }

        next_nodes = []  # List to store valid next nodes

        for action, (dr, dc) in moves.items():
            next_row, next_col = node.state[0] + dr, node.state[1] + dc

            # Check if the next move is within bounds and not hitting a wall
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols and self.maze[next_row][next_col] != '#':
                next_nodes.append((action, (next_row, next_col)))  # Add valid move

        return next_nodes  # Return all valid moves
