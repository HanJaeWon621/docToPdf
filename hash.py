import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        # 파일이 큰 경우 조금씩 읽어서 업데이트
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

#file_path = "test2.pdf"
#hash_value = calculate_sha256(file_path)
#print("SHA-256 Hash:", hash_value)
