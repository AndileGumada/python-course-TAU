# while loop runs a number of times a condition remains true
temp_f = 40

while temp_f > 32:
    print("The water is {} degrees .".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
      break
# Break - end the loop go to the next statement(outside the loop)
# Continue skips current part of the loop moves to the next part of the loop
# Pass-skips any part of the loop where "pass" appears
for nummber in range(1,9):
    if nummber == 7:
        print("We are skipping number 7")
        continue
    print("This is the number {}".format(nummber))

for nummber in range(1,7):
    if nummber == 3:
        pass
    else:
        print("The number is {} .".format(nummber))
