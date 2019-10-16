import json


def test1():
    """json書き込み"""
    dic = {
        "profile0": {
            "first": "Tarou",
            "last": "Tanaka"
        },
        "profile1": {
            "first": "Hanako",
            "last": "Yamada"
        }
    }
    a = open('sample2.json', 'w')
    json.dump(dic, a, indent=4)


def test2():
    """json読み込み"""
    a = open('sample2.json', 'r', encoding='utf-8')
    b = json.load(a)

    # print(b["profile1"])
    for i in range(2):
        print(b["profile" + str(i)]["last"] + b["profile" + str(i)]["first"])


# test1()
test2()
