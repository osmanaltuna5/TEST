# %%
import numpy as np
from matplotlib import pyplot as plt
# number of experiments
P2 = (1-(5/6)**4)
# length of the list
print(P2)
M = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

probs = []

for m in M:
    list1 = np.arange(m)
    match_count = 0

    N = range(1, m)
    total_count = 0
    for n in N:
       
        three_count = 0
        list = [np.random.randint(1,7),np.random.randint(1,7),np.random.randint(1,7),np.random.randint(1,7)]
        for number in list:
            if number==3:
                match_count += 1
                break
            
    print(match_count/n)   
    probs.append(match_count/n)
    print('Experimental probability for length {}: {:.4f} %'
          .format(m, probs[-1]*100))

plt.plot(M, probs, label=str(m))

plt.show()