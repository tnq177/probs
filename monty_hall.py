import random

random.seed(42)


def run():
    pick = random.randint(0, 2)
    car = random.randint(0, 2)

    options = set([0, 1, 2])
    options.remove(pick)
    if pick == car:
        reveal = random.choice(list(options))
    else:
        options.remove(car)
        reveal = options.pop()

    return 3 - pick - reveal == car


def main():
    N = 1000000
    change = 0
    for _ in range(N):
        change += run()

    print(f"Change wins: {change * 100/N}%")


if __name__ == "__main__":
    main()
