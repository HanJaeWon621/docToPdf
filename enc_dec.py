from cryptography.fernet import Fernet

# 키 생성 및 저장
def make_key():
    key = Fernet.generate_key()
    with open("c:/pdf/license/license.key", "wb") as key_file:
        key_file.write(key)

# 암호화된 키 데이터를 파일에 저장
def make_enc(data_to_encrypt):
    # 암호화할 문자열
       
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()

    
    # Fernet 객체 생성
    fernet = Fernet(key)

    # 문자열을 바이트로 변환하여 암호화
    encrypted_data = fernet.encrypt(data_to_encrypt.encode())

    with open("c:/pdf/license/license.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# 암호화된 액세스 키 데이터를 파일에 저장
def make_enc_awsacckey(data_to_encrypt):
    # 암호화할 문자열
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()
    # Fernet 객체 생성
    fernet = Fernet(key)

    # 문자열을 바이트로 변환하여 암호화
    encrypted_data = fernet.encrypt(data_to_encrypt.encode())

    with open("c:/pdf/license/license_awsacckey.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# 암호화된 시크릿키 데이터를 파일에 저장
def make_enc_awssecacckey(data_to_encrypt):
    # 암호화할 문자열
    
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()

    # Fernet 객체 생성
    fernet = Fernet(key)

    # 문자열을 바이트로 변환하여 암호화
    encrypted_data = fernet.encrypt(data_to_encrypt.encode())

    with open("c:/pdf/license/license_awssecacckey.dat", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
        
    return encrypted_data

# 키 복호화
def get_dec():
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()
    
    # Fernet 객체 생성
    fernet = Fernet(key)
    with open("c:/pdf/license/license.dat", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    dec_str = decrypted_data.decode()
    return dec_str
# 액세스키 복호화
def get_dec_awsacckey():
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()
    # Fernet 객체 생성
    fernet = Fernet(key)
    
    with open("c:/pdf/license/license_awsacckey.dat", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    dec_str = decrypted_data.decode()
    return dec_str
# 시크릿키 복호화
def get_dec_awssecacckey():
    # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()
    
    # Fernet 객체 생성
    fernet = Fernet(key)
    with open("c:/pdf/license/license_awssecacckey.dat", "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    dec_str = decrypted_data.decode()
    return dec_str

def get_dec_data_fromdb(key, encrypted_data):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    dec_str = decrypted_data.decode()
    return dec_str

if __name__ == "__main__":
    div='4'
    if div == '1':
        make_enc('99991231')
        dec_str = get_dec()
    elif div == '2':
        data_to_encrypt = '1'
        encrypted_data = make_enc_awsacckey(data_to_encrypt)
        #key, encrypted_data
         # 키 파일에서 키를 읽어옴
        key = get_dec()
        print("복호화된 문자열key:", key)
        dec_str = get_dec_awsacckey()
            
        print("복호화된 문자열:", dec_str)
    elif div == '3':
        data_to_encrypt = '1'
        make_enc_awssecacckey(data_to_encrypt)
        dec_str = get_dec_awssecacckey()
        print("복호화된 문자열:", dec_str)
    elif div == '4':
        dec_str = get_dec_data_fromdb('1', '1')
        print("복호화된 문자열:", dec_str)
    #make_enc(data_to_encrypt)
    
    