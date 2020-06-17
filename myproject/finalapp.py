#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np
import io
from io import BytesIO
import matplotlib.pyplot as plt

app = Flask(__name__)

#入力された色を取得して返す色を計算
def palette():
    color_1 = request.args.get("color_1", default=1, type=int)
    color_2 = request.args.get("color_2", default=1, type=int)     
    op = request.args.get("op", "+")
    
    if color_1 == color_2:
        ret = color_1
    else:
        if op == "+" or op == "mix":
            ret = color_1 + color_2
        elif op == "&" or op == "match":
            ret = -(color_1 + color_2)
    color_dic = {1:'Red', 10:'Green', 100:'Blue', 110:'Cyan', 101:'Magenta', 11:'Yellow', -110:'Green&Blue', -101:'Blue&Red', -11:'Red&Green'}
    return color_dic[ret]

@app.route("/")
def index():
    return render_template("sea-slug.html")

@app.route("/seaslug/<seaslug>")
def seaslug_viwer(seaslug):
    ##色の名前を返す
    if seaslug == "color":
        return palette()
    
    ##計算した色のウミウシの写真データを返す
    elif seaslug == "image":
        color_name = palette()
        url = 'file:static/'+ color_name+'.jpg'
        img_in = urllib.request.urlopen(url).read()
        img_bin = io.BytesIO(img_in)
        img_data = urllib.parse.quote(img_bin.getvalue())
        return "data:image/png:base64," + img_data
    
    ##計算した色のウミウシの名前を返す
    elif seaslug == "name":
        name_dic = {'Red':'アカズキンリュウグウウミウシ','Green':'ミドリリュウグウウミウシ' ,'Blue':'アオフチキセワタ','Cyan':'ミスジアオイロウミウシ','Magenta':'ヒロウミウシ','Yellow':'ウデフリツノザヤウミウシ','Green&Blue':'アオボシミドリガイ','Blue&Red':'セトリュウグウウミウシ','Red&Green':'ラボウトウミウシ'}
        color_name = palette()
        return name_dic[color_name]
    ##色ごとのカウント数のクオリ値を取得してプロットグラフを作成して返す
    elif seaslug == "count":
        counter_list = [0]*9
        color_list = ['Red','Green','Blue','Cyan','Magenta','Yellow','Green&Blue','Blue&Red','Red&Green']
        for i,color in enumerate(color_list):
            counter_list[i] = request.args.get(color, default=0, type=int)
        fig, ax = plt.subplots(1,1)    
        bar_list = ax.bar(color_list, counter_list)
        ax.set_title('Your Favorit Color Of Seaslugs')
        ax.set_xlabel('color')
        ax.set_ylabel('numer of Like')
        plt.xticks(rotation=60)
        plt.yticks([0,2,4,6,8,10,15,20])
        ax.set_ylim(0,)
        for i,c in enumerate(["r","g","b","cyan","magenta","yellow","mediumspringgreen","darkviolet","orange"]):
            bar_list[i].set_color(c)
        png_out = BytesIO()
        plt.savefig(png_out, format="png", bbox_inches="tight")
        plotimg_data = urllib.parse.quote(png_out.getvalue())
        return "data:image/png:base64," + plotimg_data
        
        

if __name__ == "__main__":
    app.run(debug=True, port=5000)

