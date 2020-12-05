data = open("data.txt", "r").read().splitlines()
# tidying things up a bit from pt1
ln = len(data)
target = 2020
# turn the list of strings into a list of ints
for i in range(ln):
    data[i] = int(data[i])


for i in range(ln):
    for j in range(ln):
        for m in range(ln):

            if i != j and data[i]+data[j]+data[m] == target:
                print(data[i]*data[j]*data[m])
