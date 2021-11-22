import cv2
import dropbox
import time
import random

startTime=time.time()

def takesnap():
    num = random.randint(0, 100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        imageName="image"+str(num)+".png"
        cv2.imwrite(imageName,frame)
        result=False

    VideoCaptureObject.release()
    cv2.destroyAllWindows()
    print("snapshoot taken") 
    return imageName  
    

def uploadFiles(imageName):
    accessToken="loXN1nTcPW8AAAAAAAAAAaXXT63mbhD3rFzeG8BQK6722K4Wg8gHtSN8K6t1Tf0_"
    file_from=imageName
    file_to="/images/"+ imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
        
def main():
    while(True):
        if(time.time()-startTime>=5):
            name=takesnap()
            uploadFiles(name)


main()






# imwrite accepts 2 things
#     -name of the image which you are saving
#     -which image you are saving




