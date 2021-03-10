
import matplotlib.pyplot as plt
list = []

THICKNESS = 0.00008
folded_thickness = THICKNESS
for i in range(1,44):
    folded_thickness *= 2
    list.append(folded_thickness)


plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(list) # Enter the variable name of the list in "List name"
plt.show()
