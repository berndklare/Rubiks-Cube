from cube import Cube
from solve_edges import solve_edges
from solve_corners import solve_corners

# Change the scramble here
scramble_1 = "D R B2 F2 U2 L2 F2 R2 U B2 L2 U R2 F' L D2 R2 D2 U B U".split()


def main():
    # Creates a cube
    cube_1 = Cube()

    # Scrambles the cube
    cube_1.scramble_cube(scramble_1)

    # Prints the scrambled cube
    print(cube_1)

    # Solves the cube
    solve_edges(cube_1)
    solve_corners(cube_1)

    # Prints the solved cube
    print(cube_1)

    # Prints moves required to solve the cube from the scrambled position
    print(f"The solution consists of {cube_1.turns} moves:")
    print("Scramble: ", " ".join(cube_1.scramble))
    print("Solution: ", " ".join(cube_1.moves_done))


if __name__ == '__main__':
    main()
