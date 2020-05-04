from cube import reverse_algorithm
import random


# Algorithms
corner_swapper = "R U' R' U' R U R' F' R U R' U' R' F R".split()
corner_rotater = "U B U' F2 U B' U' F2 D B2 D' F2 D B2 D' F2".split()


# Solves all corners for cube
def solve_corners(cube):
    # Solves all corner into correct position
    while check_corners_position(cube) is False:
        if check_buffer_solved(cube) is True:
            move_unsolved_corner_to_buffer(cube)
        else:
            solve_buffer(cube)

    # Rotates all corners into correct orientation
    while check_corners_position_and_orientation(cube) is False:
        rotate_corner(cube)


# Checks if all edges in cube is in right position
def check_corners_position(cube):
    solved = 0
    for piece in cube.pieces:
        if piece.pos.count(0) == 0 and piece.pos == piece.solved_pos:
            solved += 1
    if solved == 8:
        return True
    else:
        return False


# Checks if all corners in cube is in right position and right orientation
def check_corners_position_and_orientation(cube):
    solved = 0
    for piece in cube.pieces:
        if piece.pos.count(0) == 0 and piece.pos == piece.solved_pos and piece.col == piece.solved_col:
            solved += 1
    if solved == 8:
        return True
    else:
        return False


# Gets the moves required to move a corner piece into the buffer position.
def get_path_to_buffer(piece):
    # Top layer
    if piece.pos == [-1, 1, -1]:
        return "L' D2 L".split()
    if piece.pos == [1, 1, -1]:
        return "R2".split()
    if piece.pos == [1, 1, 1]:
        return "R'".split()
    if piece.pos == [-1, 1, 1]:
        return "F2".split()

    # Bottom layer
    if piece.pos == [-1, -1, -1]:
        return "D2".split()
    if piece.pos == [1, -1, -1]:
        return "D'".split()
    if piece.pos == [1, -1, 1]:
        return "D2 D2".split()
    if piece.pos == [-1, -1, 1]:
        return "D".split()


# Moves a random corner piece into buffer position
def move_unsolved_corner_to_buffer(cube):
    unsolved = []
    for piece in cube.pieces:
        if piece.pos != piece.solved_pos and piece.pos.count(0) == 0:
            unsolved.append(piece)

    if len(unsolved) > 1:
        for piece in unsolved:
            if piece.solved_pos == [-1, 1, -1]:
                unsolved.remove(piece)

    piece_to_move = random.choice(unsolved)
    path = get_path_to_buffer(piece_to_move)

    for move in path:
        cube.turn(move)
    for move in corner_swapper:
        cube.turn(move)
    # TODO: Corner rotating bør gjøres her for å korte ned løsningen
    for move in reverse_algorithm(path):
        cube.turn(move)


# Checks if the corner in the buffer position is solved
def check_buffer_solved(cube):
    solved = False
    for piece in cube.pieces:
        if piece.pos == [-1, 1, -1] and piece.pos == piece.solved_pos:
            solved = True
    return solved


# Moves the corner piece in the buffer position to its solved position
def solve_buffer(cube):
    position_to_swap = None
    piece_to_swap = None
    for piece in cube.pieces:
        if piece.pos == [-1, 1, -1]:
            position_to_swap = piece.solved_pos
    for piece in cube.pieces:
        if piece.pos == position_to_swap:
            piece_to_swap = piece

    path = get_path_to_buffer(piece_to_swap)

    for move in path:
        cube.turn(move)
    for move in corner_swapper:
        cube.turn(move)
    for move in reverse_algorithm(path):
        cube.turn(move)


# Rotates a random corner piece if it is in the right position but not the right orientation.
def rotate_corner(cube):
    corners_to_rotate = []
    for piece in cube.pieces:
        if piece.pos == piece.solved_pos and piece.col != piece.solved_col and piece.pos.count(0) == 0:
            corners_to_rotate.append(piece)

    corner_to_rotate = random.choice(corners_to_rotate)
    path = get_path_to_buffer(corner_to_rotate)

    for move in path:
        cube.turn(move)
    for move in corner_rotater:
        cube.turn(move)
    for move in reverse_algorithm(path):
        cube.turn(move)
