import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets

df = pd.read_csv('data.csv')

#print 'shape - ',df.shape
#print 'dataset description ---',df.columns


df.plot(kind='line', subplots=True, sharex=False, sharey=False)
plt.show()

