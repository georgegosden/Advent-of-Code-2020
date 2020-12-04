puzzleObj = open("data.txt", "r")
puzzle_input = puzzleObj.read()
lines = puzzle_input.splitlines()
validCount = 0
invalidCount = 0

# find the first and second number
for i in lines:
    letter_split = i.partition(":")[0]
    letter = letter_split[-1]
    string_to_check = i.partition(":")[2]
    appearances = string_to_check.count(letter)

  # if the first number has 1 digit
    if i[1] == "-":
        reqNum = i[0]
        if i[3] != " ":
            maxNum = i[2]+i[3]
        else:
            maxNum = i[2]
  # if the first number has 2 digits
    else:
        reqNum = i[0] + i[1]
        if i[4] != " ":
            maxNum = i[3]+i[4]
        else:
            maxNum = i[3]
    # part 1 (comment out part 2)
     if int(appearances) >= int(reqNum) and int(appearances) <= int(maxNum):
         validCount = validCount + 1
     else:
         invalidCount = invalidCount + 1
    
    # part 2 (comment out part 1)
    if string_to_check[int(reqNum)] == letter and string_to_check[int(maxNum)] != letter:
        validCount = validCount+1
    if string_to_check[int(maxNum)] == letter and string_to_check[int(reqNum)] != letter:
        validCount = validCount+1
# answer
print(validCount)
