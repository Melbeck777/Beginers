from datetime import datetime
from re import T
from textwrap import indent

def get_date_time(date_str,date_format):
    try:
        res_date = datetime.strptime(date_str,date_format)
        return True
    except:
        return False

def parse_date_time(date_str):
    year = ["%y", "%Y"]
    month = ["%m"]
    day = ["%d"]
    hour = ["%H"]
    minute = ["%M"]
    # 日付の出力形式
    answer_type = "%Y/%m/%d %H:%M"
    # 日付を解析するための各単位での要素
    date_format_elements = [year,month,day,hour,minute]
    # 年，月，日，時，分をそれぞれ区切り
    separates = [
        ["",""],
        ["/","/"],
        ["年","月","日"],
        ["-","-"," ",":"],
        ["/","/"," ",":"],
        ["年","月","日","時","分"]
    ]
    for now_index,now in enumerate(separates):
        now_len = int(len(now))
        put_flag = 0
        index_flag = 1
        if((now_index - 2) < 0 and (now_index -2)%3 != 0):
            put_flag = 1
            index_flag = 0
        for bit in range(2**now_len):
            now_format = ""
            for index, element in enumerate(date_format_elements[:len(now)+put_flag]):
                if(((bit >> index) & 1) < len(element)):
                    now_format += element[(bit >> index) & 1]
                    if(index < now_len):
                        now_format += now[index]
                else:
                    break
                if(index == now_len-index_flag):
                    if(get_date_time(date_str,now_format) == True):
                        print("true type is {}".format(now_format))
                        res_data = datetime.strptime(date_str,now_format)
                        return datetime.strftime(res_data,answer_type)
    return False

test = ["2020年5月10日","2020510","2020/5/10","2020-5-10"]
for it in test:
    print(parse_date_time(it))