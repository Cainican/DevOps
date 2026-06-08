############################################
#   Kadai03-IT11A084-09 エリアッセンカスパ   #
############################################

def main():
    # メニュー
    while True:
        print("\n処理を選択してください。")
        print("1. ファイルの読み取り")
        print("2. ファイルの書き込み (新現)")
        print("3. ファイルの書込み (追記)")
        print("4. ユーザ登泉")
        print("5. パスワード認証")
        print("6. 終了")

        num = int(input("処理選択: "))

        def file_read():
            # テキストファイルを開く
            a1 = open("Kadai0201.txt", encoding="utf-8")

            # テキストを読む
            s = a1.read()

            # ファイルを閉じる
            a1.close()

            # 結果を表示する
            print("\n" + s)

        def file_write():
            # ファイルを開く
            a2 = open("Kadai0202.txt", mode="w", encoding="utf-8")

            # ファイルに書き込む
            a2.write("IT11A084 ")
            a2.write("09 ")
            a2.write("エリアッセンカスパ ")
            a2.write("課題02の 1. ")
            a2.write("完了!")

            # ファイルを閉じる
            a2.close

            # 課題02の02を表示する
            print("\n課題02の02. 完了!")

        def file_append():
            # (1) ファイルを開く
            a3 = open("Kadai0203.txt", mode="a", encoding="utf-8")

            # (2) ファイルを追記する
            sum = input("追記内容: ")
            
            a3.write("\n" + sum)

            # ファイルを閉じる
            a3.close()

        def file_user():
            print("\nID・PWD登泉\n")
            with open("Kadai0204.txt", mode="a", encoding="utf-8") as a4:
                userID = input("IDを入力: ")
                password = input("PWDを入力: ")

                # ユーザーIDを入力
                a4.write(f'{userID},{password}\n')

                print("\n登録しました!")

                # ファイルを閉じる
                a4.close()

        def file_psw():
            print("\nID・PWD認証\n")

            # ユーザーにIDとパスワードの入力を求める認証
            input_userID = input("IDを入力: ")
            input_password = input("PWDを入力: ")

            # ファイルを開いて、入力した資格情報が既存の資格情報と一致するかどうかを確認します
            try:
                with open("Kadai0204.txt", encoding="utf-8") as a5:
                    l_a5 = a5.readlines()
                
                # ファイル内の各行を確認
                for line in l_a5:
                    # Split by comma
                    user_data = line.strip().split(",")
                    stored_userID = user_data[0]
                    stored_password = user_data[1]

                    # 入力されたIDとパスワードを保存された値と比較する
                    if input_userID == stored_userID and input_password == stored_password:
                        print("一致")
                        print("\n認証!\n")
                        return
                
                print("\nIDまたはパスワードが違います。")
            
            # ファイルが見つかりられない場合
            except FileNotFoundError:
                print("\nファイルが見つかりません。")


        def print_done():
            print("終了")

        if num == 1:
            file_read()
        
        elif num == 2:
            file_write()

        elif num == 3:
            file_append()

        elif num == 4:
            file_user()

        elif num == 5:
            file_psw()

        elif num == 6:
            print_done()
            break

main()