import os
import json
from datetime import date, timedelta
import pandas as pd

class Test_Countstreaks:
    def __init__(self):

        loc = input("Enter where you want to count streaks for: ").lower()
        sdate = date(2020,6,12)   # start date
        e1date = date(2020,6,18)

        s1date = date(2020,6,23)
        e2date = date.today()  # end date
        range=pd.date_range(sdate,e1date-timedelta(days=0), freq='d')
        range1=pd.date_range(s1date,e2date-timedelta(days=0), freq='d')

        dates=[]
        for i in range:
            dates.append(str(i)[:-9])
        for i in range1:
            dates.append(str(i)[:-9])

        base=[]
        with open(f'{loc}_{dates[0]}.json') as js:
            dat=json.load(js)
            for n in dat[0]['trends']:
                base.append({
                    'trend_name': n['name'],
                    'streaks': 1,
                    'first_trended': dates[0]
                    })

        df = pd.DataFrame(base)

        for j in dates[1:]:
            file_name=f'{loc}_{j}.json'
            with open(file_name) as json_file:
                dat=[]
                data = json.load(json_file)
                for p in data[0]['trends']:
                    name=p['name']
                    if name not in df['trend_name']:
                        dat.append({
                            'trend_name': p['name'],
                            'streaks': 1,
                            'first_trended': j
                            })
                    else:
                        idx = df.index[df['trend_name']==name]
                        df['streaks'][idx]=df['streaks'][idx]+1
                new_df = pd.DataFrame(dat)
            df=df.append(new_df)
            print(j)

            df.to_csv(f'{loc}_streaks.csv', index = False, header=True, sep='\t', encoding='utf-8')

if __name__ == '__main__':
    cp=Test_Countstreaks()
