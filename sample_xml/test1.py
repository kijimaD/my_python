import xml.etree.ElementTree as ET

# xmlファイルを解析
tree1 = ET.parse("sports1.xml")
tree2 = ET.parse("sports2.xml")

# xmlを取得
root1 = tree1.getroot()
root2 = tree2.getroot()

for child in root1:
    print("1の結果:",child.tag, child.attrib)

for child in root2:
    print("2の結果:",child.tag, child.attrib)

# 要素「name」のデータを1つずつ取得
for name in root1.iter('name'):
    print(name.text)

# 配列でデータを1つずつ取得
print(root1[0][0].text)
print(root1[0][1].text)
print(root1[1][0].text)
print(root1[1][1].text)