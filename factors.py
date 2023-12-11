import sympy
import sys

def factorize(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()
        for number in numbers:
            n = int(number.strip())
            factors = sympy.factorint(n)
            p, q = factors.keys()
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize(file_path)
