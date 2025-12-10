from heapq import heappush, heappop
from ortools.linear_solver import pywraplp
import numpy as np


def get_neighbors(lights, buttons):
    for button in buttons:
        yield tuple(((n + 1) % 2) if i in button else n for i, n in enumerate(lights))


def dijkstra(buttons, target):
    start = (0,) * len(target)
    dist = {start: 0}
    visited = set()
    heap = []
    heappush(heap, (0, start))
    while heap:
        dv, v = heappop(heap)
        if v == target:
            return dv

        if v in visited:
            continue
        visited.add(v)

        for w in get_neighbors(v, buttons):
            dw = dv + 1
            if w not in visited and (w not in dist or dw < dist[w]):
                dist[w] = dw
                heappush(heap, (dw, w))


def solve_min_sum_system(A, b):
    """
    Solves min sum(x) subject to Ax = b using Google OR-Tools.
    """
    solver = pywraplp.Solver.CreateSolver('SCIP')

    n_rows, n_cols = A.shape

    # define target variables
    x = [
        solver.IntVar(0, solver.infinity(), f'x_{j}')
        for j in range(n_cols)
    ]

    # add constraints: Ax = b
    # for each row i, sum(A[i][j] * x[j]) == b[i]
    for i in range(n_rows):
        # optimization: skip zero entries
        constraint_expr = sum(z for j, z in enumerate(x) if A[i][j] == 1)

        # add equality constraint
        solver.Add(constraint_expr == b[i])

    solver.Minimize(sum(x))

    status = solver.Solve()

    # assume we always find an optimal solution
    assert status == pywraplp.Solver.OPTIMAL
    return int(sum(z.solution_value() for z in x))




def solve(filename):
    configurations = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            i = line.index("]")
            lights = tuple(0 if x == "." else 1 for x in line[1:i])
            j = line.index("{")
            buttons = []
            for part in line[i + 2:j - 1].split():
                button = tuple(map(int, part[1:-1].split(",")))
                buttons.append(button)
            joltage = tuple(map(int, line[j + 1:-1].split(",")))
            configurations.append((lights, buttons, joltage))


    result_part_1 = sum(dijkstra(buttons, lights) for lights, buttons, _ in configurations)
    print(f"part 1: {result_part_1}")

    result_part_2 = 0
    for n, (_, buttons, joltage) in enumerate(configurations):
        matrix = [[0] * len(buttons) for _ in range(len(joltage))]
        for j, button in enumerate(buttons):
            for i in button:
                matrix[i][j] = 1
        matrix = np.array(matrix)
        target = np.array(joltage)
        result_part_2 += solve_min_sum_system(matrix, target)

    print(f"part 2: {result_part_2}")


def main():
    for filename in [
        "sample.txt",
        "input.txt"
    ]:
        print(f"-- {filename} --")
        solve(filename)


if __name__ == "__main__":
    main()
