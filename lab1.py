import numpy as np
import pandas as pd
data = pd.read_csv('tr_eikon_eod_data.csv',index_col=0, parse_dates=True)
data = pd.DataFrame(data['AAPL.O']) 
data['Returns'] = np.log(data / data.shift())
data.dropna(inplace=True)
lags = 6
cols = []
for lag in range(1, lags + 1):
     col = 'lag_{}'.format(lag)
     data[col] = np.sign(data['Returns'].shift(lag))
     cols.append(col)
data.dropna(inplace=True)
from sklearn.svm import SVC
model = SVC(gamma='auto') 
model.fit(data[cols], np.sign(data['Returns']))
data['Prediction'] = model.predict(data[cols]) 
data['Strategy'] = data['Prediction'] * data['Returns']
data[['Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
import matplotlib.pyplot as plt
plt.show()
