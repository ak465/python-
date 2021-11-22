import dropbox

class TransferData:
   def __init__(self, access_token):
       self.access_token = access_token

   def Transfer(self, file_from, file_to):
       dbx = dropbox.Dropbox(self.access_token)
       with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token="loXN1nTcPW8AAAAAAAAAAaXXT63mbhD3rFzeG8BQK6722K4Wg8gHtSN8K6t1Tf0_"
    transferData = TransferData(access_token)
    file_from = input("enter the file path: ")
    file_to  = input("enter the file to upload: ")
    transferData.Transfer(file_from, file_to)
    print("Your file has been uploaded successfully")
main()

