import argparse


def init_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Hanoi Tower')
    parser.add_argument('--discs', '-d', type=int, help='Quantidade de discos', required=True)
    return parser.parse_args()


def solver(n, source, aux, target):
    if n == 0:
        return
    solver(n - 1, source, target, aux)
    print(f'Move disco {n} de {source} para {target}')
    solver(n - 1, aux, source, target)


if __name__ == "__main__":
    args = init_args()
    solver(abs(args.discs), 'A', 'B', 'C')
