import mysql.connector
from enc_dec import *
from dbinfo import *
# MySQL 연결 설정
'''
global host    # MySQL 호스트 주소
global user    # MySQL 사용자 이름
global password  # MySQL 비밀번호
global database   # 사용할 데이터베이스 이름'''
config = {
    'host':host,       # MySQL 호스트 주소
    'user':user,   # MySQL 사용자 이름
    'password':password,   # MySQL 비밀번호
    'database':database   # 사용할 데이터베이스 이름
}

def upsert_db(file_id, share_doc_url):
    
    
    # MySQL 연결
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # 조회할 데이터
    file_id_to_search = file_id  # 조회할 파일 ID에 맞게 수정
    
    # 데이터 조회 쿼리
    select_query = "SELECT * FROM share_doc WHERE file_id = %s"
    
    # 데이터 삽입 쿼리
    insert_query = "INSERT INTO share_doc (file_id, share_doc_url) VALUES (%s, %s)"
    
    # 데이터 업데이트 쿼리
    update_query = "UPDATE share_doc SET share_doc_url = %s, uptdate=now()  WHERE file_id = %s"
    
    # 데이터베이스에서 데이터 조회
    cursor.execute(select_query, (file_id_to_search,))
    existing_data = cursor.fetchone()
    
    if existing_data:
        # 데이터가 존재하는 경우 업데이트
        new_share_data = share_doc_url  # 업데이트할 데이터에 맞게 수정
        cursor.execute(update_query, (new_share_data, file_id_to_search))
        conn.commit()
        print(f"데이터가 업데이트되었습니다. (file_id: {file_id_to_search})")
    else:
        # 데이터가 존재하지 않는 경우 삽입
        share_data_to_insert = share_doc_url  # 삽입할 데이터에 맞게 수정
        cursor.execute(insert_query, (file_id_to_search, share_data_to_insert))
        conn.commit()
        print(f"데이터가 삽입되었습니다. (file_id: {file_id_to_search})")
    
    # 연결 종료
    cursor.close()
    conn.close()

def delete_db(file_id):
    # MySQL 연결 설정
    
    # MySQL 연결
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    # 조회할 데이터
    file_id_to_search = file_id  # 조회할 파일 ID에 맞게 수정
    
    # 데이터 조회 쿼리
    #select_query = "SELECT * FROM share_doc WHERE file_id = %s"
        
    # 데이터 업데이트 쿼리
    delete_query = "DELETE FROM share_doc WHERE file_id = %s"
    
    # 데이터베이스에서 데이터 조회
    #cursor.execute(select_query, (file_id_to_search,))
    #existing_data = cursor.fetchone()
    
    #if existing_data:
        # 데이터가 존재하는 경우 업데이트
    cursor.execute(delete_query, (file_id_to_search,))
    conn.commit()
    #print(f"데이터가 삭제되었습니다. (file_id: {file_id_to_search})")
    
    # 연결 종료
    cursor.close()
    conn.close()
a=''
b=''

def get_aws():
    global a 
    global b
    # MySQL 연결
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
     # 키 파일에서 키를 읽어옴
    with open("c:/pdf/license/license.key", "rb") as key_file:
        key = key_file.read()
    # 조회할 데이터
    file_id_to_search = key  # 조회할 파일 ID에 맞게 수정
    
    # 데이터 조회 쿼리
    select_query = "SELECT * FROM awsk_mgmt WHERE enc_key = %s"
        
    # 데이터베이스에서 데이터 조회
    cursor.execute(select_query, (file_id_to_search,))
    existing_data = cursor.fetchone()
    #print(existing_data[1])
    #print(existing_data[2])

    a = get_dec_data_fromdb(key, existing_data[1])
    b = get_dec_data_fromdb(key, existing_data[2])
    empty_tuple = (a,b)
    #print(a, b)
    #print(existing_data.type)
    
    # 연결 종료
    cursor.close()
    conn.close()
    return empty_tuple

if __name__ == "__main__":
    empty_tuple = get_aws()
    print(empty_tuple[0])
    print(empty_tuple[1])