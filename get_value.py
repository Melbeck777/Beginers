from datetime import date, datetime
import locale
from time import time

def Get_date_time(date_str,date_format):
    try:
        res_date = datetime.strptime(date_str,date_format)
        return True
    except:
        return False

# 曜日を除外した日付の文字列を生成
def separate_and_connect(date_str):
    first_separate = date_str.split("(")
    second_separate = first_separate[1].split(")")
    res = first_separate[0][:-1]+second_separate[1]
    print("res date = {}".format(res))
    return res

def answer_type_date(date_str,date_format):
    # 日付の出力形式
    answer_type = "%Y/%m/%d %H:%M"
    res_date = datetime.strptime(date_str,date_format)
    res = datetime.strftime(res_date,answer_type)
    return res

def Get_date_format(date_separates):
    # print("{}, {}".format(date_separates,len(date_separates)))
    year = ["%y", "%Y"]
    month = ["%m"]
    day = ["%d"]
    date_format = [year,month,day]
    res = []
    for now_index, now_element in enumerate(date_separates):
        now_len = int(len(now_element))
        for bit in range(2**now_len):
            flag = True
            now_format = ""
            for index, element in enumerate(date_format):
                element_access = (bit << index) & 1
                # print("{} < {}".format(element_access,len(element)))
                if(element_access < len(element)):
                    now_format += element[element_access]
                    if(index < now_len):
                        now_format += now_element[index]
                else:
                    flag = False
                    break
            if(flag == True):
                res.append(now_format)
    return res

def Get_time_format(time_separates):
    # print("{}, {}".format(time_separates,len(time_separates)))
    hour = ["%H"]
    minute = ["%M"]
    time_format = [hour,minute]
    res = []
    for now_index, now_element in enumerate(time_separates):
        now_len = int(len(now_element))
        # print(now_len)
        for bit in range(2**now_len):
            now_format = ""
            flag = True
            for index, element in enumerate(time_format):
                element_access = (bit << index) & 1
                if(element_access < len(element)):
                    now_format += element[element_access]
                    if(index < now_len):
                        now_format += now_element[index]
                else:
                    flag = False
                    break
            if(flag == True):
                res.append(now_format)
    return res

def Get_english_date(date_str):
    # Get English datetime
    date_separates = [
        ["",""],
        ["-","-"],
        ["/","/"]
    ]
    date_formats = Get_date_format(date_separates)
    time_separates = [[":"]]
    time_formats = Get_time_format(time_separates)
    # print("english date formats = {}".format(date_formats))
    # print("english time formats = {}".format(time_formats))
    for now_date in date_formats:
        for now_time in time_formats:
            now_format = now_date+now_time
            # print("now_format = {}".format(now_format))
            if(Get_date_time(date_str,now_format) == True):
                return answer_type_date(date_str,now_format)
    return False

def Get_japanese_date(date_str):
    # locale.setlocale(locale.LC_TIME,'ja_JP.UTF-8')
    date_separates = [
        ["年","月","日"],
    ]
    time_separates = [["時","分"]]
    date_formats = Get_date_format(date_separates)
    time_formats = Get_time_format(time_separates)
    # print("date_formats = {}".format(date_formats))
    # print("time_formats = {}".format(time_formats))
    for now_date in date_formats:
        for now_time in time_formats:
            now_format = now_date+now_time
            if(Get_date_time(date_str,now_format) == True):
                return answer_type_date(date_str,now_format)
    return False

def parse_date_time(date_str):
    easy_date = separate_and_connect(date_str)
    res = Get_english_date(easy_date)
    if(res == False):
        return Get_japanese_date(easy_date)
    else:
        return res
# タスク
#   金額，個数，店名の取得
#   処理の結果をどう返せばいいのか？
#   結果をどういう形にして保存するか

# test = ["2020年5月10日 14時00分","2020510 14:00","2020/5/10 14:00","2020-5-10 14:00"]
test = ["2020年5月10日 (土)14時00分","2020510 (Sat)14:00"]
for it in test:
    print(parse_date_time(it))