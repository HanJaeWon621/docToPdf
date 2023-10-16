import tkinter as tk
import os
import win32com.client as win32
from pdf2docx import Converter
from docx2pdf import convert
import fitz
#import PyPDF2
import qrcode
import shutil
from PIL import Image
#from upload_file import *
from db_insert import *
from upload_aws import *
from enc_dec import *
from e_sign import *
from license import *
# tkinter 윈도우 생성
window = tk.Tk()
window.title("DOCX를 PDF로 변환합니다.")

# 수직 레이아웃을 위한 Frame 생성
vertical_layout = tk.Frame(window)
vertical_layout.grid(row=0, column=0, padx=10, pady=5)

# 수평 레이아웃 1 - 버튼 4개 추가
horizontal_layout1 = tk.Frame(vertical_layout)
horizontal_layout1.grid(row=0, column=0, padx=10, pady=10)
buttonSelectDocxFile = tk.Button(horizontal_layout1, text="변환대상파일조회")
buttonConvertDocxToPdf = tk.Button(horizontal_layout1, text="파일변환")
buttonDisplayConvertedPdfFile = tk.Button(horizontal_layout1, text="변환파일조회")

buttonSendFile = tk.Button(horizontal_layout1, text="변환파일전송")
buttonDelFile = tk.Button(horizontal_layout1, text="변환대상파일삭제")
buttonDelConvertedFile = tk.Button(horizontal_layout1, text="변환파일(전송전)삭제")
buttonDelSendFile = tk.Button(horizontal_layout1, text="변환파일(전송후)삭제")

buttonSelectDocxFile.grid(row=0, column=0, padx=10, pady=10)
buttonConvertDocxToPdf.grid(row=0, column=1, padx=10, pady=10)
buttonDelFile.grid(row=0, column=2, padx=10, pady=10)
buttonDisplayConvertedPdfFile.grid(row=0, column=3, padx=10, pady=10)
buttonDelConvertedFile.grid(row=0, column=4, padx=10, pady=10)
buttonSendFile.grid(row=0, column=5, padx=10, pady=10)


buttonDelSendFile.grid(row=0, column=6, padx=10, pady=10)

# 수평 레이아웃 3 - 라벨 추가
horizontal_layout3 = tk.Frame(vertical_layout)
horizontal_layout3.grid(row=1, column=0, padx=0, pady=0)
label = tk.Label(horizontal_layout3, text="변환대상파일")
label.grid(row=0, column=0, padx=100, pady=0)
label = tk.Label(horizontal_layout3, text="변환파일(전송전)")
label.grid(row=0, column=1, padx=100, pady=0)
label = tk.Label(horizontal_layout3, text="변환파일(전송완료)")
label.grid(row=0, column=2, padx=100, pady=0)

# 수평 레이아웃 2 - 리스트 박스 2개 추가
horizontal_layout2 = tk.Frame(vertical_layout)

horizontal_layout2.grid(row=2, column=0, padx=10, pady=10)
listbox1 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
listbox2 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
listbox3 = tk.Listbox(horizontal_layout2, width=40, height=20, selectmode=tk.MULTIPLE)
listbox1.grid(row=0, column=0, padx=10, pady=5)
listbox2.grid(row=0, column=1, padx=10, pady=5)
listbox3.grid(row=0, column=2, padx=10, pady=5)

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
# 확장자에 따라 파일 목록 가져오는 함수
def get_files(folder, extension):
    return [file for file in os.listdir(folder) if file.endswith(extension)]

# 리스트 박스1에 docx파일 로드
def display_docx_files():
    global listbox1  # 리스트 박스를 전역 변수로 선언
    
    if os.path.exists(docx_folder):
        pdf_files = get_files(docx_folder, ".docx")
        
        listbox1.delete(0, tk.END)  # 리스트 박스 내용 초기화
        
        if pdf_files:
            for pdf_file in pdf_files:
                listbox1.insert(tk.END, pdf_file)
        else:
            listbox1.insert(tk.END, "해당 확장자의 파일을 찾을 수 없습니다.")
    else:
        listbox1.delete(0, tk.END)
        listbox1.insert(tk.END, "폴더를 찾을 수 없습니다.")
# 리스트 박스2에 pdf파일 로드 pdf_folder_sendout
def display_pdf_files():
    global listbox2  # 리스트 박스를 전역 변수로 선언
    
    if os.path.exists(pdf_folder_out):
        pdf_files = get_files(pdf_folder_out, ".pdf")
        
        listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화
        
        if pdf_files:
            for pdf_file in pdf_files:
                listbox2.insert(tk.END, pdf_file)
        else:
            print( "해당 확장자의 파일을 찾을 수 없습니다.")
    else:
        listbox2.delete(0, tk.END)
        listbox2.insert(tk.END, "폴더를 찾을 수 없습니다.")

def display_send_pdf_files():
    global listbox3  # 리스트 박스를 전역 변수로 선언
    
    if os.path.exists(pdf_folder_sendout):
        pdf_files = get_files(pdf_folder_sendout, ".pdf")
        
        listbox3.delete(0, tk.END)  # 리스트 박스 내용 초기화
        
        if pdf_files:
            for pdf_file in pdf_files:
                listbox3.insert(tk.END, pdf_file)
        else:
            print( "해당 확장자의 파일을 찾을 수 없습니다.")
    else:
        listbox3.delete(0, tk.END)
        listbox3.insert(tk.END, "폴더를 찾을 수 없습니다.")


display_docx_files()
display_pdf_files()
display_send_pdf_files()
# docx파일을 pdf파일로 변환
def convert_selected_items():
    selected_items = listbox1.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox1.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    lincense_chk=check_licence_date()
    
    if lincense_chk == 1:
        label.config(text="프로그램 사용 기한이 만료되었습니다")
        return
    
    file_postfix = get_file_postfix()
    label.config(text="")
    if selected_items:
        for idx in selected_items:
            selected_file = listbox1.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로
            docx_file_path = docx_folder + "\\" + selected_file
            file_name_without_extension = file_name_without_extension + '_' + file_postfix
            # PDF로 저장할 파일 경로
            pdf_file_out_path = pdf_temp_folder + "\\" + file_name_without_extension + ".pdf"
            #qr저장 경로
            qrPath = qr_folder + "\\" + file_name_without_extension + ".png"
            #변환 pdf 경로
            output_path_pdf = pdf_folder_out + "\\" + file_name_without_extension + ".pdf"
            #변환 pdf를 다시 docx로 저장시 경로
            docx_folder_out_path = docx_folder_out + "\\" + file_name_without_extension + ".docx"
            # 파일이 존재하는지 확인 후 삭제
            db_key = file_name_without_extension + ".pdf"
            #docx파일을 pdf로 변환
            convert_docx_to_pdf(docx_file_path, pdf_file_out_path)
            #qr생성
            qrMake(qrPath, db_key)
            insert_qr_code_into_pdf(pdf_file_out_path, qrPath, output_path_pdf)
            
            

            sign(jar, output_path_pdf,output_path_pdf, crt, pem)
            convert_pdf_to_docx(output_path_pdf, docx_folder_out_path)
            os.remove(pdf_file_out_path) #임시파일삭제
        label.config(text="변환이 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력

#docx파일을 pdf로 변환
def convert_docx_to_pdf(input_path, output_path):
    convert(input_path, output_path)
    
    
def convert_docx_to_pdf_com(input_path, output_path):
    # COM 서버 생성
    word = win32.gencache.EnsureDispatch('Word.Application')

    # 워드 애플리케이션을 보이지 않도록 설정
    word.Visible = 0

    # 원본 DOCX 파일 열기
    doc = word.Documents.Open(input_path)

    # PDF로 저장
    doc.SaveAs(output_path, FileFormat=17)  # 17은 PDF 형식을 나타냅니다.

    # 작업 완료 후 Word 닫기
    doc.Close()
    word.Quit()

#pdf를 dox로 변환    
def convert_pdf_to_docx(input_path, output_path):
    # convert pdf to docx
    cv = Converter(input_path)
    cv.convert(output_path)      # all pages by default
    cv.close()
#qr이미지 생성
def qrMake(qrpath, db_key):
    # QR 코드 데이터
    qr_url = 'http://hjw8393.cafe24app.com/share/'
    #https://hjw7603.s3.ap-northeast-2.amazonaws.com/share/'
    qr_data = qr_url + db_key  # QR 코드에 포함될 데이터 nodejs 파일 경로

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # 로고 이미지 열기
    logo_path = "logo.png"  # 로고 이미지 파일 경로
    logo_img = Image.open(logo_path)

    # 로고 이미지 크기 조정
    logo_width, logo_height = logo_img.size
    qr_width, qr_height = qr_img.size
    logo_size = (qr_width // 8, qr_height // 8)  # 로고 크기 조절

    # 로고 이미지를 컬러로 합성
    #qr_img.paste(logo_img.resize(logo_size, Image.ANTIALIAS), ((qr_width - logo_size[0]) // 2, (qr_height - logo_size[1]) // 2))
    qr_img = qr_img.convert("RGBA")

    # 로고 이미지를 QR 코드 중앙에 합성
    position = ((qr_width - logo_size[0]) // 2, (qr_height - logo_size[1]) // 2)
    qr_img.paste(logo_img.resize(logo_size, Image.LANCZOS), position)

    # 최종 QR 코드 이미지 저장
    #qrpath = afworkdir + "\\" + qrFileNm
    qr_img.save(qrpath)

#pdf파일에 qr이미지 넣기
def insert_qr_code_into_pdf(input_pdf_path, input_path_qr, output_pdf_path):
    # PDF 파일 열기
    doc = fitz.open(input_pdf_path)
    #doc = fitz
    # 이미지 삽입할 위치 지정
    rect = fitz.Rect(480, 70, 520, 110)

    # 이미지 삽입
    page = doc[0]
    page.insert_image(rect, filename=input_path_qr)

    # PDF 파일 저장
    doc.save(output_pdf_path)

# aws로 파일 전송
def send_selected_items():
    selected_items = listbox2.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox2.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    label.config(text="")
    if selected_items:
        for idx in selected_items:
            selected_file = listbox2.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            output_path_pdf = pdf_folder_out + "\\" + file_name_without_extension + ".pdf"
            sendoutput_path_pdf = pdf_folder_sendout + "\\" + file_name_without_extension + ".pdf"
            # 파일이 존재하는지 확인 후 삭제
            db_key = file_name_without_extension + ".pdf"
            object_key = 'share/'+ db_key
            local_file_path = output_path_pdf
            bucket_name ='hjw7603'
            share_doc_url = 'https://hjw7603.s3.ap-northeast-2.amazonaws.com/share/' + db_key
            upload_file_aws(bucket_name, object_key, local_file_path)
            
            upsert_db(db_key, share_doc_url)
            shutil.move(output_path_pdf, sendoutput_path_pdf)
    
        label.config(text="파일전송이 성공했습니다.")
        display_send_pdf_files()
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력

# 변환대상 파일 삭제
def delete_selected_items_list1():
    selected_items = listbox1.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox1.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    #listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화

    label.config(text="")
    if selected_items:
        for idx in selected_items:
            selected_file = listbox1.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            del_path = docx_folder  + "\\" + file_name_without_extension + ".docx"
            try:
                os.remove(del_path)
                #os.remove(pdf_file_path)
                print(f'{del_path} 파일이 삭제되었습니다.')
            except OSError as e:
                print(f'파일 삭제 오류: {e}')


        label.config(text="파일삭제가 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력

# 변환 파일 삭제
def delete_selected_items_list2():
    selected_items = listbox2.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox2.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    #listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화

    label.config(text="")
    if selected_items:
        for idx in selected_items:
            selected_file = listbox2.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            output_path_pdf = pdf_folder_out + "\\" + file_name_without_extension + ".pdf"
            pdf_file_path = pdf_temp_folder + "\\" + file_name_without_extension + ".pdf"
            docx_folder_out_path = docx_folder_out + "\\" + file_name_without_extension + ".docx"
            try:
                os.remove(output_path_pdf)
                #os.remove(pdf_file_path)
                os.remove(docx_folder_out_path)
                print(f'{output_path_pdf} 파일이 삭제되었습니다.')
            except OSError as e:
                print(f'파일 삭제 오류: {e}')
            # 파일이 존재하는지 확인 후 삭제
            db_key = file_name_without_extension + ".pdf"
            #delete_db(db_key)
        
    
        label.config(text="파일삭제가 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력
        
# 변환 파일 삭제
def delete_selected_items_list3():
    selected_items = listbox2.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox2.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    #listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화

    label.config(text="")
    if selected_items:
        for idx in selected_items:
            selected_file = listbox2.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            output_path_pdf = pdf_folder_out + "\\" + file_name_without_extension + ".pdf"
            output_path_sendpdf = pdf_folder_sendout + "\\" + file_name_without_extension + ".pdf" 
            pdf_file_path = pdf_temp_folder + "\\" + file_name_without_extension + ".pdf"
            docx_folder_out_path = docx_folder_out + "\\" + file_name_without_extension + ".docx"
            try:
                os.remove(output_path_pdf)
                os.remove(output_path_sendpdf)
                #os.remove(pdf_file_path)
                os.remove(docx_folder_out_path)
                print(f'{output_path_pdf} 파일이 삭제되었습니다.')
            except OSError as e:
                print(f'파일 삭제 오류: {e}')
            # 파일이 존재하는지 확인 후 삭제
            db_key = file_name_without_extension + ".pdf"
            #share_doc_url = upload_file_to(output_path_pdf, db_key)
            object_key = 'share/'+ db_key
            bucket_name ='hjw7603'
            delete_file_aws(bucket_name, object_key)
            delete_db(db_key)
        
    
        label.config(text="파일삭제가 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력
        
# 버튼에 동작 연결
buttonSelectDocxFile.config(command=display_docx_files)
buttonConvertDocxToPdf.config(command=convert_selected_items)
buttonDisplayConvertedPdfFile.config(command=display_pdf_files)

buttonSendFile.config(command=send_selected_items)
buttonDelFile.config(command=delete_selected_items_list1)
buttonDelConvertedFile.config(command=delete_selected_items_list2)
buttonDelSendFile.config(command=delete_selected_items_list3)

# GUI 실행
window.mainloop()
