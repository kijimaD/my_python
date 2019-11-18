class Fish:
    def __init__(selfself, name, build="ほね", eyelids=False):
        self.name = name
        self.build = build
        self.eyelids = eyelids

    def swim(self):
        print("こちらの魚は泳ぎます")

    def swim_back(self):
        print("こちらの魚は後ろ向きにも泳ぎます")

class Medaka(Fish):
    pass