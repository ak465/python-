import os
import shutil

source= input("enter the source")
destination= input("enter the destination")
source=source+"/"
destination=destination+"/"

name=os.listdir(source)
for line in name:
    shutil.copy((source+line),destination) 

