# Pract 9: MapReduce Weather Analysis (Large Data + File Input)

from collections import defaultdict


# ---------------------------
# MAPPER (Stream Processing)
# ---------------------------
def mapper(file_path):
    with open(file_path, "r") as f:
        for line in f:
            try:
                year, temp = line.strip().split(",")
                yield year, float(temp)
            except:
                # Skip invalid lines
                continue


# ---------------------------
# SHUFFLE (Grouping)
# ---------------------------
def shuffle_sort(mapped_data):
    grouped = defaultdict(list)
    for year, temp in mapped_data:
        grouped[year].append(temp)
    return grouped


# ---------------------------
# REDUCER
# ---------------------------
def reducer(grouped_data):
    result = {}

    for year, temps in grouped_data.items():
        total = 0
        count = 0

        for t in temps:
            total += t
            count += 1

        avg = total / count
        result[year] = round(avg, 2)

    return result


# ---------------------------
# MAIN
# ---------------------------
def main():
    file_path = "weather.txt"   # Input file

    # Step 1: Map (streaming)
    mapped = mapper(file_path)

    # Step 2: Shuffle
    grouped = shuffle_sort(mapped)

    # Step 3: Reduce
    reduced = reducer(grouped)

    print("\nAverage Temperature Per Year:")
    for year, avg in sorted(reduced.items()):
        print(year, "→", avg)

    # Find hottest & coolest
    hottest = max(reduced, key=reduced.get)
    coolest = min(reduced, key=reduced.get)

    print("\n🔥 Hottest Year:", hottest, "with", reduced[hottest])
    print("❄️ Coolest Year:", coolest, "with", reduced[coolest])


if __name__ == "__main__":
    main()