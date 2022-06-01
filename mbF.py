import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import io
sd = pd.Timestamp("2020-08-12"+" 00:00:00")
ed = pd.Timestamp("2020-09-12"+" 00:10:00")
diff = ed - sd
print('Dates are between', sd, 'and', ed)
score = [random.randint(1, 10) for i in range(100)]
print(score)
dates = [sd + pd.tseries.offsets.DateOffset(days=random.randint(1, diff.days)) for i in range(100)]
print(dates)
def see(score, dates, start_date, end_date):
    def retList(x):
        y = dfm.loc[x]['Scores'].tolist()
        try:
            l = len(y)
            return y
        except:
            return [y]
    df = pd.DataFrame({'Scores': score, 'Dates': dates})
    df.sort_values('Dates', inplace=True)
    dfm = df[(df['Dates'] >= start_date) & (df['Dates'] <= end_date)]
    dfm.set_index('Dates', inplace=True)
    dls = [str(i).split()[0] for i in list(set(dfm.index))]
    dls.sort()
    yls = list(map(retList, dls))
    h = len(max(yls, key=len))
    buf = io.BytesIO()
    matplotlib.style.use(['dark_background'])
    pd.DataFrame(yls, index=dls, columns=["User " + str(i + 1) for i in range(h)]).plot(kind='bar', title="Ratings between " +str(start_date).split()[0] + " and " +str(end_date).split()[0], xlabel="Dates", ylabel="Scores", figsize=(9, 6))
    plt.tight_layout()
    plt.savefig(buf, format='png')
    im = Image.open(buf)
    return im
see(score, dates, "2020-08-25","2020-08-30").show()
