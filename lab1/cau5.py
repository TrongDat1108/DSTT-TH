import matplotlib .pyplot as plt
import numpy as np
l = [1, 4, 6, 8, 22, 11, 10, 3, 6]
x = [str(i) for i in np.arange(len(l))]
plt.bar(np.arange(len(l)),l,color='m')
plt.xticks(np.arange(len(l)),x)
plt.show ()
