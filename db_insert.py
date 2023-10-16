import mysql.connector

def upsert_db(file_id, share_doc_url):
    # MySQL 연결 설정
    config = {
        'host': 'database-1.c2tc0okknqs6.us-east-1.rds.amazonaws.com',        # MySQL 호스트 주소
        'user': 'admin',    # MySQL 사용자 이름
        'password': 'pwd061218*',# MySQL 비밀번호
        'database': 'share_db' # 사용할 데이터베이스 이름
    }
    
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
    config = {
        'host': 'database-1.c2tc0okknqs6.us-east-1.rds.amazonaws.com',        # MySQL 호스트 주소
        'user': 'admin',    # MySQL 사용자 이름
        'password': 'pwd061218*',# MySQL 비밀번호
        'database': 'share_db' # 사용할 데이터베이스 이름
    }
    
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
if __name__ == "__main__":
    delete_db('testdocx_2023103141147.pdf')