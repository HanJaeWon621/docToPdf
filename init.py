import os

# PDF 폴더 경로
wokr_root_folder = "C:\\pdf"
pdf_folder = wokr_root_folder +"\\temppdf"  # PDF 폴더 경로를 적절히 수정하세요.
pdf_folder_out =  wokr_root_folder +"\\outpdf"  # PDF 폴더 경로를 적절히 수정하세요.
docx_folder =  wokr_root_folder +"\\workdocx"  # 작업 폴더.
qr_folder =  wokr_root_folder +"\\qrimg" #qrimg폴더
docx_folder_out =   wokr_root_folder +"\\outdocx"

def init_make_dir():
    if not os.path.exists(wokr_root_folder):
        os.makedirs(wokr_root_folder)
        print(f'Directory "{wokr_root_folder}" created successfully.')
        if not os.path.exists(wokr_root_folder):
            os.makedirs(wokr_root_folder)
            print(f'Directory "{wokr_root_folder}" created successfully.')
        else:
            print(f'Directory "{wokr_root_folder}" already exists.')
            
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)
            print(f'Directory "{pdf_folder}" created successfully.')
        else:
            print(f'Directory "{pdf_folder}" already exists.')
            
        if not os.path.exists(pdf_folder_out):
            os.makedirs(pdf_folder_out)
            print(f'Directory "{pdf_folder_out}" created successfully.')
        else:
            print(f'Directory "{pdf_folder_out}" already exists.')
        
        if not os.path.exists(docx_folder):
            os.makedirs(docx_folder)
            print(f'Directory "{docx_folder}" created successfully.')
        else:
            print(f'Directory "{docx_folder}" already exists.')
        
        if not os.path.exists(qr_folder):
            os.makedirs(qr_folder)
            print(f'Directory "{qr_folder}" created successfully.')
        else:
            print(f'Directory "{qr_folder}" already exists.')
            
        if not os.path.exists(docx_folder_out):
            os.makedirs(docx_folder_out)
            print(f'Directory "{docx_folder_out}" created successfully.')
        else:
            print(f'Directory "{docx_folder_out}" already exists.')
    else:
        print(f'Directory "{wokr_root_folder}" already exists.')
        
        if not os.path.exists(wokr_root_folder):
            os.makedirs(wokr_root_folder)
            print(f'Directory "{wokr_root_folder}" created successfully.')
        else:
            print(f'Directory "{wokr_root_folder}" already exists.')
            
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)
            print(f'Directory "{pdf_folder}" created successfully.')
        else:
            print(f'Directory "{pdf_folder}" already exists.')
            
        if not os.path.exists(pdf_folder_out):
            os.makedirs(pdf_folder_out)
            print(f'Directory "{pdf_folder_out}" created successfully.')
        else:
            print(f'Directory "{pdf_folder_out}" already exists.')
        
        if not os.path.exists(docx_folder):
            os.makedirs(docx_folder)
            print(f'Directory "{docx_folder}" created successfully.')
        else:
            print(f'Directory "{docx_folder}" already exists.')
        
        if not os.path.exists(qr_folder):
            os.makedirs(qr_folder)
            print(f'Directory "{qr_folder}" created successfully.')
        else:
            print(f'Directory "{qr_folder}" already exists.')
            
        if not os.path.exists(docx_folder_out):
            os.makedirs(docx_folder_out)
            print(f'Directory "{docx_folder_out}" created successfully.')
        else:
            print(f'Directory "{docx_folder_out}" already exists.')
# 버튼에 동작 연결
if __name__ == "__main__":
    print('작업디렉토리 생성')
    init_make_dir()
