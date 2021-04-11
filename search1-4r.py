import pandas as pd

def serch():
    df=pd.read_csv("./01serch/abc.csv")
    source=list(df["name"])

    while True:        
        word = input("アルファベットを入力してください >>")
        if word in source:
            print("{}がみつかりました".format(word))
        else:
            print("{}がみつかりませんでした".format(word))
            add_flg=input("追加登録しますか？(0：しない　1：する)")
            if add_flg=="1":
                source.append(word)
        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("./01serch/abc.csv",encoding="utf_8-sig")
        print(source)

if __name__ == "__main__":
    serch()
