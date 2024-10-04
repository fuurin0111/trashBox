#C++がコンパイラできる環境でないと無理です。
#まずこのディレクトリに移動して
#powershellの場合、./rip exp.rip
#ターミナル場合、   rip exp.rip
#または、 python rip.py exp.rip
# exp.ripはripファイルであれば大丈夫です。
#最期に"True"をつけると実行ファイルが消えます。(非推奨)

#コマンド
#imp : c++のライブラリをインポートできます。(imp <ライブラリ>)
#use : c++のusingディレクティブができます。。(use <省略名>)
#out : pythonのprint()と一緒です。(out <出力したいもの>)
#box : 変数定義ができます。(box <型> <変数名> <初期値>)
#cbox: 変数定義した変数の値を変更。(cbox <変数名> <値>)
#"#" : コメントが書けます。
#re  : 関数等のreturnができます。(re <値>)
#func: 関数が書けます。(func <型> <関数名>)
#for : 繰り返し処理できます。(for <型> <変数名> <初期値> <条件>)
#if  : 条件付き処理ができます。(if <条件>)
#else: いつも道理です。

#注意点
#if,else,func,for等で{}を使用しますが必ず改行してから書いてください。
#if,for等で条件を書く際は空白を入れないようにしてください。
#out 1+2 このようなこともできますが、これをする際も(1+2)のように空白を入れないでください。
#例: i == 2 ×
#    i==2　 〇

# コマンド実行・エラー発生時に途中終了するためのモジュールを読み込む
import sys
import os

# 変数の宣言
inp=""
tmp=0
out=""
INPUT=[]
OUTPUT=[]
ERROR=[]
k=0
com=""
bo=False

# トランスパイルの対応表
ces_command=["imp","use","out","box","#","re","{","}","func","for","cbox","#","if","else"]
cpp_command=[["#include <",1,">"],["using namespace ",1,";"],["cout << ",1," << endl",";"],[1," ",2," = ",3,";"],["// ",1],["return ",1,";"],["{"],["}"],[1," ",2,"()"],["for (",1," ",2," = ",3,"; ",4,"; ",2,"++)"],[1," = ",2,";"],[],["if (",1,")"],["else"]]

# 引数の取得
fni=sys.argv
fn=fni[1]
if fn.find(".rip") == -1:
    print(".ripを入れてください")
    sys.exit()
cn=fn.replace(".rip","")+".exe"    

# 入力を受け付ける代わりに第1引数で指定されたファイルを読み込みripのコードをリストに追記していく
_file=open(fn,"r",encoding="utf-8")
for line in _file:
    inp=line
    if inp == "\n":
        pass
    elif inp[0]=="!":
        INPUT.append(["!",inp[1:len(inp)]])
    else:
        INPUT.append(list(map(str,inp.split())))

# ファイルを閉じる
_file.close()

for ind,i in enumerate(INPUT,1):
    if i[0] in ces_command:
        tmp = ces_command.index(i[0])
        for u in cpp_command[tmp]:
            if type(u) is int:
                if u<=len(i)-1:
                    out += i[u]
                else:
                    k=0
                    for q in cpp_command[tmp]:
                        if type(q) is int and q > k:
                            k=q
                    ERROR.append([str(i)," ^\nline : "+str(ind)+" error!\nThere are not enough arguments\nRequired amount : "+str(k)])
                    bo=True
                    break
            else:
                out += u
        OUTPUT.append([out+"\n"])
        out = ""
    elif i != ["END"]:
        ERROR.append([i," ^\nline : "+str(ind)+" error!\nThere is no ",i," instruction"])
        bo=True

# エラーが出ていなければトランスパイルした結果を第2引数で指定されたファイル.cppに上書きし、トランスパイルの成功を通知する。エラーが出ていればエラーを出力する
if bo == True:
    # エラーの出力を見やすくするために一行空ける
    print()
    for i in ERROR:
        for j in i:
            print(j)
        print()
else:
    print(":) < rip trance was successful!")
    a = (len(fni) == 3 and fni[2] == "True")
    if not a:
        print(f"The next time you run it, you can use {cn} or ./{cn}")
    _file = open(cn+".cpp","w",encoding="utf-8")
    for i in OUTPUT:
        for j in i:
            _file.write(j)
    # ファイルを閉じ、第2引数で指定されたファイル名の実行ファイルを作成する
    _file.close()
    com="g++ "+cn+".cpp -o "+cn
    os.system(com)
    # トランスパイルしてcppファイルは消しておく
    com="del "+cn+".cpp"
    os.system(com)
    com="powershell -Command ./"+cn
    os.system(com)
    # 実行ファイルを刑したい場合は消すコード
    if a:
        com="del "+cn
        os.system(com)