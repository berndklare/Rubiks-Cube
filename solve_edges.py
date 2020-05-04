from cube import reverse_algorithm
import random


# Algorithms
edge_swapper = "R U R' U' R' F R2 U' R' U' R U R' F'".split()
edge_flipper = "R U R' B' R2 U' R' U B L2 F2 U' B2 R2 F2 D' B2 U2".split()


# Solves all edges for cube
def solve_edges(cube):
    # Solves all edges into correct position
    while check_edges_position(cube) is False:
        if check_buffer_solved(cube) is True:
            move_unsolved_edge_to_buffer(cube)
        else:
            solve_buffer(cube)

    # Flips all edges into correct oriantation
    while check_edges_position_and_orientation(cube) is False:
        flip_edge(cube)


# Checks if all edges in cube is in right position
def check_edges_position(cube):
    solved = 0
    for piece in cube.pieces:
        if piece.pos.count(0) == 1 and piece.pos == piece.solved_pos:
            solved += 1
    if solved == 12:
        return True
    else:
        return False


# Checks if all edges in cube is in right position and right orientation
def check_edges_position_and_orientation(cube):
    solved = 0
    for piece in cube.pieces:
        if piece.pos.count(0) == 1 and piece.pos == piece.solved_pos and piece.col == piece.solved_col:
            solved += 1
    if solved == 12:
        return True
    else:
        return False


# Gets the moves required to move an edge piece into the buffer position.
def get_path_to_buffer(piece):
    # Top layer
    if piece.pos == [0, 1, -1]:
        return "B2 D L2".split()
    if piece.pos == [1, 1, 0]:
        return "R2 D2 L2".split()
    if piece.pos == [0, 1, 1]:
        return "F2 D' L2".split()
    if piece.pos == [-1, 1, 0]:
        return "R2 R2".split()

    # Middle layer
    if piece.pos == [-1, 0, -1]:
        return "L".split()
    if piece.pos == [1, 0, -1]:
        return "U2 R' U2".split()
    if piece.pos == [1, 0, 1]:
        return "U2 R U2".split()
    if piece.pos == [-1, 0, 1]:
        return "L'".split()

    # Bottom layer
    if piece.pos == [0, -1, -1]:
        return "D L2".split()
    if piece.pos == [1, -1, 0]:
        return "D2 L2".split()
    if piece.pos == [0, -1, 1]:
        return "D' L2".split()
    if piece.pos == [-1, -1, 0]:
        return "L2".split()


# Moves a random edge piece into buffer position
def move_unsolved_edge_to_buffer(cube):
    unsolved = []
    for piece in cube.pieces:
        if piece.pos != piece.solved_pos and piece.pos.count(0) == 1:
            unsolved.append(piece)

    piece_to_move = random.choice(unsolved)
    path = get_path_to_buffer(piece_to_move)

    for move in path:
        cube.turn(move)
    for move in edge_swapper:
        cube.turn(move)
    # TODO: Edge flipping bør gjøres her for å korte ned løsningen
    for move in reverse_algorithm(path):
        cube.turn(move)


# Checks if the edge in the buffer position is solved
def check_buffer_solved(cube):
    solved = False
    for piece in cube.pieces:
        if piece.pos == [1, 1, 0] and piece.pos == piece.solved_pos:
            solved = True
    return solved


# Moves the edge piece in the buffer position to its solved position
def solve_buffer(cube):
    position_to_swap = None
    piece_to_swap = None
    for piece in cube.pieces:
        if piece.pos == [1, 1, 0]:
            position_to_swap = piece.solved_pos
    for piece in cube.pieces:
        if piece.pos == position_to_swap:
            piece_to_swap = piece

    path = get_path_to_buffer(piece_to_swap)

    for move in path:
        cube.turn(move)
    for move in edge_swapper:
        cube.turn(move)
    for move in reverse_algorithm(path):
        cube.turn(move)


# Flips a random edge piece if it is in the right position but not the right orientation.
def flip_edge(cube):
    edges_to_flip = []
    for piece in cube.pieces:
        if piece.pos == piece.solved_pos and piece.col != piece.solved_col and piece.pos.count(0) == 1:
            edges_to_flip.append(piece)

    edge_to_flip = random.choice(edges_to_flip)
    path = get_path_to_buffer(edge_to_flip)

    for move in path:
        cube.turn(move)
    for move in edge_flipper:
        cube.turn(move)
    for move in reverse_algorithm(path):
        cube.turn(move)
