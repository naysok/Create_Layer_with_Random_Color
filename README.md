# Create_Layer_with_Random_Color  


ライノで新規レイヤーを作成するときに毎回毎回黒のレイヤーになる。補助線とそれから作った切断用ソリッドなどがすべて同じ色ではわかりにくく不便に感じる。  
レイヤーを新規作成する際に今あるレイヤーとは別の色でレイヤーを作成する（イラレなどはこうですね）コマンドを作った >>> `CreateLayer`  

![photo](_image/220807_1.png)  


## Install  

// インストーラを利用する場合  
下記より最新の rhi ファイルをダウンロードしてダイアログに従ってください。  
[https://github.com/naysok/Create_Layer_with_Random_Color/releases/](https://github.com/naysok/Create_Layer_with_Random_Color/releases/)  

// 自分でコンパイルする場合  
ライノのコマンド作成は、PythonEdtor から New >> Command で以下の写真のように設定する。  
そこに [_src/CreateLayer_cmd.py](https://github.com/naysok/Create_Layer_with_Random_Color/blob/main/_src/CreateLayer%EF%BC%BFcmd.py) の中身をコピペしスクリプトを実行すると、コマンドが作成されるはず。  

![photo](_image/220807_0.png)  

インストール先はここ。何かあればここを確認する。  
```
C:\Users\USER_NAME\AppData\Roaming\McNeel\Rhinoceros\7.0\Plug-ins\PythonPlugins
```


## Motivation  

まさしくこのスレッド↓。  
[https://discourse.mcneel.com/t/new-layer-with-random-color/13917/17](https://discourse.mcneel.com/t/new-layer-with-random-color/13917/17)  

このスレッド内にプラグインが置かれているが Rhino6 では動かないらしい。  

また、個人的には選択用の黄色などは避けたいし、数に限りの有るプリセットではなく今現在は無い色を探してその色にしてほしい。  


## 動作環境  

- Rhino6 en-us (Windows10)  
- Rhino7 en-us (Windows10)  

// そのほかは未確認  


## ポイント  

- 黄色は選択状態と被るので避ける  
- RGB を HSL 色空間に置き換えて、H の値で既存の色を避ける（これならば 1軸）  
  - RGB の三次元空間を評価するのが面倒  

作っから要らなかったものは `Purge` で消せるので、1個だけのレイヤーではなく、とりあえず適当に5個くらい作るほうがテンポが良かった。現状は5個作成していますが、10個作るでもいいかも。  

また、後で気が付いたことだが、親レイヤーとして使うレイヤーは黒がいいので、通常のレイヤー作成の機能を使い、ごちゃごちゃ触りたいようにこのランダムカラーのコマンドを使うというように、僕の使い方ではちょうど棲み分けが出来ている気がする。  


## 面倒  

- RhinoCommon で ColorARGB が Rhino7 以降で実装されているらしく Rhino6 では使えない  
- HSL を rhinoscriptsyntax の関数では HLS となっていてうれしくない  


## Ref  

- ColorRGBToHLS (rhinoscriptsyntax)  
  - [https://developer.rhino3d.com/api/RhinoScriptSyntax/#collapse-ColorRGBToHLS](https://developer.rhino3d.com/api/RhinoScriptSyntax/#collapse-ColorRGBToHLS)  


- ColorHLSToRGB (rhinoscriptsyntax)  
  - [https://developer.rhino3d.com/api/RhinoScriptSyntax/#collapse-ColorHLSToRGB](https://developer.rhino3d.com/api/RhinoScriptSyntax/#collapse-ColorHLSToRGB)  


- Rhino_Display_ColorHSL (RhinoCommon)  
  - [https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Display_ColorHSL.htm](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Display_ColorHSL.htm)  


- HSL and HSV (Wikipedia)  
  - [https://en.wikipedia.org/wiki/HSL_and_HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)  

