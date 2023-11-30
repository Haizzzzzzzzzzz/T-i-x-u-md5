import pyautogui
import time
import pyperclip
import keyboard
import csv
from sklearn import tree
import binascii
import re
import pandas as pd
import numpy as np
import datetime


money = 75100
win = 0
lose = 0
win_lt = 0
lose_lt = 0
vong = 0
vong_lt = 0
copy = 0
dung = 0
sai = 0
check = False


while True:
    # Kiểm tra xem phím "q" đã được nhấn hay chưaq
    if keyboard.is_pressed("q"):
        break
    # Lấy tọa độ hiện tại của con trỏ chuột
    current_position = pyautogui.position()
    print(current_position)

while (money <= 500000):
    # Đặt thời gian chờ là 1 phút (60 giây)
    # waiting_time = 14
    # # Chờ đợi trong 1 phút
    # time.sleep(waiting_time) 1426/611

    # Di chuyển chuột đến tọa độ (x, y) và bấm chuột trái
    target_position = (1426, 611)
    pyautogui.moveTo(*target_position)
    pyautogui.click()

    # Paste dữ liệu từ clipboardq
    data_pasted = pyperclip.paste()

    while data_pasted[0] == "{":
        if ((data_pasted[0] != "{")):
            break
        target_position = (1426, 611)
        waiting_time = 12
        time.sleep(waiting_time)
        pyautogui.moveTo(*target_position)
        pyautogui.click()

        # Paste dữ liệu từ clipboardq
        data_pasted = pyperclip.paste()

    # In ra dữ liệu đã được paste
    print("Chuỗi đầu: "+data_pasted)

    # Chuyển đổi chuỗi hex sang dạng byte
    md5_byte = binascii.unhexlify(str(data_pasted))

    # Chuyển đổi các byte thành các giá trị số thập phân
    decimal_values = []
    for b in md5_byte:
        decimal_values.append(int(b))

    # Đọc dữ liệu từ file CSV vào DataFrame
    df_dactrung = pd.read_csv('output1.csv')
    df_nhan = pd.read_csv('output2.csv')

    # Chuyển đổi DataFrame thành mảng numpy
    dactrung = df_dactrung.to_numpy()
    nhan = df_nhan.to_numpy()

    # Khởi tạo mô hình DecisionTreeClassifier và fit dữ liệu
    my_tree = tree.DecisionTreeClassifier()
    result = my_tree.fit(dactrung, nhan)

    # Dự đoán kết quả cho một dữ liệu mới
    new_data = np.array([decimal_values])
    print("new_data: ", new_data)
    kq_dd = result.predict(new_data)

    # Tính toán độ chính xác trên dữ liệu đào tạo
    accuracy = result.score(dactrung, nhan)
    print("Độ chính xác của kết quả dư đoán:", accuracy*100)

    # Tên file CSV để lưu dữ liệu
    csv_file = 'output1.csv'

    # Mở file CSV trong chế độ ghi ('w') và tạo writer object
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi tiêu đề của cột
        # writer.writerow(['Decimal Values'])

        # Ghi các giá trị số thập phân vào file CSV
        writer.writerow(decimal_values)
    print("Mã hóa chuỗi đầu: "+str([decimal_values]))
    print("Kết quả dự đoán là: "+str(kq_dd))

    if ((vong_lt >= 10 & win >= 7) | (win_lt >= 5)):
        if (kq_dd == 1):
            target_position = (1152, 526)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 1
            target_position = (1062,664)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 1
            target_position = (1285, 712)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            print("Bạn vừa đánh tài")
            check = True
        else: #5k: 1062,664; 10k = 1129,661
            target_position = (1440, 520)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 2
            target_position = (1062,664)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 2
            target_position = (1285, 712)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            print("Bạn vừa đánh xỉu")
            check = True
    

    if data_pasted is not None:
        # waiting_time_kq = 48

        # time.sleep(waiting_time_kq)

        # Di chuyển chuột đến tọa độ (x, y) và bấm chuột trái
        target_position = (1426, 611)
        pyautogui.moveTo(*target_position)
        pyautogui.click()

        # Paste dữ liệu từ clipboardq
        string = pyperclip.paste()

        while string[0] != "{":
            if ((string[0] == "{")):
                break
            target_position = (1426, 611)
            waiting_time = 12
            time.sleep(waiting_time)
            pyautogui.moveTo(*target_position)
            pyautogui.click()

            # Paste dữ liệu từ clipboardq
            string = pyperclip.paste()

        # Tìm chuỗi con nằm trong ngoặc {}
        start_index = string.find("{") + 1
        end_index = string.find("}")
        number_string = string[start_index:end_index]

        # Tách chuỗi thành các số con dựa trên dấu gạch ngang "-"
        numbers = number_string.split("-")

        # Chuyển đổi từng số con thành số nguyên và tính tổng
        total = sum(map(int, numbers))

        kq = 0
        if total <= 10:
            kq = 0
        else:
            kq = 1

        # Tên file CSV để lưu dữ liệu
        csv_file = 'output2.csv'

        # Mở file CSV trong chế độ ghi ('w') và tạo writer object
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)

            # Ghi tiêu đề của cột
            # writer.writerow(['Result'])

            # Ghi các giá trị số thập phân vào file CSV
            writer.writerow(str(kq))

        print("Chuỗi kết quả"+string)
        print("Kết quả cuối cùng: "+str(total))

    if (kq_dd == kq):
        win = win + 1
        vong_lt = vong_lt + 1
        win_lt = win_lt + 1
        lose_lt = 0
        dung = dung+1
        print("Bạn vừa ăn nhưng đéo tiền", datetime.datetime.now().strftime("%H:%M:%S"))
        if (check == True):
            money = money+4900
            print("Húp 4900 vào lúc: ", datetime.datetime.now().strftime("%H:%M:%S"))
    else:
        lose = lose + 1
        vong_lt = vong_lt + 1
        lose_lt = lose_lt + 1
        win_lt = 0
        sai = sai + 1
        print("Bạn đéo ăn nhưng đqéo mất tiền", datetime.datetime.now().strftime("%H:%M:%S"))
        if (check == True):
            money = money - 5000
            print("Bạn choi ngu vừa mất 5000 vào lúc: ", datetime.datetime.now().strftime("%H:%M:%S"))

    check = False

    if ((lose_lt >= 3) | (lose == win & vong_lt >= 10) | (lose > win & lose >= 5)):
        win = 0
        lose = 0
        win_lt = 0
        lose_lt = 0
        vong = 0
        vong_lt = 0
        check = False

    print("win :"+str(win))
    print("lose :"+str(lose))
    print("win_lt :"+str(win_lt))
    print("lose_lt :"+str(lose_lt))
    print("vong :"+str(vong))
    print("vong_lt :"+str(vong_lt))
    print("Số lần đoán đúng :"+str(dung))
    print("Số lần đoán sai :"+str(sai))
    print("Money :"+str(money))

    # money = money + 100

    # Copy dữ liệu vào clipboard
    # data_to_copy = "target_position"
    # pyperclip.copy(data_to_copy)
