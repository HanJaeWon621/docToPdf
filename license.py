from enc_dec import *
import datetime

# 사용 일자 체크 데모버전, 운영 버전
def check_licence_date():
    # 현재 시간을 얻기
    now = datetime.datetime.now()
    
    # 년, 월, 일, 시, 분, 초 얻기
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    file_postfix = str(year) + '' + str(month) + '' + str(day) + '' + str(hour) + '' + str(minute) + '' + str(second)
    
    # 년, 월, 일, 시, 분, 초 얻기


    year_s =str(year)
    month_s =''
    day_s =''
    date_s=''
    if month < 10:
        month_s = '0'+str(month)
    else:
        month_s = str(month)
    if day < 10:
        day_s = '0'+str(day)
    else:
        day_s = str(day)

    date_s = year_s + month_s + day_s
    date_int =  int(date_s)
    dec_str = get_dec()
    dec_str_int = int(dec_str)
    check=0
    if date_int > dec_str_int: #라이센스 기한 초과
        check=1
    else:
        check=0
    
    return check

def get_file_postfix():
    # 현재 시간을 얻기
    now = datetime.datetime.now()
    
    # 년, 월, 일, 시, 분, 초 얻기
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    file_postfix = str(year) + '_' + str(month) + '' + str(day) + '' + str(hour) + '' + str(minute) + '' + str(second)
    return file_postfix
if __name__ == "__main__":
    print('license check:', check_licence_date())