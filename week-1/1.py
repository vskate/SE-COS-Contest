numberOfPackages = 10
candiesSum = sum(range(1, 11))

print(candiesSum)

topValue = numberOfPackages
lowValue = 0
numberOfGifts = 0

while (topValue + lowValue == numberOfPackages) & (topValue > numberOfPackages / 2):
    numberOfGifts += 1
    topValue -= 1
    lowValue += 1
    print(lowValue, topValue)

print("The number of students that will receive gifts is: " + str(numberOfGifts))
print()
