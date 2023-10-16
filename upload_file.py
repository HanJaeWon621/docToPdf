import dropbox


def upload_file_to(local_file_path_param, dropbox_file_param):
    # Dropbox 액세스 토큰
    ACCESS_TOKEN = 'sl.BnDBDQDGt3d2YuMLH9l9x7EqHa-L6hU378bep19QJnPXUpYinfZaP_GsAQ3e8AndOejv2QFCUShfS5jJGO5SiwGXhcl-PYQ2El4oRznEVFHBlR5BqZ7B8Lc9NDs4HG8XZDwieGbPnp-4ARx2xZTQCKo'
    
    
    # Dropbox 애플리케이션 정보
    app_key = 'omv3j9h9mk3jhq9'
    app_secret = 'lcee8pv9phk5gzr'
    
    # Dropbox OAuth 2.0 인증 흐름 생성
    flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    
    # 사용자의 Dropbox 계정과 연결
    authorize_url = flow.start()
    print(f"1. Go to: {authorize_url}")
    print("2. Click 'Allow' (you might have to log in first)")
    print("3. Copy the authorization code.")
    print("authorize_url>>", authorize_url)
    # 사용자가 별도의 스텝에서 "authorization code"를 얻어서 여기에 붙여넣습니다.
    authorization_code = input("uyBej714-XAAAAAAAAAAHpOyjX3ah_lpG8ZH7H53F00")
    
    # 액세스 토큰과 리프레시 토큰 얻기
    access_token, refresh_token = flow.finish(authorization_code)
    
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    
    # Dropbox 클라이언트 초기화
    dbx = dropbox.Dropbox(access_token)
    
    # 업로드할 파일 경로 및 이름
    #local_file_path = 'C:\\pdf\\afwork\\test2.pdf'
    #dropbox_file_path = '/sharepdf/test2.pdf'  # Dropbox 내에서의 파일 경로
    local_file_path = local_file_path_param
    dropbox_file_path = '/sharepdf/' + dropbox_file_param
    db_key = dropbox_file_param
    # 파일 업로드
    with open(local_file_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite)
    
    # 업로드된 파일의 공유 링크 생성
    shared_link = dbx.sharing_create_shared_link(dropbox_file_path)
    
    # 공유 링크 URL
    shared_link_url = shared_link.url
    # db_key로 공유 링크 URL UPDATE
    # 공유 링크를 데이터베이스에 저장하는 코드를 추가하세요.
    # 예를 들어, 여기에서는 SQLite를 사용합니다.
    '''
    import sqlite3
    
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO shared_links (file_name, link_url) VALUES (?, ?)', ('file.txt', shared_link_url))
    
    conn.commit()
    conn.close()
    '''
    print(f'File uploaded and shared link created: {shared_link_url}')
    
if __name__ == "__main__":
    upload_file_to('2','2')