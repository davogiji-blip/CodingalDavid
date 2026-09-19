def binarytoInt(binaryInput)
binary = {'0' : 0, '1': 1}
resultInteger = 0

for i in range(0, len(binary) - 1 ):
  resultInteger = resultInteger + binary[binaryInput[i]] * 2

return resultInteger + binary[binaryInput[-1]]


binaryNum = Input("Input Binary Number : ")
print("Integr equivalent : ", binarytoInt(binaryNum))

