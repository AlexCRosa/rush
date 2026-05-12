import sys


def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height).

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """

    if x <= 0 or y <= 0:
        print ("Invalid size", file=sys.stderr)
        return

    for height in range(y):
        for width in range(x):
            # Check what pattern to follow
            if (x > 1 and y > 1):
                if (height == 0 and width == 0):
                    print ("/", end="")
                elif (height == 0 and width == x - 1):
                    print ("\\", end="")
                elif (height == y - 1 and width == 0):
                    print ("\\", end="")
                elif (height == y - 1 and width == x - 1):
                    print ("/", end="")
                elif height == 0 and (width != 0 or width != x - 1):
                    print ("*", end="")
                elif height > 0 and height < y - 1 and (width == 0 or width == x - 1):
                    print ("*", end="")
                elif height == y - 1 and (width != 0 or width != x - 1):
                    print ("*", end="")
                else:
                    print (" ", end="")
            else:
                print("*", end="")
        print ()


if __name__ == "__main__":
    rush(int(sys.argv[1]), int(sys.argv[2]))