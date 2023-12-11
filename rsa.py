import sympy
import sys

def rsa_factorize(number):
    factors = sympy.factorint(number)
    p, q = factors.keys()
    print(f"{number}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        number = int(file.read().strip())
        rsa_factorize(number)
