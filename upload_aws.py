import boto3
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

aws_access_key_id = ''
aws_secret_access_key = ''
def upload_s3_object(bucket_name, object_key, local_file_path, flag):
    # AWS S3 자격 증명 설정
    
    # S3 클라이언트 생성
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    
    try:
        if flag =='D':
            # S3 객체 삭제
            s3.delete_object(Bucket=bucket_name, Key=object_key)
            print(f"{object_key} 파일이 {bucket_name} 버킷에서 삭제되었습니다.")
            
        # 파일 업로드
        s3.upload_file(local_file_path, bucket_name, object_key)
        print(f'{local_file_path} 파일이 {bucket_name} 버킷에 성공적으로 업로드되었습니다.')
    except FileNotFoundError:
        print(f'{local_file_path} 파일을 찾을 수 없습니다1.')
    except NoCredentialsError:
        print('AWS 자격 증명이 설정되지 않았습니다.')
    except Exception as e:
        print(f'파일 업로드 중 오류 발생: {str(e)}')
    
def check_s3_object_exists(bucket_name, object_key):
    # AWS S3 자격 증명 설정
    #bucket_name = 'hjw7603'
    
    # S3 클라이언트 생성
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    try:
        # AWS 리전 및 인증 설정
        #s3 = boto3.client('s3')
        
        #bucket_name = 'hjw7603'
        # S3 버킷에서 객체 가져오기 시도
        s3.head_object(Bucket=bucket_name, Key=object_key)

        # 객체가 존재하면 True 반환
        return True
    except NoCredentialsError:
        print("AWS 자격 증명이 없습니다.")
        return False
    except PartialCredentialsError:
        print("AWS 자격 증명이 부분적으로 제공되었습니다.")
        return False
    except Exception as e:
        # 객체가 존재하지 않거나 다른 오류가 발생한 경우 False 반환
        if "404" in str(e):
            return False
        else:
            print(f"오류 발생: {e}")
            return False
def upload_file_aws(bucket_name, object_key, local_file_path):
    # 체크할 S3 버킷 및 객체 키 설정
    if check_s3_object_exists(bucket_name, object_key):
        
        print(f"{object_key} 파일이 {bucket_name} 버킷에 존재합니다.")
        upload_s3_object(bucket_name, object_key, local_file_path,'D')
    else:
        print(f"{object_key} 파일이 {bucket_name} 버킷에 존재하지 않습니다.")
        upload_s3_object(bucket_name, object_key, local_file_path,'')
def delete_s3_object(bucket_name, object_key):
    # AWS S3 자격 증명 설정
   # bucket_name = 'hjw7603'
    
    # S3 클라이언트 생성
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"{object_key} 파일이 {bucket_name} 버킷에서 삭제되었습니다.")
            

    #except FileNotFoundError:
        #ㄴprint(f'{object_key} 파일을 찾을 수 없습니다.')
    except NoCredentialsError:
        print('AWS 자격 증명이 설정되지 않았습니다.')
    except Exception as e:
        print(f'파일 삭제중 오류 발생: {str(e)}')        
def delete_file_aws(bucket_name, object_key):
    # S3 객체의 존재 여부 확인
    #if check_s3_object_exists(bucket_name, object_key):
    delete_s3_object(bucket_name, object_key)
    
if __name__ == "__main__":
    # 체크할 S3 버킷 및 객체 키 설정
    print("main")
