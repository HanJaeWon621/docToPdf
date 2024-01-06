import tkinter as tk
import os
import win32com.client as win32
from pdf2docx import Converter
from docx2pdf import convert
from docx import Document
from concurrent.futures import ThreadPoolExecutor
import fitz
import PyPDF2
import qrcode
import shutil
from PIL import Image
#from upload_file import *
from db_insert import *
from upload_aws import *
from enc_dec import *
from e_sign import *
from license import *
from gui_init import *
from appinfo import *
from hash import *
# tkinter 윈도우 생성
bucket_name = awsbucket #'sharehjw'
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
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
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
            #convert_pdf_to_docx_parrel(output_path_pdf, docx_folder_out_path)
            os.remove(pdf_file_out_path) #임시파일삭제
        label.config(text="변환이 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력

#docx파일을 pdf로 변환
def convert_docx_to_pdf(input_path, output_path):
    print(input_path, output_path)
    convert(input_path, output_path)
    
    
def convert_docx_to_pdf_com(input_path, output_path):
    # COM 서버 생성
    word = win32.gencache.EnsureDispatch('Word.Application')

    # 워드 애플리케이션을 보이지 않도록 설정
    word.Visible = 0
    print(input_path)
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

def pdf_to_text(pdf_file, start_page, end_page):
    text = ""
    pdf = PyPDF2.PdfFileReader(pdf_file)
    for page in range(start_page, end_page):
        text += pdf.getPage(page).extractText()
    return text

def text_to_docx(text, docx_document):
    docx_document.add_paragraph(text)
    
def convert_pdf_to_docx_parrel(input_path, output_path):
    pdf_file = input_path  # PDF 파일명
    docx_file = output_path  # DOCX 파일명
    num_threads = 4  # 사용할 스레드 수

    num_threads = 4  # 사용할 스레드 수

    with open(pdf_file, 'rb') as pdf:
        num_pages = PyPDF2.PdfFileReader(pdf).getNumPages()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        docx_document = Document()  # Document 객체를 직접 만듭니다.

        futures = []

        for i in range(num_threads):
            start_page = i * num_pages // num_threads
            end_page = (i + 1) * num_pages // num_threads

            future = executor.submit(pdf_to_text, pdf_file, start_page, end_page)
            futures.append(future)

        for future in futures:
            text = future.result()
            text_to_docx(text, docx_document)

        docx_document.save(docx_file)

    print(f"PDF 파일을 DOCX 파일로 변환 완료: {docx_file}")
#qr이미지 생성
def qrMake(qrpath, db_key):
    # QR 코드 데이터
    qr_url = cafe24url
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
    logo_path = "c:\\pdf\\logo.png"  # 로고 이미지 파일 경로
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
        #label.config(text="전송을 시작했습니다.")
        for idx in selected_items:
            selected_file = listbox2.get(idx)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            # PDF로 저장할 파일 경로
            output_path_pdf = pdf_folder_out + "\\" + file_name_without_extension + ".pdf"
            sendoutput_path_pdf = pdf_folder_sendout + "\\" + file_name_without_extension + ".pdf"
            # 파일이 존재하는지 확인 후 삭제
            db_key = file_name_without_extension + ".pdf"
            object_key = 'share/'+ db_key
            local_file_path = output_path_pdf
            
            #share_doc_url = 'https://'+bucket_name+'.s3.ap-northeast-2.amazonaws.com/share/' + db_key
            share_doc_url = 'https://'+bucket_name+'.s3.ap-northeast-2.amazonaws.com/' + object_key
            upload_file_aws(bucket_name, object_key, local_file_path)
            hash_value = calculate_sha256(local_file_path)
            upsert_db(db_key, share_doc_url, hash_value)
            shutil.move(output_path_pdf, sendoutput_path_pdf)
    
        #label.config(text="파일전송이 성공했습니다.")
        show_alert("파일전송이 성공했습니다.")
        display_send_pdf_files()
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        #label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력
        show_alert("전송할 파일을 선택하세요.")

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


        show_alert("파일삭제가 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        show_alert("삭제할 파일을 선택하세요.")  # 라벨에 텍스트 입력

    display_docx_files()
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
            #pdf_file_path = pdf_temp_folder + "\\" + file_name_without_extension + ".pdf"
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
        
    
        show_alert("파일삭제가 성공했습니다.")
        display_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        show_alert("삭제할 파일을 선택하세요.")  # 라벨에 텍스트 입력
        
# 전송완료 파일 삭제
def delete_selected_items_list3():
    selected_items = listbox3.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox3.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    #listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화

    label.config(text="")
    if selected_items:
        #label.config(text="삭제처리 중입니다.")
        for idx in selected_items:
            selected_file = listbox3.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리
            print(file_name_without_extension)
            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            output_path_sendpdf = pdf_folder_sendout + "\\" + file_name_without_extension + ".pdf" 
            docx_folder_out_path = docx_folder_out + "\\" + file_name_without_extension + ".docx"
            try:
                os.remove(output_path_sendpdf)
                #os.remove(docx_folder_out_path)
                #print(f'{output_path_sendpdf} 파일이 삭제되었습니다.')
                # 파일이 존재하는지 확인 후 삭제
                db_key = file_name_without_extension + ".pdf"
                #share_doc_url = upload_file_to(output_path_pdf, db_key)
                object_key = 'share/'+ db_key
                #bucket_name ='hjw7603'
                delete_file_aws(bucket_name, object_key)
                delete_db(db_key)
            except OSError as e:
                print(f'파일 삭제 오류: {e}')
            
        #label.config(text="파일삭제가 성공했습니다.")
        show_alert("파일삭제가 성공했습니다.")
        display_send_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        #label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력
        show_alert("삭제할 파일을 선택하세요.")

# 전송완료 파일 삭제
def backupSendFile():
    selected_items = listbox3.curselection()  # 선택한 항목의 인덱스 가져오기
    selected_files = [listbox3.get(idx) for idx in selected_items]  # 선택한 항목 가져오기
    
    #listbox2.delete(0, tk.END)  # 리스트 박스 내용 초기화
    if not os.path.exists(pdf_folder_sendout_backup):
        os.makedirs(pdf_folder_sendout_backup)
    label.config(text="")
    if selected_items:
        #label.config(text="삭제처리 중입니다.")
        for idx in selected_items:
            selected_file = listbox3.get(idx)
            print(selected_file)
            file_name_without_extension, _ = os.path.splitext(selected_file)  # 파일명과 확장자 분리

            # 원본 DOCX 파일 경로

            # PDF로 저장할 파일 경로
            output_path_sendpdf = pdf_folder_sendout + "\\" + file_name_without_extension + ".pdf" 
            output_path_sendpdf_backup = pdf_folder_sendout_backup + "\\" + file_name_without_extension + ".pdf"
            try:
                shutil.move(output_path_sendpdf, output_path_sendpdf_backup)
            except OSError as e:
                print(f'파일 백업 오류: {e}')
            
        show_alert("파일 백업이 성공했습니다.")
        display_send_pdf_files()
    else:
        #listbox2.insert(tk.END, "선택한 항목이 없습니다.")
        #label.config(text="선택한 파일 목록이 없습니다.")  # 라벨에 텍스트 입력
        show_alert("백업할 파일을 선택하세요.")     
# 버튼에 동작 연결
btnSelectDocxFile.config(command=display_docx_files)
btnConvertDocxToPdf.config(command=convert_selected_items)
btnDisplayConvertedPdfFile.config(command=display_pdf_files)
btnDisplaySendPdfFile.config(command=display_send_pdf_files)

btnSendFile.config(command=send_selected_items)
btnDelFile.config(command=delete_selected_items_list1)
btnDelConvertedFile.config(command=delete_selected_items_list2)
btnDelSendFile.config(command=delete_selected_items_list3)

btnAllSelFile.config(command=select_all_items1)
btnAllSelConvertedFile.config(command=select_all_items2)
btnAllSelSendFile.config(command=select_all_items3)
btnAllBackupSendFile.config(command=backupSendFile)

# GUI 실행
window.mainloop()

