import getch

KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122
KEY_D = 100


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 関数渡しで下記2つのメソッドを勇者インスタンスに渡す
        self.hero = Hero(3, 3, self.is_movable, self.get_message, self.draw)
        # マップは町人をリストで保持
        self.townspeople = []
        self.townspeople.append(Townsman(3, 1, 'K', "I'm King"))
        self.townspeople.append(Townsman(1, 5, 'S', "I'm Soldier 1"))
        self.townspeople.append(Townsman(5, 5, 'S', "I'm Soldier 2"))

    # ゲームを開始
    def run(self):
        self.hero.run()

    # 勇者が座標x, yに動ければTrueを返すメソッド
    def is_movable(self, x, y):
        # 枠の判定
        if (x < 0):
            return False
        elif (self.width - 1 < x):
            return False
        elif (y < 0):
            return False
        elif (self.height - 1 < y):
            return False

        # 町人の判定
        for townsman in self.townspeople:
            if(x == townsman.x and y == townsman.y):
                return False

        return True

    # 画面に現在の状態を描画するメソッド
    def draw(self, message):
        # 辞書のキーにx,yのタプル、バリューにキャラクターアイコンを登録
        characters = {}
        characters[(self.hero.x, self.hero.y)] = self.hero.icon
        # キャラクターアイコンの辞書に町人を追加
        for townsman in self.townspeople:
            characters[(townsman.x, townsman.y)] = townsman.icon

        # 各行をテキストで返すメソッド内の関数
        def get_row(y):
            row_list = []
            row_list.append('|')
            for x in range(0, self.width):
                # (x, y)にキャラクターがいればそれを描画し、いなければ空白を描画
                if((x, y) in characters):
                    row_list.append(characters[(x, y)])
                else:
                    row_list.append(' ')
            row_list.append('|\n')
            return ''.join(row_list)

        # 各行を連結してマップを作成
        map_list = []
        map_list.append('+{}+\n'.format('-' * self.width))
        for y in range(0, self.height):
            map_list.append(get_row(y))
        map_list.append('+{}+\n'.format('-' * self.width))

        map_list.append('{}\n'.format('#' * 10))
        map_list.append(message + '\n')
        map_list.append('{}\n'.format('#' * 10))

        print(''.join(map_list))

    def get_message(self, x, y):
        for townsman in self.townspeople:
            if(x == townsman.x and y == townsman.y):
                return townsman.message
        return 'no one exists..'


class Hero:
    # マップのis_movable と drawメソッドを受け取り登録
    def __init__(self, x, y, is_movable, get_message ,draw_map):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.get_message = get_message
        self.draw_map = draw_map

    def talk(self):
        message = ''
        if(self.icon == '^'):
            message = self.get_message(self.x, self.y-1)
        elif(self.icon == '<'):
            message = self.get_message(self.x-1, self.y)
        elif(self.icon == '>'):
            message = self.get_message(self.x+1, self.y)
        elif(self.icon == 'V'):
            message = self.get_message(self.x, self.y+1)
        return message

    def run(self):
        print('----------------------')
        print('w:up, a:left, s:right, z:down')
        print('ctrl-c:quit')
        print('----------------------')

        while (True):
            message = ''

            key = ord(getch.getch())
            if (key == KEY_CTRL_C):
                print('bye!!')
                break;
            elif (key == KEY_W):
                self.icon = '^'
                if(self.is_movable(self.x, self.y-1)):
                    self.y -= 1
            elif (key == KEY_A):
                self.icon = '<'
                if (self.is_movable(self.x-1, self.y)):
                    self.x -= 1
            elif (key == KEY_S):
                self.icon = '>'
                if (self.is_movable(self.x+1, self.y)):
                    self.x += 1
            elif (key == KEY_Z):
                self.icon = 'V'
                if (self.is_movable(self.x, self.y+1)):
                    self.y += 1
            elif(key == KEY_D):
                # 会話をしてメッセージを取得
                message = self.talk()
            else:
                print('key input: ' + str(key))
                continue
            # print('ICON:{}, X:{}, Y:{}'.format(self.icon,self.x, self.y))

            self.draw_map(message)

class Townsman:
    def __init__(self, x, y, icon, message):
        self.x = x
        self.y = y
        self.icon = icon
        self.message = message

dqmap = Map(7, 7)
dqmap.run()
