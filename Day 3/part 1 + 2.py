with open("data.txt", "r") as f:
    slope = f.readlines()


def TreeCount(right, down):
    trees = 0
    for i in range(0, len(slope), down):
        if slope[i][right * i % len(slope[i].strip())] == "#":
            trees += 1
    return trees


# Answer Part 1
print({TreeCount(3, 1)})
# Answer Part 2
print({TreeCount(1, 2) * TreeCount(3, 1) * TreeCount(5, 1)
       * TreeCount(7, 1) * TreeCount(1, 2)})
