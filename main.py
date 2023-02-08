from fastapi import File, UploadFile, FastAPI
from app import convertion_csv
import boto3
from mangum import Mangum
import json
from uuid import uuid4

app = FastAPI()

aws_bucket= 'Random-name' #insert your bucket name
file_location= 's3://Random-name.s3.eu-west-2.amazonaws.com/' #obtained from s3
#access key and secret key is require to push in the s3
s3 = boto3.client('s3', aws_access_key_id='###########', aws_secret_access_key='######################')

@app.post("/file")
def convertion(file: UploadFile):
    #to create unique file name every time
    key_1= uuid4()
    key_2= uuid4()
    df= json.load(file.file)
    convert= convertion_csv(df)
    first, second = convert.json_to_csv_que()
    first.to_csv(str(key_1)+'.csv')
    second.to_csv(str(key_2)+'.csv')
    response= s3.upload_file(str(key_1)+'.csv', aws_bucket, str(key_1)+'.csv')
    response1= s3.upload_file(str(key_2)+'.csv', aws_bucket, str(key_2)+'.csv')
    file1_path= file_location + str(key_1)+'.csv'
    file2_path= file_location + str(key_2)+'.csv'
    return {'file 1':file1_path, 'file 2': file2_path}

#handler is for lambda
handler= Mangum(app)

