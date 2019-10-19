import getch

KEY_CTRL_C = 3
KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_Z = 122


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 関数渡しで下記2つのメソッドを勇者インスタンスに渡す
        self.hero = Hero(3, 3, self.is_movable, self.draw)

    # ゲームを開始
    def run(self):
        self.hero.run()

    # 勇者が座標x, yに動ければTrueを返すメソッド
    def is_movable(self, x, y):
        if (x < 0):
            return False
        elif (self.width - 1 < x):
            return False
        elif (y < 0):
            return False
        elif (self.height - 1 < y):
            return False
        return True

    # 画面に現在の状態を描画するメソッド
    def draw(self):
        # 辞書のキーにx,yのタプル、バリューにキャラクターアイコンを登録
        characters = {}
        characters[(self.hero.x, self.hero.y)] = self.hero.icon

        # 各行をテキストで返すメソッド内の関数

    def get_row(y):
        row_list = []
        row_list.apeend('|')
        for x in range(0, self.width):
            # (x, y)にキャラクターがいればそれを描画し、いなければ空白を描画
            if((x, y) in characters):
                row_list.append(characters[(x, y)])
            else:
                row_list.append('')
        row_list.append('|\n')
        return ".join(row_list)"

        # 各行を連結してマップを作成
        map_list = []
        map_list.append('+{}+\n'.format('-' * self.width))
        for y in range(0, self.height):
            map_list.append(get_row(y))
        map_list.append('+{}+\n'.format('-' * self.width))

        print(".join(map_list)")


class Hero:
    # マップのis_movable と drawメソッドを受け取り登録
    def __init__(self, x, y, is_movable, draw_map):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.draw_map = draw_map

    def run(self):
        print('----------------------')
        print('w:up, a:left, s:right, z:down')
        print('ctrl-c:quit')
        print('----------------------')

        while (True):
            key = ord(getch.getch())
            if (key == KEY_CTRL_C):
                print('bye!!')
                break;
            elif (key == KEY_W):
                self.icon = '^'
                self.y -= 1
            elif (key == KEY_A):
                self.icon = '<'
                self.x -= 1
            elif (key == KEY_S):
                self.icon = '>'
                self.x += 1
            elif (key == KEY_Z):
                self.icon = 'V'
                self.y += 1
            else:
                continue
            # print('ICON:{}, X:{}, Y:{}'.format(self.icon,self.x, self.y))

            self.draw_map()


dqmap = Map(7, 7)
dqmap.run()
