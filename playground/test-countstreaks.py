import os
import json
from datetime import date, timedelta
import pandas as pd

class Test_Countstreaks:
    def __init__(self):

        loc = input("Enter where you want to count streaks for: ").lower()
        sdate = date(2020,6,12)   # start date
        edate = date(2020,6,18)

        s1date = date(2020,6,23)
        e1date=date(2020,6,28)

        s2date=date(2020,7,2)
        e2date = date.today()  # end date
        range=pd.date_range(sdate,edate-timedelta(days=0), freq='d')
        range1=pd.date_range(s1date,e1date-timedelta(days=0), freq='d')
        range2=pd.date_range(s2date,e2date-timedelta(days=0), freq='d')

        dates=[]
        for i in range:
            dates.append(str(i)[:-9])
        for i in range1:
            dates.append(str(i)[:-9])
        for i in range2:
            dates.append(str(i)[:-9])

        base=[]
        names=[]
        with open(f'{loc}_{dates[0]}.json') as js:
            dat=json.load(js)
            for n in dat[0]['trends']:
                base.append({
                    'trend_name': n['name'],
                    'streaks': 1,
                    'first_trended': dates[0]
                    })
                names.append(n['name'])

        df = pd.DataFrame(base)

        for j in dates[1:]:
            file_name=f'{loc}_{j}.json'
            with open(file_name) as json_file:
                dat=[]
                data = json.load(json_file)
                for p in data[0]['trends']:
                    name=p['name']
                    if name not in names:
                        dat.append({
                            'trend_name': name,
                            'streaks': 1,
                            'first_trended': j
                            })
                        names.append(name)
                    else:
                        idx = df.index[df['trend_name']==name]
                        df.loc[idx, 'streaks'] += 1
                new_df = pd.DataFrame(dat)
            df=df.append(new_df)
            print(j)

        df=df.sort_values(by=['streaks'], ascending=False)
        df.to_csv(f'{loc}_streaks.csv', index = False, header=True, sep='\t', encoding='utf-8')

if __name__ == '__main__':
    cp=Test_Countstreaks()
