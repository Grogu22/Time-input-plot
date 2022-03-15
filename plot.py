import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
df = pd.read_csv('data.csv')
print('Dates are between', df['Date'][0], 'and', df['Date'][13])
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)
while True:
    try:
        ds = pd.Timestamp(input("Enter start date :") + " 00:00:00")
        if (ds == df['Date']).any() == False: print("Enter start date again !! It is not in dataset")
        else: break
    except: print("Error !! Enter again.")
while True:
    try:
        de = pd.Timestamp(input("Enter end date :") + " 00:00:00")
        if (de == df['Date']).any() == False: print("Enter start date again !! It is not in dataset")
        else: break
    except: print('Error !! Enter again.')
dfm = df[(df['Date'] >= ds) & (df['Date'] <= de)]
cols = ['Open', 'High', 'Low', 'Close', 'Adj Close']
plt.figure(1, figsize=(8, 5))
plt.title('Bitcoin Prices', fontdict={'fontweight': 'bold', 'fontsize': 20})
for i in cols:
    plt.plot_date(dfm['Date'], dfm[i], '.-', label=i)
plt.tight_layout()
plt.legend(loc='upper left', frameon=True)
plt.show()
