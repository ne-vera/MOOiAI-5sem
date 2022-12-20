import matplotlib.pyplot as plt

alpha = 0.06
beta = 0.04
gamma = 1 + alpha - beta
N = 10000

population_list = []
population_list.append(N)
i = 1
while i < 50:
    N = gamma * N
    population_list.append(N)
    i = i + 1

plt.plot([i for i in range(1, 51)],population_list)
plt.show()


start = 10000
finish = 2 * start
current = 10000
years = 0
while current < finish:
    current = current * gamma
    years += 1
print(f"Численность населения удваивоится через {years - 1} лет")

minus = population_list[10] * 0.8
years = 0
while minus < population_list[10]:
    minus = gamma * minus
    years = years + 1
print (f"Если на 10 - ый год численность населения упадет на 20%, она восстановится через {years} лет")

x = 1000000
N = 10000
logistic_list = []
logistic_list.append(N)
i = 1
while i < 50:
    N = N + gamma*(1 - N/x)*N
    logistic_list.append(N)
    i = i + 1

plt.plot([i for i in range(1, 51)],logistic_list)
plt.show()
