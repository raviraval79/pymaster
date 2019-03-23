#basic program to load a data and show line chart for the same

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets

#change the file path for trying different data files
df = pd.read_csv('data.csv')

#uncomment below to inspect data
#print 'shape - ',df.shape
#print 'dataset description ---',df.columns

#use below code to create line charts for each column
#df.plot(kind='line', subplots=True, sharex=False, sharey=False)

#use below code to create histogram for each column
#df.hist()

#use below code to show a chart for one of the columns
series = np.array(df['High'])
plt.plot(series)


plt.show()

