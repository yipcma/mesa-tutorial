from model import *
import matplotlib.pyplot as plt

all_wealth = []
for j in range(100):
    model = MoneyModel(10)
    for i in range(10):
        model.step()
    agent_wealth = [a.wealth for a in model.schedule.agents]

    all_wealth.extend(agent_wealth)

plt.hist(all_wealth)
plt.show()