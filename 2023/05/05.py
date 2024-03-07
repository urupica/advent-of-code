

def main1():
    sources = None
    destinations = None
    with open("sample.txt") as input_file:
        for row in input_file:
            row = row.strip()
            if row.startswith("seeds:"):
                row = row.replace("seeds:", "")
                sources = list(map(int, row.split()))
                destinations = []
            elif row.endswith("map:"):
                sources, destinations = destinations, sources
            elif row:
                destination_start, source_start, length = map(int, row.split())
                sources_copy = list(sources)
                for item in sources_copy:
                    if source_start <= item < source_start + length:
                        sources.remove(item)
                        destinations.append(destination_start + item - source_start)
            else:
                destinations.extend(sources)
                sources = []
    sources.extend(destinations)
    print(min(sources))


def main2():
    sources = None
    destinations = None
    with open("input.txt") as input_file:
        for row in input_file:
            row = row.strip()
            if row.startswith("seeds:"):
                row = row.replace("seeds:", "")
                sources = []
                destinations = []
                ranges = list(map(int, row.split()))
                for i in range(len(ranges) // 2):
                    start, length = ranges[2 * i], ranges[2 * i + 1]
                    sources.append((start, length))
            elif row.endswith("map:"):
                sources, destinations = destinations, sources
            elif row:
                destination_start, source_start, length = map(int, row.split())
                sources_copy = list(sources)
                for item_start, item_length in sources_copy:
                    a, b = item_start, item_start + item_length - 1
                    c, d = source_start, source_start + length - 1
                    if a <= d and b >= c:
                        sources.remove((a, b - a + 1))
                        if a < c:
                            sources.append((a, c - a))
                        if b > d:
                            sources.append((d + 1, b - d))
                        destinations.append((max(a, c) + destination_start - source_start, min(b, d) - max(a, c) + 1))
            else:
                destinations.extend(sources)
                sources = []
    sources.extend(destinations)
    print(min(source[0] for source in sources))


if __name__ == "__main__":
    main2()
