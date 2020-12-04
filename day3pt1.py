with open("day3.txt", "r") as f:
    slope = f.readlines()


def TreeCount(right, down):
    trees = 0
    for i in range(0, len(slope), down):
        print(i)
        if slope[i][right * i % len(slope[i].strip())] == "#":
            trees += 1
    return trees


print({TreeCount(3, 1)})
