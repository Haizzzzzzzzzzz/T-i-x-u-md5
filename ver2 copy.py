import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


import pyautogui
import time
import pyperclip
import keyboard
import csv
import binascii
import re
import datetime


money = 100000
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
history = False
attack = True
reset = False
x2 = 1
# while True:
#     # Kiểm tra xem phím "q" đã được nhấn hay chưaq
#     if keyboard.is_pressed("q"):
#         break
#     # Lấy tọa độ hiện tại của con trỏ chuột
#     current_position = pyautogui.position()
#     print(current_position)


# Hàm chuyển đổi chuỗi thời gian sang dạng số giây
# def time_to_seconds(time_str):
#     if ':' not in time_str:
#         return 0  # Hoặc giá trị khác tùy ý nếu không muốn đặt giá trị 0
#     h, m, s = map(int, time_str.split(':'))
#     return h * 3600 + m * 60 + s

while (money <= 500000):
    #  # Đặt thời gian chờ là 1 phút (60 giây)
    # waiting_time = 15
    # # Chờ đợi trong 1 phút
    # time.sleep(waiting_time)

    # Di chuyển chuột đến tọa độ (x, y) và bấm chuột trái
    file_data1 = "output1.csv"
    file_data2 = "output2.csv"
    # file_data3 = "test3.csv"
    target_position = (1424, 629)
    pyautogui.moveTo(*target_position)
    pyautogui.click()

    # Paste dữ liệu từ clipboardq
    data_pasted = pyperclip.paste()

    while data_pasted[0] == "{":
        if ((data_pasted[0] != "{")):
            break
        target_position = (1424, 629)
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


  
    # Đọc dữ liệu từ tệp CSV vào DataFrame
    data1 = pd.read_csv(file_data1, header=None)  # Không có dòng tiêu đề trong tệp CSV
    data2 = pd.read_csv(file_data2, header=None)  # Không có dòng tiêu đề trong tệp CSV
    # data3 = pd.read_csv(file_data3, header=None)

    # Chuyển đổi dữ liệu đầu ra thành mảng 1D
    output_data = data2.values.ravel()

    # Xóa cột đầu ra khỏi DataFrame data1 (nếu cần)
    # data1 = data1.drop(columns=[output_column_index])  # Thay output_column_index bằng chỉ số cột chứa đầu ra
    # Chuyển đổi chuỗi thời gian sang dạng số
    ####################
    # Chuyển đổi chuỗi thời gian sang dạng số
    # time_data = data3[0].apply(str).apply(time_to_seconds) 

    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    # X_train, X_test, y_train, y_test, time_train, time_test = train_test_split(
    # data1, output_data, time_data, test_size=0.2, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(
    data1, output_data, test_size=0.2, random_state=42)

    # Chuẩn hóa dữ liệu huấn luyện và kiểm tra
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Khởi tạo mô hình MLP
    model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=50000, learning_rate='adaptive',learning_rate_init=0.002, solver='adam')

    # Huấn luyện mô hình với dữ liệu huấn luyện
    model.fit(X_train_scaled, y_train)

    # Dữ liệu 1 mới cần được mã hóa và chuẩn hóa
    new_data = np.array([decimal_values])
    new_data_scaled = scaler.transform(new_data)

    # Dự đoán kết quả dữ liệu 2
    predicted_output = model.predict(new_data_scaled)

    # Tính phần trăm đúng trên tập kiểm tra
    accuracy = model.score(X_test_scaled, y_test) * 100

    vong = vong+1

    print("Độ chính xác trên tập kiểm tra: %.2f%%" % accuracy)
    print("Dự đoán kết quả dữ liệu 2: ", predicted_output)
    # Tên file CSV để lưu dữ liệu
    csv_file = 'output1.csv'

    # Mở file CSV trong chế độ ghi ('w') và tạo writer object
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi tiêu đề của cột
        # writer.writerow(['Decimal Values'])

        # Ghi các giá trị số thập phân vào file CSV
        writer.writerow(decimal_values)

    csv_file = 'test3.csv'

    # Mở file CSV trong chế độ ghi ('w') và tạo writer object
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi tiêu đề của cột
        # writer.writerow(['Decimal Values'])

        # Ghi các giá trị số thập phân vào file CSV
        writer.writerow(datetime.datetime.now().strftime("%H:%M:%S"))
    #######################################################
    if((vong_lt >= 10 and win >= 7) or (win_lt >= 5)):
        attack = True
    elif (win_lt >= 5):
        attack = True
    elif (win >= lose*4):
        attack = True
    elif (dung > sai*3):
        attack = True
    else: attack = False
    #######################################################
    if (attack):
        if (predicted_output == 1):
            target_position = (1152, 526)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 1
            target_position = (1062,664)
            pyautogui.moveTo(*target_position)
            pyautogui.click()
            waiting_time = 1
            for i in range(1, x2 + 1):
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
            waiting_time = 1
            for i in range(1, x2 + 1):
                target_position = (1285, 712)
                pyautogui.moveTo(*target_position)
                pyautogui.click()
            print("Bạn vừa đánh xỉu")
            check = True

    if data_pasted is not None:
        # waiting_time_kq = 49

        # time.sleep(waiting_time_kq)

        # Di chuyển chuột đến tọa độ (x, y) và bấm chuột trái
        target_position = (1424, 629)
        pyautogui.moveTo(*target_position)
        pyautogui.click()

        # Paste dữ liệu từ clipboardq
        string = pyperclip.paste()

        while string[0] != "{":
            if ((string[0] == "{")):
                break
            target_position = (1424, 629)
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
    

    if (predicted_output == kq):
        if (check == True):
            money = money+(4900*x2)
            print("Húp 4900 vào lúc: ", datetime.datetime.now().strftime("%H:%M:%S"))
        x2 = 1
        win = win + 1
        vong_lt = vong_lt + 1
        win_lt = win_lt + 1
        lose_lt = 0
        dung = dung+1
        history = True
        
            
    else:
        print("x2: "+str(x2))
        money = money - (5000*x2)
        print("Bạn choi ngu vừa mất 5000 vào lúc: ", datetime.datetime.now().strftime("%H:%M:%S"))
        x2 = x2*2
        lose = lose + 1
        vong_lt = vong_lt + 1
        lose_lt = lose_lt + 1
        win_lt = 0
        sai = sai + 1
        history = False
        
            
    #######################################################
    if(lose_lt >= 3):
        reset = True
    elif(lose == win & vong_lt >= 10):
        reset = True
    elif(lose > win & lose >= 5):
        reset = True
    else:
        reset = False
    #######################################################       
    if (reset):
        win = 0
        lose = 0
        win_lt = 0
        lose_lt = 0
        vong = 0
        vong_lt = 0
        check = False
    
    # Tên file CSV để lưu dữ liệu
    csv_file = 'LichSu.csv'

    # Các giá trị cần ghi vào tệp
    predicted_output_value = str(predicted_output)
    kq_value = str(kq)
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    accuracy_value = str(accuracy)


    # Tạo danh sách chứa các giá trị cần ghi
    data_to_write = [predicted_output_value, kq_value, time_now, accuracy_value,str(history),str(money)]

    # Mở file CSV trong chế độ ghi ('a') và tạo đối tượng writer
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi danh sách các giá trị vào tệp
        writer.writerow(data_to_write)

    check = False

    print("Chuỗi kết quả"+string)
    print("Kết quả cuối cùng: "+str(total))

    print("win :"+str(win))
    print("lose :"+str(lose))
    print("win_lt :"+str(win_lt))
    print("lose_lt :"+str(lose_lt))
    print("vong :"+str(vong))
    print("vong_lt :"+str(vong_lt))
    print("Số lần đoán đúng :"+str(dung))
    print("Số lần đoán sai :"+str(sai))
    print("Money :"+str(money))
