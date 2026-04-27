import pandas as pd 
import matplotlib.pyplot as plt 
# Read CSV file 
df = pd.read_csv("marks.csv") 
# Display first 5 rows 
print(df.head()) 
# Statistical summary 
print("\nStatistical Summary:") 
print(df.describe()) 
# Visualization 
df.hist() 
plt.show() 
df.plot() 
plt.show()