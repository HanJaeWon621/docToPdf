import subprocess

# Windows 명령을 실행하려면 subprocess.run() 함수를 사용합니다.
# 예를 들어, "dir" 명령을 실행해보겠습니다.
'''
기능 문서 전자서명 처리
수행 프로그램  jar="c:\\sign\\open-pdf-sign.jar"
변환 대상 파일 input_doc="c:\\sign\\test.pdf"
변환 파일      output_doc="c:\\sign\\test3.pdf"
인증서 파일    crt="c:\\sign\\cert.cer"
개인키         pem="c:\\sign\\private_key.pem"
자바 설치 필요
'''
def sign(jar, input_doc,output_doc, crt, pem):
    cmd="java -jar "+ jar +" --input "+ input_doc + " --output "+output_doc+" --certificate "+ crt +" --key " + pem

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # 결과 출력
    print("표준 출력:")
    print(result.stdout)

    print("에러 출력:")
    print(result.stderr)

    # 반환 코드 확인 (0은 성공을 나타냅니다)
    print("반환 코드:", result.returncode)

if __name__ == "__main__":
    jar="c:\\sign\\open-pdf-sign.jar"
    input_doc="c:\\sign\\test.pdf"
    output_doc="c:\\sign\\test3.pdf"
    crt="c:\\sign\\cert.cer"
    pem="c:\\sign\\private_key.pem"