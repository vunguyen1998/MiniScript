import os

switcher = {
        1: "Khí Vận",
        2: "Cổ Trùng"
    }
print(switcher)
selectTruyen = input('Nhập số tương ứng: ')

def switchCase(argument):
    switcher = {
        1: "Khí Vận",
        2: "Cổ Trùng"
    }
    return switcher.get(argument, "nothing")
print(switchCase(selectTruyen))

while True:
    os.system('cls')
    cv = input('Nhập nội dung CV: ')
    ts = input('Nhập nội dung Dịch: ')
    # if os.path.isdir('new_folder') == False:
    #     os.mkdir('data')
    with open('data/train.txt', 'a', encoding="utf-8") as f:
        f.write('\n' + cv)
    with open('data/label_train.txt', 'a', encoding="utf-8") as f1:
        f1.write('\n' + ts)
