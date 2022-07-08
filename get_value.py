from datetime import datetime
from re import T

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
    answer_type = "%Y/%m/%d %H:%M"
    date_format_elements = [year,month,day,hour,minute]
    separates = [
        ["",""],
        ["/","/"],
        ["年","月"],
        ["-","-"," ",":"],
        ["/","/"," ",":"],
        ["年","月","時","分"]
    ]
    for now in separates:
        now_len = int(len(now))
        for bit in range(2**now_len):
            now_format = ""
            for index, element in enumerate(date_format_elements[:len(now)+1]):
                if(((bit >> index) & 1) < len(element)):
                    now_format += element[(bit >> index) & 1]
                    if(index < now_len):
                        now_format += now[index]
                if(index == now_len):
                    print(now_format)
                    if(get_date_time(date_str,now_format) == True):
                        print("true type is {}".format(now_format))
                        res_data = datetime.strptime(date_str,now_format)
                        return datetime.strftime(res_data,answer_type)
    return False

test = "2020510"
print(parse_date_time(test))