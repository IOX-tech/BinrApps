import time

for i in range(10):
    time.sleep(1)
    print(10-i,"seconds left")
print("Done!!")
p = input("Input Y to continue:")
if p == 'y' or p == 'Y':
    print("confirmed")
else:
    exit