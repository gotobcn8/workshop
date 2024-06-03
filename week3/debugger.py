import pdb

GNAME = 15


def subtract(a, b):
    """
    This is a function a excute a - b
    """
    return a - b


def main():
    x = 10
    y = 20
    pdb.set_trace()
    result = subtract(x, y)
    print(f"Result: {result}")


if __name__ == "__main__":

    pdb.run("main()")
