import numpy as np
import pandas as pd
from google.colab import drive
from datetime import datetime
import sys

filename = sys.argv[1]

df = pd.read_csv(filename)

def get_stat(df):
  ans = [0, 0, 0, 0, 0,]
  listSegment = np.unique(df['Segment'])
  move = [[], [], [], [], []]
  subgamecategory = [[], [], [], [], []]
  os = [[], [], [], [], []]
  obl = [[], [], [], [], [], []]
  version = [[], [], [], [], []]
  for i, item in enumerate(df['Segment']):
    ans[item-1]+=1
    move[item-1].append(df['gamecategory'][i])
    obl[item-1].append(df['oblast'][i])
    os[item-1].append(df['os'][i])
    subgamecategory[item-1].append(df['subgamecategory'][i])
    version[item-1].append(df['osv'][i])
  game = []
  osi=[]
  ios = []
  veri = []
  obli = []
  for i in range(5):
    ans[i] = ans[i]/len(df['Segment'])*100
    dat = pd.DataFrame(move[i]).value_counts()
    col = dat.index.tolist()
    game.append(dat[0]/len(move[i]))
    dat = pd.DataFrame(os[i]).value_counts()
    osi.append(dat[0]/len(os[i]))
    ios.append((len(os[i])-dat[0])/len(os[i]))
    dat = pd.DataFrame(obl[i]).value_counts()
    ufa = str(dat.index.tolist()[0])
    ufa = ufa[2:len(ufa)-3]
    obli.append(ufa)
    dat = pd.DataFrame(version[i]).value_counts()
    code = str(dat.index.tolist()[0])
    code = code[2:len(code)-3]
    veri.append(code)
  pas={
      'Segment':listSegment,
      'Сoverage': ans,
      'oblast' : obli,
      'osv': veri,
      'Love Game': game,
      'Android':osi,
      'IOS': ios
  }

  df_ret = pd.DataFrame(pas)
  return df_ret

stat = get_stat(df)

stat.to_csv('state.csv')
