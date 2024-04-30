import wx                       #wxpython(GUI)

import matplotlib as mpl        #グラフ描画
import matplotlib.pyplot as plt #matplotlibパッケージ内のモジュール
from mpl_toolkits.mplot3d import Axes3D

import numpy as np              #ベクトルや行列の計算を高速に処理するためのライブラリ
import seaborn                  #グラフの体裁が良くなる？
import seaborn as sns           #文字設定のため

import pandas as pd             #データの統計量を表示したり、グラフ化するなど、データ分析や機械学習で必要となる作業を簡単に行うことができる




#GUI関連
class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "グラフ描画", size=(250,80))

        # Create widgets.(コンボボックス、ボタン実装)
        panel = wx.Panel(self)

        #self←クラスのインスタンス変数宣言
#        self.combo = wx.ComboBox(panel, choices=self.items,style=wx.CB_READONLY)
        #self.combo.Bind(wx.EVT_COMBOBOX, self.SelectItem)

        button_1 = wx.Button(panel, wx.ID_ANY, '実行')
        #Bindイベントを関連付ける
        button_1.Bind(wx.EVT_BUTTON, self.click_button_1)
        button_2 = wx.Button(panel, wx.ID_ANY, '閉じる')
        button_2.Bind(wx.EVT_BUTTON, self.click_button_2)
   

        # Set sizer.(レイアウト設定)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(button_1,1)
        sizer.Add(button_2,1)

        #sizerにsizer_hを追加してレイアウト表示
        panel.SetSizer(sizer)


    #コンボボックス選択時の処理
#    def SelectItem(self,event):
#        plt.clf()
#        plt.close()

    #実行ボタン押下時の処理
    def click_button_1(self,event):
        #正弦波選択
         R_sin.sin_g()

#        event.Skip()実装前に使用

    #閉じるボタン押下時の処理
    def click_button_2(self, event):  # wxGlade: MyFrame.<event_handler>
        #アプリケーション終了
        self.Destroy()


#リアルタイムで正弦波
class R_sin():
   def sin_g():

       # 描画領域を取得
        fig, ax = plt.subplots(1, 1)

        # y軸方向の描画幅を指定
        ax.set_ylim((-1.1, 1.1))

        # x軸:時刻
        x = np.arange(0, 100, 0.5)

        # 周波数を高くしていく
        for Hz in np.arange(0.1, 10.1, 0.01):
          # sin波を取得
          y = np.sin(2.0 * np.pi * (x * Hz) / 100)
          # グラフを描画する
          line, = ax.plot(x, y, color='blue')
          # 次の描画まで0.01秒待つ
          plt.pause(0.01)
          # グラフをクリア
          line.remove()

#        plt.clf()
#        plt.close()

if __name__ == '__main__':
    #wx.AppのMainLoop関数を呼び出しを行い，イベントのキャッチを開始
    app = wx.App(False)
    MyFrame().Show(True)
    app.MainLoop()