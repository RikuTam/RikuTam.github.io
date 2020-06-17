# 最終課題
## SeaSlug Viewer

1. プログラムの内容<br>
    ・色を２つユーザーに選択する<br>
    ・それらを混ぜる(mix)か合わせるだけか(match)も選ぶ<br>
    ・出てきた色の名前を表示する<br>
    ・同時にその色のウミウシの画像とウミウシの名前を表示する。<br>
    ・気に入ったらLikeボタンを押すようにアラートする<br>
    ・Likeボタンを押したらカウント数が増える<br>
    ・カウント数を記録して色ごとのカウント数棒グラフを表示する。<br>
    ・色を変えたらカウントもリセットされ、0からスタート。<br>
    ・各色何回ボタンを押したかで自分の好みの色のウミウシがグラフから分かる。<br>
<br><br>
2. 工夫したところ<br>
    1. pythonについて<br>
    ・色１と色２が反転しても結果の色が変わらないように、python上ではもとの色のデータ(選択できるRGBの３色)を1,10,100の数値として置き換えた。初めは1×３のベクトルデータにしていたが、辞書のkeyにリストやnumpyオブジェクトが使えないことに気づき変更した。<br>
    ・ユーザーが選択した色の値をjavascriptから取得する作業を最初に関数で設定して、各flaskルートの中でデータ取得をいちいち書かないようにした。<br>
    ・ウミウシの写真のjpgデータの名前を計算後の色の名前と一致させることで、pythonでローカルデータのurlにアクセスにする際に直接javascriiptから取得したstr値を使えるようにした。<br>
    ・各色のカウント数に関するクエリ値を取得するのにリストとfor文を用いた<br>
    ・棒グラフの各棒の色を設定するのにfor文で一気に設定した。<br>
    2. javascriptについて<br>
    ・カウンター値を蓄積させるために、まずロードしたらカウンターの変数を定義する処理を実行するようにした。<br>
    ・各色のカウンター数をクエリパラメータに蓄積させるため最初にURLSearchParamsでクエリ文字列を作った。<br>
<br><br>
3. 苦労した点<br>
    ・pythonでローカルファイルの画像データを読み込んでバイナリデータに変換する方法を調べるのに苦労した。<br>
    ・html上でユーザーによって変更された値を変更するだけでなく蓄積させる方法に手間取った。最初はpython上で値を貯めようとしていたが、@app外で定義した変数が使えなくて断念。javascript上でやるにしてもonloadのメソッドを知らなかったので、まずhtmlに値を挿入して、その値を再度javascriptで取得しようと思ったが上手くいかなかった。<br>
    ・カウンター値はonloadのメソッドで変数を最初に定義すればよいことが分かったが、計算後の色データを別の関数やgetメソッドで再利用するのがどうしてもできなかったので、結局関数ごとにhtmlから入力された色データを取得しpythonに毎回計算させることにした。<br>
    ・サイト上で上手く表示されないときに一つ要素を変えると別の問題が新たに発生してまた表示されない、ということが多くかなり時間がかかった。<br>
    ・htmlとjavascriptは学んでいなったので、それらを理解するのに時間がかかった。結局javascriptはあまり理解していないが、いろいろなサイトのコードから付け焼刃でやってるうちになんとなく仕組みがわかった。<br>
    <br><br>
4. やりたりなかったこと<br>
    ・Likeボタンが押されるとカウンターが増えて、その増えたカウント数をグラフにプロットして表示する。という挙動にしたかったが、なぜか最初にLikeボタンを押すと、カウンターは増えてグラフが表示されるものの、カウント数が反映されてないままになってしまった。<br>
    つまり、１回目に押すとカウントは１と表示されるが、表示されるグラフ上では０となる。２回目押すとグラフは１で表示される。<br>
    ・javascript上で実行される関数やgetメソッドの順番が単純に上からになっていないせいだと思って、onclickやonmouseupメソッドでどうにかしてみたり、when.().done()メソッドを見つけて、順番を制御してみたりしたが上手くいかなかった。結局解決しないまま完成とした。<br>
    <br><br>
5. コメント<br>
    色々調べて修正を加えたり途中で新しいメソッドを見つけたりしながらの作業だったので、コードは汚くなりましたが、ウミウシのかわいさに免じて大目に見てください。<br><br>
    *画像引用サイト：[世界のウミウシ](https://seaslug.world/)*


```python

```