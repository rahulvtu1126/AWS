### 1. function to list buckets
import boto3
class s3_object():
    def list_aws_buckets(self):
        response=boto3.client('s3')
        s3_list=[]
        try:
            name=response.list_buckets()
            for i in name['Buckets']:
                s3_list.append(i['Name'])
            if len(s3_list)==0:
                return "There is no bucket in s3"
            else:
                return "Bucket list in s3 bucket are : ", s3_list
        except Exception as e:
            print(f'error is :  {e}')
        
    def create_s3_bucket(self,bucketName):
        response=boto3.client('s3')

        try:
            create_s3=response.create_bucket(Bucket=bucketName)
        except Exception as e:
            a=f'Please check this Error - {e}'
        
        if create_s3 is True:
            return (bucketName,'is created')
        else:
            return a
        
    
    def create_folder_in_s3(self,bucketName,dirName):
        response=boto3.client('s3')
        try:
            response.put_object(Bucket=bucketName,Key=dirName + '/')
            return dirName, 'folder created in bucket', bucketName
        except Exception as e:
            print(f'error is :  {e}')
    
    def CreateEmptyFileInS3(self,bucketName,fileName,extension):
        response=boto3.client('s3')
        try:
            response.put_object(Bucket=bucketName,Key=fileName +'.' + extension)
            return fileName +'.' + extension + ' created on bucket ' + bucketName
        except Exception as e:
            print(f'error is : {e}')
    
    def list_objects_s3(self,BucketName):
        response=boto3.client('s3')
        bucket_object=[]
        try:
            for i in response.list_objects(Bucket=bucketName)['Contents']:
                bucket_object.append(i['Key'])
        except Exception as e:
            #print(f'error {bucketName} - {e}')
            pass

        if 'Contents' not in response.list_objects(Bucket=bucketName):
            return bucketName, 'bucket is empty. There is no object available'
        else:
            return f'object in the given bucket {bucketName} are: ', bucket_object 
    
    def uploadFileToS3Bucket(self,fileToUpload,bucketName,fileNameOnS3):
        response=boto3.client('s3')
        try:
            response.upload_file(Filename=fileToUpload, Bucket=bucketName, Key=fileNameOnS3)
            return fileToUpload + ' uploaded on bucket ' + bucketName + ' with file name as ' + fileNameOnS3
        except Exception as e:
            print(f'error is : {e}')

    def uploadFileToS3Bucket(self,fileToUpload,bucketName,fileNameOnS3):
        response=boto3.client('s3')
        try:
            response.upload_file(Filename=fileToUpload, Bucket=bucketName, Key=fileNameOnS3)
            return fileToUpload + ' uploaded on bucket ' + bucketName + ' with file name as ' + fileNameOnS3
        except Exception as e:
            print(f'error is : {e}')

    def DownFileFromS3Bucket(self,bucketName,fileNameOnS3,fileDownloadPath):
        response=boto3.client('s3')
        try:
            response.download_file(Bucket=bucketName, Key=fileNameOnS3, Filename=fileDownloadPath )
            return fileNameOnS3 + ' Downloaded from bucket ' + bucketName + ' tp Path ' + fileDownloadPath
        except Exception as e:
            print(f'error is : {e}')
    def deleteObjectFromS3(self,bucketName,fileName):
        response=boto3.client('s3')
        try:
            response.delete_object(Bucket=bucketName,Key=fileName)
            return fileName + ' deleted from bucket ' + bucketName
        except Exception as e:
            print(f'error is : {e}')

    def deleteBucketFromS3(self,bucketName):
        response=boto3.client('s3')
        try:
            response.delete_bucket(Bucket=bucketName)
            return bucketName + ' deleted from s3 '
        except Exception as e:
            print(f'error is :  {e}')

if __name__=="__main__":
    a=s3_object()
    i=int(input(" \n \
                Please type the number given in below text for given operation \n \
                1. List buckets from s3 \n \
                2. List Object From s3 bucket \n \
                3. Create bucket on s3 \n \
                4. CreateFolder on s3 bucket \n \
                5. Create empty File on s3 bucket \n \
                6. Upload file on s3 bucket \n \
                7. Download file from s3 bucket\n \
                8. Delete Folder and file on s3 bucket \n \
                9. Delete Bucket from s3 \n \
                \n Please provide your input here : \
                "))
    if i == 1:
        print(a.list_aws_buckets())
    elif i==2:
        bucketName=str(input("please provide bucket name to list all object: "))
        print(a.list_objects_s3(bucketName))
    elif i == 3:
        bucketName=str(input("Please provide bucket name: "))
        print(a.create_s3_bucket(bucketName))
    elif i == 4:
        bucketName=str(input("please provide bucket in which you want to create folder : "))
        dirName=str(input("please folder Name : "))
        print(a.create_folder_in_s3(bucketName,dirName))
    elif i == 5:
        bucketName=str(input("please provide bucket in which you want to create file : "))
        fileName=str(input("please file Name : "))
        extension=str(input("please file extension : "))
        print(a.CreateEmptyFileInS3(bucketName,fileName,extension))
    elif i==6:
        fileToUpload=str(input('Please provide file path with filename: '))
        bucketName=str(input('Please provide bucket name on which file need to be uploaded: '))
        fileNameOnS3=str(input('Please provide path and file name to keep on bucket : '))
        print(a.uploadFileToS3Bucket(fileToUpload,bucketName,fileNameOnS3))
    elif i==7:
        bucketName=str(input('Please provide bucket name from which file need to be Downloaded: '))
        fileNameOnS3=str(input('Please provide path and file name to Download from bucket : '))
        fileDownloadPath=str(input('Please provide file path with filename where need to be Downloaded: '))
        print(a.DownFileFromS3Bucket(bucketName,fileNameOnS3,fileDownloadPath))
    elif i==8:
        bucketName=str(input('Please provide bucket name from which file need to be deleted: '))
        fileName=str(input('Please provide path and file name to delete from bucket : '))
        print(a.deleteObjectFromS3(bucketName,fileName))
    elif i==9:
        bucketName=str(input('Please provide bucket name which needs to be deleted: '))
        print(a.deleteBucketFromS3(bucketName))
    else:
        print("Not a valid option. Please choose valid option from given one")

