from cryptography.fernet import Fernet

# 키 생성 및 저장
def make_key():
    key = Fernet.generate_key()
    with open("c:/pdf/license/license.key", "wb") as key_file:
        key_file.write(key)

# 암호화된 데이터를 파일에 저장
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

# 암호화된 데이터를 파일에 저장
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

# 암호화된 데이터를 파일에 저장
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

# 복호화
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
# 복호화
def get_dec_awsacckey(key, encrypted_data):

    # Fernet 객체 생성
    fernet = Fernet(key)
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    dec_str = decrypted_data.decode()
    return dec_str 
# 복호화
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
if __name__ == "__main__":
    div='3'
    if div == '1':
        make_enc('1')
        dec_str = get_dec()
    elif div == '2':
        data_to_encrypt = '1'
        make_enc_awsacckey(data_to_encrypt)
        dec_str = get_dec_awsacckey()
    elif div == '3':
        data_to_encrypt = '1'
        make_enc_awssecacckey(data_to_encrypt)
        dec_str = get_dec_awssecacckey()
    #make_enc(data_to_encrypt)
    
    print("복호화된 문자열:", dec_str)