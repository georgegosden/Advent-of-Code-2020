data = open("data.txt", "r").read().splitlines()
# turn the list of strings into a list of ints
for i in range(len(data)):
    data[i] = int(data[i])
target = 2020
for i in range(len(data)):
    for j in range(len(data)):
        if i != j and data[i]+data[j] == target:
            print(data[i]*data[j])
