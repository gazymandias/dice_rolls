from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def d(sides):
    return randint(1, sides)


def roll(n, sides):
    return tuple(d(sides) for _ in range(n))


rolls = []
epoch = 0
all_rolls = pd.DataFrame(columns=['epoch', 'rolls'])

while len(np.unique(rolls)) != 20:
    dice = roll(1, 20)
    rolls.append(dice)
    if len(np.unique(rolls)) == 20:
        # print(f"Completed in {len(rolls)} rolls")
        epoch_rolls = pd.DataFrame([[epoch, len(rolls)]], columns=['epoch', 'rolls'])
        all_rolls = all_rolls.append(epoch_rolls, ignore_index=True)
        # reset
        rolls = []
        epoch += 1
        if epoch <= 100000:
            continue
        else:
            break

minValue = all_rolls['rolls'].min()
maxValue = all_rolls['rolls'].max()
meanValue = all_rolls['rolls'].mean()
modeValue = all_rolls['rolls'].mode()

# print(all_rolls)
print(f"Min: {minValue}, Max: {maxValue}, Mean: {meanValue}")
sns.distplot(all_rolls['rolls'])
plt.show()
