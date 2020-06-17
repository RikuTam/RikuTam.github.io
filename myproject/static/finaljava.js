window.onload = function() {
    
//Likeカウンター用の変数設定
    var count_disp = document.getElementById("count");
    var count_value = 0;
    var count_up_btn = document.getElementById("like");
    var count_params = new URLSearchParams({'Red':0, 'Green':0, 'Blue':0, 'Cyan':0, 'Magenta':0, 'Yellow':0, 'Green&Blue':0, 'Blue&Red':0, 'Red&Green':0});
    
//色やウミウシ表示に関する関数
function SeaslugSelector() {
    
    var param = {};
    param["color_1"] = document.getElementById("c1").value;
    param["color_2"] = document.getElementById("c2").value;
    param["op"] = document.getElementById("op").value;
    var query = jQuery.param(param);

// 色の計算
    $.get("/seaslug/color" + "?" + query, function(data) {
        document.getElementById("result").innerHTML = data;
     });
//ウミウシの画像表示
    $.get("/seaslug/image"+"?"+ query, function(data) {
        document.getElementById("seaslugimg").src = data;
     });
//Like押すのを促す
    $.get("/seaslug/color" + "?" + query, function(data) {
        alert(data + '色のウミウシが気に入ったらLikeを押してね！');
     });
//ウミウシの名前表示
    $.get("/seaslug/name"+"?"+query, function(data){
        document.getElementById("seaslugname").innerHTML = data
      });
};
   
    
//クリックでLikeカウンターアップしてカウント数をSearchparamsに記録
function CounterUp() {
            count_value += 1;
            count_disp.innerHTML = count_value;
        
        var param = {};
        param["color_1"] = document.getElementById("c1").value;
        param["color_2"] = document.getElementById("c2").value;
        param["op"] = document.getElementById("op").value;
        var query = jQuery.param(param);
    
        $.get("/seaslug/color" + "?" + query, function(data) {
            count_params.set(data,count_value);
         });
};    
    

//Likeボタンでカウント数プロットとグラフ表示
function GraphViewer() {
    
        $.get("/seaslug/count"+"?"+count_params.toString(), function(data){
            document.getElementById("plotimg").src = data;
        });  
};

    
//Likeボタンの色の挙動
count_up_btn.onmousedown = function() {
          count_up_btn.style.backgroundColor = "#FF69B4";
};
count_up_btn.onmouseup = function() {
      count_up_btn.style.backgroundColor = "";
};
    
//色が変わったらカウンターをリセットする関数
function CounterRemove(){
    count_value = 0;
    count_disp.innerHTML = count_value;
};
    
// イベント設定
document.getElementById("like").addEventListener("click", function(){
    $.when(
          CounterUp()
    ).done(function(){
          GraphViewer();
    });  
}, false);
document.getElementById("c1").addEventListener("change", function(){
    SeaslugSelector();
    CounterRemove();
}, false);
document.getElementById("c2").addEventListener("change", function(){
    SeaslugSelector();
    CounterRemove()
}, false);
document.getElementById("op").addEventListener("change", function(){
    SeaslugSelector();
    CounterRemove()
}, false);
// run once
SeaslugSelector();
    
};