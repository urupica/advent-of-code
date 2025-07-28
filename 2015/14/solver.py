import re


def simulate_1(reindeer, total_seconds):
    best = 0
    for name, fly_speed, fly_time, rest_time in reindeer:
        total = 0
        seconds = 0
        is_flying = True
        while seconds < total_seconds:
            if is_flying:
                total += min(fly_time, total_seconds - seconds) * fly_speed
                seconds += fly_time
            else:
                seconds += rest_time
            is_flying = not is_flying
        best = max(best, total)
    return best


def simulate_2(reindeer, total_seconds):
    reindeer_names = [name for name, *_ in reindeer]
    points = {name: 0 for name in reindeer_names}
    total_distance = {name: 0 for name in reindeer_names}
    flown = {name: 0 for name in reindeer_names}
    rested = {name: 0 for name in reindeer_names}
    currently_flying = {name: True for name in reindeer_names}
    for _ in range(total_seconds):
        for name, fly_speed, fly_time, rest_time in reindeer:
            if currently_flying[name]:
                flown[name] += 1
                total_distance[name] += fly_speed
                if flown[name] == fly_time:
                    flown[name] = 0
                    currently_flying[name] = False
            else:
                rested[name] += 1
                if rested[name] == rest_time:
                    rested[name] = 0
                    currently_flying[name] = True
        max_total_distance = max(total_distance.values())
        for name in reindeer_names:
            if total_distance[name] == max_total_distance:
                points[name] += 1
    return max(points.values())


def solve(filename):
    reindeer = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            pattern = r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\."
            result = re.match(pattern, line)
            name, fly_speed, fly_time, rest_time = result.groups()
            reindeer.append((name, int(fly_speed), int(fly_time), int(rest_time)))

    result_part_1 = simulate_1(reindeer, 1000 if filename == "sample.txt" else 2503)
    print(f"part 1: {result_part_1}")

    result_part_2 = simulate_2(reindeer, 1000 if filename == "sample.txt" else 2503)
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
