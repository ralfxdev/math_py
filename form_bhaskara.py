import math

def bhaskara(a, b, c):
    """Calculates the roots of a quadratic equation using the Bhaskara formula.

    Args:
        a (float): Coefficient of the quadratic term.
        b (float): Coefficient of the linear term.
        c (float): Constant term.

    Returns:
        tuple: A tuple containing the roots of the quadratic equation. 
            If the roots are real and distinct, returns a tuple of two real roots.
            If the roots are real and equal, returns a tuple containing a single real root.
            If the roots are complex, returns a tuple of two complex roots.
    """
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    """Main function of the program."""
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    roots = bhaskara(a, b, c)

    if len(roots) == 2:
        print("The roots of the equation are:", roots[0], "and", roots[1])
    elif len(roots) == 1:
        print("The equation has a double root:", roots[0])
    else:
        print("The roots of the equation are complex:", roots[0], "and", roots[1])

if __name__ == "__main__":
    main()
