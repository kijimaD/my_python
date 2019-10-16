import datetime


def main():

    print("スコアを入力してください")

    while True:
        file_read = open("score.csv", "r", encoding="utf-8")
        i = 0
        for line in file_read:
            line = line.strip()  # 改行を取り除く
            in_data = line.split(",")
            print(f'{str(i)} {in_data[0]:10} {in_data[1]:10}')
            i += 1
        file_read.close

        print("usage:score")
        raw_input = input(">>")
        data = raw_input.split(",")
        score = data[0]
        if data[0] == "look":
            pass
            # df = pd.read_csv('score.csv', names=[
            #                  'record_time', 'entry', 'score'])
            # print(df.describe)
            # plt.plot(df['score'], marker="o")
            # plt.show()
            #
            # plt.xlabel('xlabel')  # x軸
            # plt.ylabel('ylabel')  # y軸
            # plt.show() # グラフの描画
        else:
            with open("score.csv", "a") as w:
                w.write(datetime.datetime.now().strftime(
                    '%Y/%m/%d|%H:%M:%S') + str(",") + score + str("\n"))


if __name__ == '__main__':
    main()
