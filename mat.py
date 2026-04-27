import matplotlib.pyplot as plt
import pandas as pd
"""x=['a','b','c','d','e','f','g','h','i']
y=[1,2,3,4,5,6,7,8,9]

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph')
plt.show()

plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.show()"""


d=pd.read_csv('marks.csv')
print(d)
print(d.head())