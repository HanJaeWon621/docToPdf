
host  =''    # MySQL 호스트 주소
user  =''  # MySQL 사용자 이름
password =''   # MySQL 비밀번호
database =''   # 사용할 데이터베이스 이름
with open("c:/pdf/envinfo/host.dat", "r") as dbinfo_file:
    host = dbinfo_file.read()  
    
with open("c:/pdf/envinfo/user.dat", "r") as dbinfo_file:
    
    user = dbinfo_file.read()
    
with open("c:/pdf/envinfo/password.dat", "r") as dbinfo_file:
    password = dbinfo_file.read()
    
with open("c:/pdf/envinfo/database.dat", "r") as dbinfo_file:
    database = dbinfo_file.read()