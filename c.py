from cx_Freeze import setup, Executable

# 실행 파일의 정보 설정
executables = [
    Executable("pdf_converter.py")  # 스크립트 파일명을 여기에 넣어주세요.
]

# 빌드 설정
build_options = {
    "packages": [],  # 필요한 패키지 추가
    "excludes": [],  # 제외할 패키지 설정
}

# 빌드 설정과 실행 파일 설정을 결합
setup(
    name="pdf_converter",  # 프로그램 이름
    version="1.0",
    description="My Script Description",
    options={"build_exe": build_options},
    executables=executables
)
