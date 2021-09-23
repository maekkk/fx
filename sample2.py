import sys
print(sys.version)
print(sys.path)
from importlib_metadata import version
print(version('numpy'))


#二次元グラフのサンプル
import matplotlib.pyplot as plt
x = [100,200,300,400,500]
y = [1,2,3,4,5]
#グラフを書く
plt.plot(x,y)

#グラフのタイトル
plt.title("x/y")
#x軸のラベル
plt.xlabel("x")
#y軸のラベル
plt.ylabel("y")
#表示
plt.show()

#ファイル読み込みのサンプル
from tkinter import filedialog

typ = [('テキストファイル','*.*')] 
dir = 'C:\\pg'
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

print(fle)

#pandasのサンプル
import pandas as pd

# データの読み込み
typ = [('テキストファイル','*.*')] 
dir = 'C:\\pg'
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

factories = pd.read_csv(fle, index_col=0)
print(factories)
