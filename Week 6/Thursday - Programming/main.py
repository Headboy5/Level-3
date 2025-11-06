def solve_crossmath():
    solutions = []

    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c in (a, b):
                    continue
                for d in range(1, 10):
                    if d in (a, b, c):
                        continue
                    for e in range(1, 10):
                        if e in (a, b, c, d):
                            continue
                        for f in range(1, 10):
                            if f in (a, b, c, d, e):
                                continue
                            for g in range(1, 10):
                                if g in (a, b, c, d, e, f):
                                    continue
                                for h in range(1, 10):
                                    if h in (a, b, c, d, e, f, g):
                                        continue
                                    for i in range(1, 10):
                                        if i in (a, b, c, d, e, f, g, h):
                                            continue
                                        # compute expression using floats
                                        expr = a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10
                                        if abs(expr - 66) < 1e-12:
                                            solutions.append((a, b, c, d, e, f, g, h, i))

    if solutions:
        print(f"Found {len(solutions)} solution(s):")
        for sol in solutions:
            a, b, c, d, e, f, g, h, i = sol
            print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, i={i}")
    else:
        print("No solution found.")

    return solutions

def main():
    # Run the solver and exit. solve_crossmath prints the result.
    solve_crossmath()


if __name__ == "__main__":
    main()