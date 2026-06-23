def solve_linear_equation(a, b, c):
    """
    Solves equations of the form:
    ax + b = c
    """

    print(f"Equation: {a}x + {b} = {c}")

    # Step 1
    print(f"Step 1: Move {b} to the other side")
    right_side = c - b
    print(f"{a}x = {right_side}")

    # Step 2
    print(f"Step 2: Divide both sides by {a}")
    x = right_side / a
    print(f"x = {x}")

    return x


# Example
solve_linear_equation(2, 3, 7)