from get_data import get_data
import math
import matplotlib.pyplot as plt
import numpy as np

roles2 = ["reg", "reg", "vil1", "vil2", "cop", "doc"]
roles3 = ["reg", "reg", "vil1", "vil2", "vil3", "cop", "doc"]
roles4 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "cop", "doc"]
roles5 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "cop", "doc"]
roles6 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "cop", "doc"]
roles7 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "cop", "doc"]
roles8 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "vil8", "cop", "doc"]
roles9 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "vil8", "vil9", "cop", "doc"]
roles10 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "vil8", "vil9", "vil10", "cop", "doc"]
roles11 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "vil8", "vil9", "vil10", "vil11", "cop", "doc"]
roles12 = ["reg", "reg", "vil1", "vil2", "vil3", "vil4", "vil5", "vil6", "vil7", "vil8", "vil9", "vil10", "vil11", "vil12", "cop", "doc"]

w2 = get_data(roles2, 2)
w3 = get_data(roles3, 3)
w4 = get_data(roles4, 4)
w5 = get_data(roles5, 5)
w6 = get_data(roles6, 6)
w7 = get_data(roles7, 7)
w8 = get_data(roles8, 8)
w9 = get_data(roles9, 9)
w10 = get_data(roles10, 10)
w11 = get_data(roles11, 11)
w12 = get_data(roles12, 12)

even_winrates = [w2, w4, w6, w8, w10, w12]
even_winrates = [math.log10(i) for i in even_winrates]

odd_winrates = [w3, w5, w7, w9, w11]
odd_winrates = [math.log10(i) for i in odd_winrates]

even_vils = [2, 4, 6, 8, 10, 12]
even_vils = [math.log10(i) for i in even_vils]

odd_vils = [3, 5, 7, 9, 11]
odd_vils = [math.log10(i) for i in odd_vils]

plt.scatter(even_vils, even_winrates, color="red", label="Even Vil")
plt.scatter(odd_vils, odd_winrates, color="blue", label="Odd Vil")

alpha, beta = np.polyfit(even_vils, even_winrates, 1)
print(f"even coefficients: {alpha}, {beta}")
with open("results.txt", "a") as f:
    f.write(f"{alpha}, {beta}\n")
even_vils = np.array(even_vils)
plt.plot(even_vils, alpha*even_vils+beta, color="red")

alpha, beta = np.polyfit(odd_vils, odd_winrates, 1)
print(f"odd coefficients: {alpha}, {beta}")
with open("results.txt", "a") as f:
    f.write(f"{alpha}, {beta}\n")
odd_vils = np.array(odd_vils)
plt.plot(odd_vils, alpha*odd_vils+beta, color="blue")

plt.title("Village Winrate versus Villager Number")
plt.xlabel("log(Number of Villagers)")
plt.ylabel("log(Winrate) (log(%))")
plt.legend()
plt.show()
