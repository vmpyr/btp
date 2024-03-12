import matplotlib.pyplot as plt

data = None

with open("./variable_history", "r", encoding="utf-8") as f:
    data = f.read()

data = data.split("\n")
data.pop()


for i in range(len(data)):
    data[i] = data[i].split(" ")
    data[i][2] = float(data[i][2][:-1])
    data[i][0] = int(data[i][0])
    data[i].pop(1)

# plot the data
plt.plot([x[0] for x in data], [x[1] for x in data])
plt.xlabel('Epochs')
plt.ylabel('Lambda')
plt.title('Lambda vs Epochs')
plt.grid()
plt.show()

