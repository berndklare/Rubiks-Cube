from copy import deepcopy


class Piece:
    def __init__(self, position):
        # Pieces position given in coordinates [x, y, z]
        self.pos = position

        # Pieces colors are all set to "."
        # [U, D, F, B, R, L]
        self.col = ["." for n in range(6)]

        # Sets the color orientation of a piece based on its starting position in the cube.
        if self.pos[1] == 1:
            self.col[0] = "W"
        if self.pos[1] == -1:
            self.col[1] = "Y"
        if self.pos[2] == 1:
            self.col[2] = "G"
        if self.pos[2] == -1:
            self.col[3] = "B"
        if self.pos[0] == 1:
            self.col[4] = "R"
        if self.pos[0] == -1:
            self.col[5] = "O"

        # Saves the pieces initial solved position and color orientation.
        self.solved_pos = deepcopy(self.pos)
        self.solved_col = deepcopy(self.col)

    def rotate(self, axis):
        # Rotates both the the position and color orientation for the piece.
        # Rotation of position is always clockwise. This is done by multiplying with the axis' own coordinate.

        if axis == "x":
            if self.pos[0] == 1:
                self.col[0], self.col[1], self.col[2], self.col[3] = self.col[2], self.col[3], self.col[1], self.col[0]
            elif self.pos[0] == -1:
                self.col[0], self.col[1], self.col[2], self.col[3] = self.col[3], self.col[2], self.col[0], self.col[1]
            self.pos[1], self.pos[2] = self.pos[2] * self.pos[0], -self.pos[1] * self.pos[0]

        if axis == "y":
            if self.pos[1] == 1:
                self.col[2], self.col[3], self.col[4], self.col[5] = self.col[4], self.col[5], self.col[3], self.col[2]
            if self.pos[1] == -1:
                self.col[2], self.col[3], self.col[4], self.col[5] = self.col[5], self.col[4], self.col[2], self.col[3]
            self.pos[0], self.pos[2] = -self.pos[2] * self.pos[1], self.pos[0] * self.pos[1]

        if axis == "z":
            if self.pos[2] == 1:
                self.col[0], self.col[1], self.col[4], self.col[5] = self.col[5], self.col[4], self.col[0], self.col[1]
            if self.pos[2] == -1:
                self.col[0], self.col[1], self.col[4], self.col[5] = self.col[4], self.col[5], self.col[1], self.col[0]
            self.pos[0], self.pos[1] = self.pos[1] * self.pos[2], -self.pos[0] * self.pos[2]


class Cube:
    def __init__(self):
        # Create a piece for every x, y, z coordinate from -1 to 1.
        self.pieces = \
            [Piece(elem) for elem in [[x, y, z] for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)]]

        # Counter for how many times the function turn() has been called
        self.turns = 0

        # Variable for saving the scramble used in the function scramble_cube.
        self.scramble = []

        # Saves every move done in the function turn.
        self.moves_done = []

    def turn(self, move):
        # Set face to be turned, and times to be turned
        face = move[0]
        times = 1

        # Set number of turns. Anti-clockwise/inverted turns is done by 3 clockwise turns.
        if len(move) == 2:
            if move[1] in "'iI":
                times = 3
            if move[1] in "123":
                times = int(move[1])

        # Make safe for lower case moves
        face = face.capitalize()

        # Check if valid turn
        if face in "FBUDLR":
            if times in [1, 2, 3]:
                # Increase turn counter if move is valid
                self.turns += 1

                # Saves the move.
                self.moves_done.append(move)

                # Turns all the pieces in a face clockwise around the given axis.
                # TODO: Kan gjøres enklere
                if face == "R":
                    for piece in self.pieces:
                        if piece.pos[0] == 1:
                            for n in range(times):
                                piece.rotate("x")

                if face == "L":
                    for piece in self.pieces:
                        if piece.pos[0] == -1:
                            for n in range(times):
                                piece.rotate("x")

                if face == "U":
                    for piece in self.pieces:
                        if piece.pos[1] == 1:
                            for n in range(times):
                                piece.rotate("y")

                if face == "D":
                    for piece in self.pieces:
                        if piece.pos[1] == -1:
                            for n in range(times):
                                piece.rotate("y")

                if face == "F":
                    for piece in self.pieces:
                        if piece.pos[2] == 1:
                            for n in range(times):
                                piece.rotate("z")

                if face == "B":
                    for piece in self.pieces:
                        if piece.pos[2] == -1:
                            for n in range(times):
                                piece.rotate("z")

    # Returns the color of a pieces side. Used for printing the cube.
    # TODO: Kan forenkles.
    def get_color(self, coordinates, side):
        for piece in self.pieces:
            if piece.pos == coordinates:
                if piece.col[side] is None:
                    return "?"
                else:
                    return piece.col[side]

    # Prints the cube
    def __str__(self):
        string = f"""
           {self.get_color([-1, 1, -1], 0)}  {self.get_color([0, 1, -1], 0)}  {self.get_color([1, 1, -1], 0)}
           {self.get_color([-1, 1, 0], 0)}  {self.get_color([0, 1, 0], 0)}  {self.get_color([1, 1, 0], 0)}
           {self.get_color([-1, 1, 1], 0)}  {self.get_color([0, 1, 1], 0)}  {self.get_color([1, 1, 1], 0)}\n
{self.get_color([-1, 1, -1], 5)}  {self.get_color([-1, 1, 0], 5)}  {self.get_color([-1, 1, 1], 5)}    \
{self.get_color([-1, 1, 1], 2)}  {self.get_color([0, 1, 1], 2)}  {self.get_color([1, 1, 1], 2)}    \
{self.get_color([1, 1, 1], 4)}  {self.get_color([1, 1, 0], 4)}  {self.get_color([1, 1, -1], 4)}    \
{self.get_color([1, 1, -1], 3)}  {self.get_color([0, 1, -1], 3)}  {self.get_color([-1, 1, -1], 3)}
{self.get_color([-1, 0, -1], 5)}  {self.get_color([-1, 0, 0], 5)}  {self.get_color([-1, 0, 1], 5)}    \
{self.get_color([-1, 0, 1], 2)}  {self.get_color([0, 0, 1], 2)}  {self.get_color([1, 0, 1], 2)}    \
{self.get_color([1, 0, 1], 4)}  {self.get_color([1, 0, 0], 4)}  {self.get_color([1, 0, -1], 4)}    \
{self.get_color([1, 0, -1], 3)}  {self.get_color([0, 0, -1], 3)}  {self.get_color([-1, 0, -1], 3)}
{self.get_color([-1, -1, -1], 5)}  {self.get_color([-1, -1, 0], 5)}  {self.get_color([-1, -1, 1], 5)}    \
{self.get_color([-1, -1, 1], 2)}  {self.get_color([0, -1, 1], 2)}  {self.get_color([1, -1, 1], 2)}    \
{self.get_color([1, -1, 1], 4)}  {self.get_color([1, -1, 0], 4)}  {self.get_color([1, -1, -1], 4)}    \
{self.get_color([1, -1, -1], 3)}  {self.get_color([0, -1, -1], 3)}  {self.get_color([-1, -1, -1], 3)}\n
           {self.get_color([-1, -1, 1], 1)}  {self.get_color([0, -1, 1], 1)}  {self.get_color([1, -1, 1], 1)}
           {self.get_color([-1, -1, 0], 1)}  {self.get_color([0, -1, 0], 1)}  {self.get_color([1, -1, 0], 1)}
           {self.get_color([-1, -1, -1], 1)}  {self.get_color([0, -1, -1], 1)}  {self.get_color([1, -1, -1], 1)}
        """
        return string

    # Scrambles the cube
    def scramble_cube(self, scramble):
        for move in scramble:
            self.turn(move)
        self.turns = 0
        self.scramble = self.moves_done
        self.moves_done = []


# Reverses any valid series of move so that the outputted algorithm will reverse the cube back to its original state.
def reverse_algorithm(algorithm):
    new_alg = []
    for move in reversed(algorithm):
        new_move = move[0]
        if len(move) == 1:
            new_move += "'"
        if len(move) == 2:
            if move[1] == "2":
                new_move += "2"
        new_alg.append(new_move)
    return new_alg
