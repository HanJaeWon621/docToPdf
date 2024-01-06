cafe24url  =''    # qr이미지 스캔시 pdf다운처리 프로그램
awsbucket  =''
with open("c:/pdf/envinfo/cafe24url.dat", "r") as cafe24url_file:
    cafe24url = cafe24url_file.read()

with open("c:/pdf/envinfo/awsbucket.dat", "r") as awsbucket_file:
    awsbucket = awsbucket_file.read()  