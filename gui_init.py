import tkinter as tk
from tkinter import ttk, messagebox


window = tk.Tk()
window.title("DOCX를 PDF로 변환합니다.")
# 수직 레이아웃을 위한 Frame 생성
vertical_layout = tk.Frame(window)
vertical_layout.grid(row=0, column=0, padx=10, pady=5)

# 수평 레이아웃 1 - 버튼 4개 추가
horizontal_layout1 = tk.Frame(vertical_layout)
horizontal_layout1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
btnSelectDocxFile          = tk.Button(horizontal_layout1, text="대상파일조회", padx=5, pady=5)
btnDelFile                 = tk.Button(horizontal_layout1, text="대상파일삭제", padx=5, pady=5)
btnAllSelFile              = tk.Button(horizontal_layout1, text="전체선택/해제", padx=5, pady=5)

btnDisplayConvertedPdfFile = tk.Button(horizontal_layout1, text="변환파일조회", padx=5, pady=5)
btnDelConvertedFile        = tk.Button(horizontal_layout1, text="변환파일삭제", padx=5, pady=5)
btnAllSelConvertedFile     = tk.Button(horizontal_layout1, text="전체선택/해제", padx=5, pady=5)

btnDisplaySendPdfFile      = tk.Button(horizontal_layout1, text="전송파일조회", padx=5, pady=5)
btnDelSendFile             = tk.Button(horizontal_layout1, text="전송파일삭제", padx=5, pady=5)
btnAllSelSendFile          = tk.Button(horizontal_layout1, text="전체선택/해제", padx=5, pady=5)

btnSelectDocxFile.grid(row=0, column=0, padx=(40,10), pady=10)
btnDelFile.grid(row=0, column=1, padx=(0,10), pady=10)
btnAllSelFile.grid(row=0, column=2, padx=0, pady=10)

btnDisplayConvertedPdfFile.grid(row=0, column=3, padx=(110, 10), pady=10)
btnDelConvertedFile.grid(row=0, column=4, padx=(0,10), pady=10)
btnAllSelConvertedFile.grid(row=0, column=5, padx=0, pady=10)

btnDisplaySendPdfFile.grid(row=0, column=6, padx=(110, 10), pady=10)
btnDelSendFile.grid(row=0, column=7, padx=(0,10), pady=10)
btnAllSelSendFile.grid(row=0, column=8, padx=0, pady=10)



# 수평 레이아웃 3 - 라벨 추가
horizontal_layout3 = tk.Frame(vertical_layout)
horizontal_layout3.grid(row=1, column=0, padx=0, pady=0)
label1 = tk.Label(horizontal_layout3, text="            변환대상파일                                                                  ")
label2 = tk.Label(horizontal_layout3, text="                변환파일(전송전)                                                                 ")
label3 = tk.Label(horizontal_layout3, text="              변환파일(전송완료)                                                        ")
label1.grid(row=1, column=0, padx=0, pady=0)
label2.grid(row=1, column=2, padx=0, pady=0)
label3.grid(row=1, column=4, padx=0, pady=0)


# 수평 레이아웃 2 - 리스트 박스 2개 추가
horizontal_layout2 = tk.Frame(vertical_layout)

horizontal_layout2.grid(row=2, column=0, padx=10, pady=10)
listbox1 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
btnConvertDocxToPdf              = tk.Button(horizontal_layout2, text="파일변환->", padx=5, pady=5)
# 버튼의 글자 크기와 색상 설정
btnConvertDocxToPdf.config(font=("Gothic", 13), fg="blue")
listbox2 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
btnSendFile                = tk.Button(horizontal_layout2, text="파일전송->", padx=5, pady=5)
# 버튼의 글자 크기와 색상 설정
btnSendFile.config(font=("Gothic", 13), fg="blue")
listbox3 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
listbox1.grid(row=0, column=0, padx=1, pady=5)
btnConvertDocxToPdf.grid(row=0, column=1, padx=10, pady=5)
listbox2.grid(row=0, column=2, padx=1, pady=5)
btnSendFile.grid(row=0, column=3, padx=10, pady=5)
listbox3.grid(row=0, column=4, padx=1, pady=5)


# 수평 레이아웃 3 - 라벨 추가
horizontal_layout3 = tk.Frame(vertical_layout)
horizontal_layout3.grid(row=3, column=0, padx=10, pady=10)
label = tk.Label(horizontal_layout3, text="")
label.grid(row=0, column=0, padx=10, pady=10)

# PDF 폴더 경로
wokr_root_folder = "C:\\pdf"
pdf_temp_folder = wokr_root_folder +"\\temppdf"  # PDF 폴더 경로를 적절히 수정하세요.
pdf_folder_out =  wokr_root_folder +"\\outpdf"  # 변환된 폴더.
pdf_folder_sendout =  wokr_root_folder +"\\sendpdf"  # 변환된 폴더.
docx_folder =  wokr_root_folder +"\\workdocx"  # 작업 폴더.
qr_folder =  wokr_root_folder +"\\qrimg" #qrimg폴더
docx_folder_out =   wokr_root_folder +"\\outdocx"

#기능 문서 전자서명 처리
jar=wokr_root_folder +"\\sign\\open-pdf-sign.jar" #수행 프로그램
crt=wokr_root_folder +"\\sign\\cert.cer" #인증서 파일
pem=wokr_root_folder +"\\sign\\private_key.pem" # 개인키

def select_all_items1():
    selected_indices = listbox1.curselection()
    count = len(selected_indices)
    if count == 0:
        for i in range(listbox1.size()):
            listbox1.select_set(i)
    else:
        listbox1.selection_clear(0, tk.END)
    
def select_all_items2():
    selected_indices = listbox2.curselection()
    count = len(selected_indices)
    if count == 0:
        for i in range(listbox2.size()):
            listbox2.select_set(i)
    else:
        listbox2.selection_clear(0, tk.END)

def select_all_items3():
    selected_indices = listbox3.curselection()
    count = len(selected_indices)
    if count == 0:
        for i in range(listbox3.size()):
            listbox3.select_set(i)
    else:
        listbox3.selection_clear(0, tk.END)

def setFileInfo():
  dispStr = "변환대상파일 : " + str(listbox1.size()) + "개" + " || 변환완료파일 : " + str(listbox2.size()) + "개" + " || 전송완료파일 : " + str(listbox3.size()) + "개"
  label.config(text=dispStr)
def show_alert(msg):
    messagebox.showinfo("알림", msg)