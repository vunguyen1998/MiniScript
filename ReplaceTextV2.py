import os
import time
from tkinter import *
from tkinter import messagebox
import re

def edit_text():
    text2.delete("1.0", "end")
    txt = text.get("1.0", "end")

    #Tính thời gian tại thời điểm bắt đầu thuật toán
    start_time = time.time()

    # Mở và đọc data
    freplace = open("./txt/replace.txt", "r", encoding="utf-8")
    fname = open("./txt/name.txt", "r", encoding="utf-8")
    fsau_name = open("./txt/sau_name.txt", "r", encoding="utf-8")
    ftruoc_name = open("./txt/truoc_name.txt", "r", encoding="utf-8")
    fluat_nhan = open("./txt/luat_nhan.txt", "r", encoding="utf-8")
    fxung_ho = open("./txt/xung_ho.txt", "r", encoding="utf-8")
    
    ftrang_bi = open("./txt/trang_bi.txt", "r", encoding="utf-8")
    fcap_bac = open("./txt/cap_bac.txt", "r", encoding="utf-8")
    ften_cap_bac = open("./txt/ten_cap_bac.txt", "r", encoding="utf-8")

    # Tạo file tạm
    ftemp = open("./txt/temp.txt", "a", encoding="utf-8")
    
    # Tạo mảng trống
    replace= []
    name = []
    name2 = []
    name3 = []
    truoc_name = []
    truoc_name2 = []
    sau_name = []
    sau_name2 = []
    luat_nhan = []
    xung_ho = []
    xung_ho2 = []
    number = []
    
    trang_bi = []
    trang_bi2 = []
    cap_bac = []
    cap_bac2 = []
    ten_cap_bac = []
    ten_cap_bac2 = []

    # Lọc data theo thứ tự dài -> ngắn
    for line in freplace.readlines():
        replace.append(line.strip('\n'))
    for line in fname.readlines():
        name.append(line.strip())
    for line in ftruoc_name.readlines():
        truoc_name.append(line.strip())
    for line in fsau_name.readlines():
        sau_name.append(line.strip())
    for line in fluat_nhan.readlines():
        luat_nhan.append(line.strip())
    for line in fxung_ho.readlines():
        xung_ho.append(line.strip())
        
    for line in ftrang_bi.readlines():
        trang_bi.append(line.strip())
    for line in fcap_bac.readlines():
        cap_bac.append(line.strip())
    for line in ften_cap_bac.readlines():
        ten_cap_bac.append(line.strip())

    # Điền data đã lọc vào mảng trống đã tạo trước đó
    replace = sorted(replace, key=len, reverse=True)
    name = sorted(name, key=len, reverse=True)
    truoc_name = sorted(truoc_name, key=len, reverse=True)
    sau_name = sorted(sau_name, key=len, reverse=True)
    luat_nhan = sorted(luat_nhan, key=len, reverse=True)
    xung_ho = sorted(xung_ho, key=len, reverse=True)
    
    trang_bi = sorted(trang_bi, key=len, reverse=True)
    cap_bac = sorted(cap_bac, key=len, reverse=True)
    ten_cap_bac = sorted(ten_cap_bac, key=len, reverse=True)
    
    number = re.findall(r'\d+', txt)
    number = sorted(number, key=len, reverse=True)
    
    # Sắp xếp câu
    for rp in replace:
        if rp.find(' ') > -1 and rp.find('=') > -1:
            old = rp.split('=')[0]
            new = rp.split('=')[1]
            txt = txt.replace(old[0].upper() + old[1:], new)
            txt = txt.replace(old[0].lower() + old[1:], new)

    # Chuẩn bị trước, lọc những Name, Trước Name, Sau Name cần sử dụng, rồi lưu vào biến riêng
    for i in name:
        if txt.find(i) > -1:
            name2.append(i.strip())
            
    for i in xung_ho:
        if txt.find(i[0].upper() + i[1:]) > -1:S
            xung_ho2.append((i[0].upper() + i[1:]).strip())
        elif txt.find(i[0].lower() + i[1:]) > -1:
            xung_ho2.append((i[0].lower() + i[1:]).strip())

    for i in truoc_name:
        if txt.find(i.split('*')[0]) > -1:
            truoc_name2.append(i.strip())

    for i in sau_name:
        if txt.find(i[0].upper() + i[1:]) > -1:
            sau_name2.append((i[0].upper() + i[1:]).strip())
        elif txt.find(i[0].lower() + i[1:]) > -1:
            sau_name2.append((i[0].lower() + i[1:]).strip())
    
    for i in trang_bi:
        if txt.find(i) > -1:
            trang_bi2.append(i.strip())
    
    for i in cap_bac:
        if txt.find(i) > -1:
            cap_bac2.append(i.strip())
    
    for i in ten_cap_bac:
        if txt.find(i.lower()) > -1:
            ten_cap_bac2.append(i.lower().strip())
        if txt.find(i.title()) > -1:
            ten_cap_bac2.append(i.title().strip())
        
    for j in number:
        txt = txt.replace('kinh nghiệm ' + j + ' điểm', j + ' điểm kinh nghiệm')
        txt = txt.replace('hồn tinh ' + j + ' viên', j + ' viên hồn tinh')
        
        # đổi vạn
        if int(j) < 100:
            txt = txt.replace(j + " vạn", str(int(j)*10) + " ngàn")
        elif (int(j)%100 == 0):
            txt = txt.replace(j + " vạn", str(int(j)//100) + " triệu")
        else:
            txt = txt.replace(j + " vạn", str(int(j)//100) + " triệu " + str(int(j)%100) + "0 ngàn")
        
        # đổi ức
        if int(j) < 10:
            txt = txt.replace(j + " ức", str(int(j)*100) + " triệu")
        elif (int(j)%10 == 0):
            txt = txt.replace(j + " ức", str(int(j)//10) + " tỷ")
        else:
            txt = txt.replace(j + " ức", str(int(j)//10) + " tỷ " + str(int(j)%10) + "00 triệu")

    #  Sắp xếp tên cấp bậc trang bị
    for i in trang_bi2:
        for j in cap_bac2:
            for k in ten_cap_bac2:
                txt = txt.replace(k.lower() + " " + j + " " + i, i + " " + j + " " + k.title())
                txt = txt.replace(k.title() + " " + j + " " + i, i + " " + j + " " + k.title())

    for i in name2:
        
        # Đổi Name X Number = Number viên Name
        for j in number:
            txt = txt.replace(i + " × " + j, j + " viên " + i)
            txt = txt.replace(i + " ×" + j, j + " viên " + i)
        
        # Tìm Name cùng Name, Name Name
        for j in name2:
            if txt.find(i + " cùng " + j) != -1:
                txt = txt.replace(i + " cùng " + j, i + j + "end")
                name3.append(i + " và " + j)
                ftemp.write(i + j + "end=" + i + " và " + j + '\n')
            if txt.find(j + " cùng " + i) != -1:
                txt = txt.replace(j + " cùng " + i, j + i + "end")
                name3.append(j + " và " + i)
                ftemp.write(j + i + "end=" + j + " và " + i + '\n')
                
            if txt.find(i + " " + j) != -1:
                txt = txt.replace(i + " " + j, j + i + "end")
                name3.append(j + " của " + i)
                ftemp.write(j + i + "end=" + j + " của " + i + '\n')
            if txt.find(j + " " + i) != -1:
                txt = txt.replace(j + " " + i, i + j + "end")
                name3.append(i + " của " + j)
                ftemp.write(i + j + "end=" + i + " của " + j + '\n')

        # Luật nhân
        for j in luat_nhan:
            j1 = j.split('=')[0]
            j1_truoc = j1.split('{0}')[0]
            j1_sau = j1.split('{0}')[1]
            
            j2 = j.split('=')[1]
            j2_truoc = j2.split('{0}')[0]
            j2_sau = j2.split('{0}')[1]
            
            if len(j1_truoc) > 0:
                if (txt.find(j1_truoc[0].lower() + j1_truoc[1:] + i + j1_sau) != -1 or txt.find(j1_truoc[0].upper() + j1_truoc[1:] + i + j1_sau) != -1):
                    txt = txt.replace(j1_truoc[0].lower() + j1_truoc[1:] + i + j1_sau, "start" + j2_truoc + i + j2_sau + "end")
                    txt = txt.replace(j1_truoc[0].upper() + j1_truoc[1:] + i + j1_sau, "start" + j2_truoc + i + j2_sau + "end")
                    name3.append(j2_truoc + i + j2_sau)
                    ftemp.write("start" + j2_truoc + i + j2_sau + "end=" + j2_truoc + i + j2_sau + '\n')
            else:
                if txt.find(i + j1_sau) != -1:
                    txt = txt.replace(i + j1_sau, "start" + j2_truoc + i + j2_sau + "end")
                    name3.append(j2_truoc + i + j2_sau)
                    ftemp.write("start" + j2_truoc + i + j2_sau + "end=" + j2_truoc + i + j2_sau + '\n')

        for j in sau_name2:
            for k in truoc_name2:
                if (k.find('*') == -1):
                    if txt.find(j + " " + i + " " + k) != -1:
                        txt = txt.replace(j + " " + i + " " + k, k + i + j + "end")
                        name3.append(k + " " + i + " " + (j[0].lower() + j[1:]))
                        ftemp.write(k + i + j + "end=" + k + " " + i + " " + (j[0].lower() + j[1:]) + '\n')
                else:
                    k = k.split('*')[0]
                    if txt.find(j + " " + i + " " + k) != -1:
                        txt = txt.replace(j + " " + i + " " + k, k + i + j + "end")
                        name3.append(k + " của " + i + " " + (j[0].lower() + j[1:]))
                        ftemp.write(k + i + j + "end=" + k + " của " + i + " " + (j[0].lower() + j[1:]) + '\n')

            if txt.find(j + " " + i) != -1:
                txt = txt.replace(j + " " + i, i + j + "end")
                name3.append(i + " " + (j[0].lower() + j[1:]))
                ftemp.write(i + j + "end=" + i + " " + (j[0].lower() + j[1:]) + '\n')

        for j in truoc_name2:
            if (j.find('*') == -1):
                if txt.find(i + " " + j) != -1:
                    txt = txt.replace(i + " " + j, j + i + "end")
                    name3.append(j + " " + i)
                    ftemp.write(j + i + "end=" + j + " " + i + '\n')
            else:
                j = j.split('*')[0]       
                if txt.find(i + " " + j) != -1:
                    txt = txt.replace(i + " " + j, j + i + "end")
                    name3.append(j + " của " + i)
                    ftemp.write(j + i + "end=" + j + " của " + i + '\n')
    
    ftemp.close()
    ftemp = open("./txt/temp.txt", "r", encoding="utf-8")
    ftemp = ftemp.read().split('\n')
    
    # Replace từ trong file tạm
    for i in ftemp:
        if i != '':
            txt = txt.replace(i.split('=')[0], i.split('=')[1])
    
    # Xóa file tạm
    if os.path.exists("./txt/temp.txt"):
        os.remove("./txt/temp.txt")

    for i in xung_ho2:
        # Luật nhân
        for j in luat_nhan:
            j1 = j.split('=')[0]
            j1_truoc = j1.split('{0}')[0]
            j1_sau = j1.split('{0}')[1]
            
            j2 = j.split('=')[1]
            j2_truoc = j2.split('{0}')[0]
            j2_sau = j2.split('{0}')[1]
            
            if len(j1_truoc) > 0:
                txt = txt.replace(j1_truoc[0].lower() + j1_truoc[1:] + i + j1_sau, j2_truoc + i + j2_sau)
                txt = txt.replace(j1_truoc[0].upper() + j1_truoc[1:] + i + j1_sau, j2_truoc + i + j2_sau)
            else:
                txt = txt.replace(i + j1_sau, j2_truoc + i.lower() + j2_sau)

        for j in sau_name2:
            for k in truoc_name2:
                if (k.find('*') == -1):
                    txt = txt.replace(j + " " + i + " " + k, k + " " + i + " " + (j[0].lower() + j[1:]))
                else:
                    k = k.split('*')[0]
                    txt = txt.replace(j + " " + i + " " + k, k + " của " + i + " " + (j[0].lower() + j[1:]))
            txt = txt.replace(j + " " + i, i + " " + (j[0].lower() + j[1:]))

        for j in truoc_name2:
            if (j.find('*') == -1):
                txt = txt.replace(i + " " + j, j + " " + i.lower())
            else:
                j = j.split('*')[0]       
                txt = txt.replace(i + " " + j, j + " của " + i.lower())  

    name3 = sorted(name3, key=len, reverse=True)
    print(name3)
    print(len(name3))

    for i in name3:
        # Luật nhân
        for j in luat_nhan:
            j1 = j.split('=')[0]
            j1_truoc = j1.split('{0}')[0]
            j1_sau = j1.split('{0}')[1]
            
            j2 = j.split('=')[1]
            j2_truoc = j2.split('{0}')[0]
            j2_sau = j2.split('{0}')[1]
            
            if len(j1_truoc) > 0:
                txt = txt.replace(j1_truoc[0].lower() + j1_truoc[1:] + i + j1_sau, j2_truoc + i + j2_sau)
                txt = txt.replace(j1_truoc[0].upper() + j1_truoc[1:] + i + j1_sau, j2_truoc + i + j2_sau)
            else:
                txt = txt.replace(i + j1_sau, j2_truoc + i + j2_sau)

        for j in sau_name2:
            for k in truoc_name2:
                if (k.find('*') == -1):
                    txt = txt.replace(j + " " + i + " " + k, k + " " + i + " " + (j[0].lower() + j[1:]))
                else:
                    k = k.split('*')[0]
                    txt = txt.replace(j + " " + i + " " + k, k + " của " + i + " " + (j[0].lower() + j[1:]))
            txt = txt.replace(j + " " + i, i + " " + (j[0].lower() + j[1:]))

        for j in truoc_name2:
            if (j.find('*') == -1):
                txt = txt.replace(i + " " + j, j + " " + i)
            else:
                j = j.split('*')[0]       
                txt = txt.replace(i + " " + j, j + " của " + i)  

    # Đổi Nàng -> Cô nếu tích vào ô
    if (var1.get() == 1):
        txt = txt.replace('nàng', 'cô')
        txt = txt.replace('Nàng', 'Cô')
    
    # Auto viết hoa sau dấu "
    txt1 = ''
    for i in txt.split('"'):
        if i != '':
            res = '"' + i[0].upper() + i[1:]
            txt1 += ''.join(res)
    
    # Đổi hội thoại
    txt1 = txt1.replace('."', '.\n')
    txt1 = txt1.replace('!"', '!\n')
    txt1 = txt1.replace('?"', '?\n')
    txt1 = txt1.replace('~"', '~\n')
    txt1 = txt1.replace('~ "', '~\n')
    txt1 = txt1.replace(': "', ':\n- ')
    txt1 = txt1.replace(', "', ':\n- ')
    txt1 = txt1.replace('\n"', '\n- ')
    
    # Nếu dòng đầu là tên chương thì viết hoa
    if (txt1.split('\n')[0].find(':') > -1):
        txt1 = txt1.replace(txt1.split('\n')[0], txt1.split('\n')[0].title())
    
    # Xóa hàng thừa
    txt1 = txt1.replace('\n\n', '\n')
    txt1 = txt1.replace('\n \n', '\n')
    
    # Auto viết hoa đầu dòng
    txt2 = ''
    for i in txt1.split('\n'):
        if i != '':
            if i[0] == ' ' and len(i) > 1:
                res = i[1].upper() + i[2:] + '\n'
            else:
                res = i[0].upper() + i[1:] + '\n'
            txt2 += ''.join(res)
            
    # Auto viết hoa đầu câu
    txt3 = ''
    for i in txt2.split('? '):
        if i != '':
            res = '? ' + i[0].upper() + i[1:]
            txt3 += ''.join(res)
    txt4 = ''
    for i in txt3.split('! '):
        if i != '':
            res = '! ' + i[0].upper() + i[1:]
            txt4 += ''.join(res)
    txt5 = ''
    for i in txt4.split('. '):
        if i != '':
            res = '. ' + i[0].upper() + i[1:]
            txt5 += ''.join(res)
    
    txt5 = txt5.replace('. ! ? "', '')
            
    text2.insert("insert", txt5)

    #Tính thời gian tại thời điểm kết thúc thuật toán
    end_time = time.time()    

    #tính thời gian chạy của thuật toán Python
    elapsed_time = end_time - start_time

    messagebox.showinfo(title="Thành công", message="Thời gian thực hiện: {time:.0f} giây.\n\nBấm OK để tiếp tục!\t\n".format(time = elapsed_time))

def search_name():
    text2.delete("1.0", "end")
    txt = text.get("1.0", "end")

    # Tạo chuỗi trống
    name = ""

    txt = txt.split()
    # Sắp xếp câu
    for i2, i in enumerate(txt):
        # 6 từ viết hoa liên tiếp
        if txt[i2][0].isupper():
            if txt[i2+1][0].isupper():
                if txt[i2+2][0].isupper():
                    if txt[i2+3][0].isupper():
                        if txt[i2+4][0].isupper():
                            if txt[i2+5][0].isupper():
                                if txt[i2+6][0].isupper():
                                    name += txt[i2] + " " + txt[i2+1] + " " + txt[i2+2] + " " + txt[i2+3] + " " + txt[i2+4] + " " + txt[i2+5] + " " + txt[i2+6] + "\n"
                                elif txt[i2+6][0].isupper() == False: 
                                    name += txt[i2] + " " + txt[i2+1] + " " + txt[i2+2] + " " + txt[i2+3] + " " + txt[i2+4] + " " + txt[i2+5] + " " + "\n"
                            elif txt[i2+5][0].isupper() == False:
                                name += txt[i2] + " " + txt[i2+1] + " " + txt[i2+2] + " " + txt[i2+3] + " " + txt[i2+4] + "\n"
                        elif txt[i2+4][0].isupper() == False:
                            name += txt[i2] + " " + txt[i2+1] + " " + txt[i2+2] + " " + txt[i2+3] + "\n"
                    elif txt[i2+3][0].isupper() == False:
                        name += txt[i2] + " " + txt[i2+1] + " " + txt[i2+2] + "\n"
                elif txt[i2+2][0].isupper() == False:
                    name += txt[i2] + " " + txt[i2+1] + "\n"
            elif txt[i2+1][0].isupper() == False:
                name += ""

        # 2 từ viết hoa liên tiếp + xưng hô với người
        if txt[i2-3][0].isupper() == False and txt[i2-2][0].isupper() and txt[i2-1][0].isupper() and (txt[i2] + " " + txt[i2+1] == "sư huynh" or txt[i2] + " " + txt[i2+1] == "sư đệ" or txt[i2] + " " + txt[i2+1] == "sư muội" or txt[i2] + " " + txt[i2+1] == "sư phụ"):
            name += txt[i2-2] + " " + txt[i2-1] + " " + txt[i2] + " " + txt[i2+1] + "\n"
        # 1 từ viết hoa liên tiếp + xưng hô với người
        if txt[i2-2][0].isupper() == False and txt[i2-1][0].isupper() and (txt[i2] + " " + txt[i2+1] == "sư huynh" or txt[i2] + " " + txt[i2+1] == "sư đệ" or txt[i2] + " " + txt[i2+1] == "sư muội" or txt[i2] + " " + txt[i2+1] == "sư phụ"):
            name += txt[i2-1] + " " + txt[i2] + " " + txt[i2+1] + "\n"
        # 2 từ viết hoa liên tiếp + hậu tố
        if txt[i2-2][0].isupper() and txt[i2-1][0].isupper() and (txt[i2] == "tông" or txt[i2] == "thành" or txt[i2] == "trấn" or txt[i2] == "sơn" or txt[i2] == "thôn"):
            name += txt[i2-2] + " " + txt[i2-1] + " " + txt[i2] + "\n"

    name2= ''
    for i in name.split('\n'):
        if name2.find(i) == -1:
            name2 += i + '\n'
    name = name2

    text2.insert("insert", name)
    messagebox.showinfo(title="Thành công", message="Đã xử lý thành công")

def load_chuong(id):
    text.delete("1.0", "end")
    x = text3.get()
    txt = open('D:/TRUYEN_YY/' + id + '/CV/Chương ' + x + '.txt', 'r', encoding="utf-8")
    text.insert("insert", txt.read())

def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

def check(file_txt, inp, outp, add):
    with open(file_txt, 'r', encoding="utf-8") as file:
        # read all content from a file using read()
        content = file.readlines()
        # check if string present or not
        if (add in content) == True or (add + '\n' in content) == True:
            print(add, 'đã tồn tại trong', outp)
        else:
            print('Đã thêm vào', outp, ':', add)
            with open(file_txt, 'a', encoding="utf-8") as f:
                f.write('\n' + add)
                f.close()

def add_replace():
    def add_replace_name():
        status = ''
        old = e1.get()
        new = e2.get()
        inp = old.strip() + '=' + new
        if (new != ''):
            if (old != ''):
                check('./txt/replace.txt', inp, 'Replace', inp.strip())
                status += 'Đã thêm ' + inp + ' vào file Replace\n'
            if (var.get() == 1 or old == ''):
                check('./txt/name.txt', new, 'Name', new.strip())
                status += 'Đã thêm ' + new + ' vào file Names\n'
        else:
            status = 'Vui lòng nhập từ mới'
        l4.config(text = status)

    newWindow = Toplevel(root)
    newWindow.title("Add Replace")

    # newWindow.geometry("500x300")

    l1 = Label(newWindow, text ="Từ gốc: ", font=("Arial", 16))
    l2 = Label(newWindow, text ="Từ mới: ", font=("Arial", 16))
    l1.grid(row=1, column=0, padx=4, pady=4)
    l2.grid(row=2, column=0, padx=4, pady=4)
    
    e1 = Entry(newWindow)
    e2 = Entry(newWindow)
    e1.grid(row=1, column=1, padx=4, pady=4, columnspan=5)
    e2.grid(row=2, column=1, padx=4, pady=4, columnspan=5)

    var = IntVar()
    c = Checkbutton(newWindow, text='Thêm từ này vào Names', variable=var)
    c.grid(row=3, column=1, pady=2)

    l3 = Label(newWindow, text ="Status: ", font=("Arial", 16))
    l4 = Label(newWindow, font=("Arial", 14))
    l3.grid(row=4, column=0, padx=4, pady=4)
    l4.grid(row=4, column=1, padx=4, pady=4, rowspan=2)

    button = Button(newWindow, text = "ADD", font=("Arial Bold", 18), command=lambda: add_replace_name())
    button.grid(row=7, column=0, pady=2)
    
    if text.selection_get():
        data = text.selection_get() # copy selected text to clipboard
        e1.insert(0, data)
    # elif text2.selection_get():
    #     data2 = text2.selection_get() # copy selected text to clipboard
    #     e2.insert(0, data2)

def add_names():
    def add_name():
        old = e1.get("1.0", "end")
        old = old.split('\n')
        for i in old:
            if i != '':
                inp = i.strip()
                check('./txt/name.txt', inp, 'Name', inp.strip())
        e1.delete("1.0", "end")
            
    newWindow = Toplevel(root)
    newWindow.title("Add Names")

    # newWindow.geometry("500x300")

    l1 = Label(newWindow, text ="Nhập mỗi Name một dòng", font=("Arial", 16))
    l1.grid(row=0, column=0, pady=4)
    
    e1 = Text(newWindow)
    e1.grid(row=1, column=0, columnspan=2, rowspan=2)

    l3 = Label(newWindow, text ="Status: ", font=("Arial", 16))
    l4 = Label(newWindow, font=("Arial", 14))
    l3.grid(row=3, column=0, pady=4)
    l4.grid(row=3, column=1, pady=4, rowspan=2)

    button = Button(newWindow, text = "ADD", font=("Arial Bold", 18), command=lambda: add_name())
    button.grid(row=4, column=0, pady=2)
    
root = Tk()
root.title('Replace Tool')
root.geometry("1280x400")
# root.iconbitmap("myIcon.ico")

my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Search Name", command=lambda: search_name())
file_menu.add_command(label="Add Name to Name.txt", command=lambda: add_name())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

list_truyen_menu = Menu(my_menu)
my_menu.add_cascade(label="List Truyện", menu=list_truyen_menu)
list_truyen_menu.add_command(label="Khí Vận" , command=lambda: load_chuong('KHÍ VẬN'))
list_truyen_menu.add_command(label="Thần Khí", command=lambda: load_chuong('THẦN KHÍ'))

my_menu.add_command(label="Search Name", command=lambda: search_name())
my_menu.add_command(label="Add Name", command=lambda: add_name())

# Create Menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_separator()
help_menu.add_command(label="Exit", command=root.quit)

my_menu.add_command(label="Add Replace", command=lambda: add_replace())

l1 = Label( root, text = "Nhập Nội Dung", font=("Arial", 16))
l2 = Label( root, text = "Kết Quả", font=("Arial", 16))

l1.place(height=24, width=200, x=180, y=0)
l2.place(height=24, width=200, x=900, y=0)

text = Text(root, wrap=WORD)
text2 = Text(root, wrap=WORD)
text3 = Entry(root)

text.place(height=350, width=550, x=10, y=30)
text2.place(height=350, width=550, x=720, y=30)
text3.place(height=24, width=60, x=610, y=0)

list_truyen = ['Chọn truyện', 'KHÍ VẬN', 'THẦN KHÍ']

# select.insert(END, "Chọn truyện:")
# for p in list_truyen:
#     select.insert(END, p)

button = Button(text = "OK", font=("Arial Bold", 18), command=lambda: edit_text())
button.place(height=50, width=60, x=610, y=200)

var1 = IntVar()
c1 = Checkbutton(root, text='Nàng -> Cô', variable=var1)
c1.place(height=30, width=120, x=570, y=150)

m = Menu(root, tearoff = 0)
m.add_command(label ="Add Replace", command=lambda:add_replace())
m.add_command(label ="Add Names", command=lambda:add_names())
m.add_separator()
m.add_command(label ="Thôi")

root.bind("<Button-3>", do_popup)
# btn = Button(root,
#              text ="Click to open a new window",
#              command = openNewWindow)
# btn.grid(row=3, column=1, pady=2)

mainloop()
