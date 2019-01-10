#Python script to scan directory and remove the Index File
#Created for testing OTCS 2747725
import time
import os

raw_input('Press any key to rename Index file') #Assuming direct control
def timint():
    print("Renaming files")
    os.chdir("C:\PhoenixCluster\Index") #Change directory
    for filename in os.listdir("."):
        if filename.startswith("INDEX"): #Look for index
            os.rename(filename, filename.replace ("INDEX" , "index_complete")) #Replacing file
        elif filename.startswith("index_"):
            os.remove(filename)
    time.sleep(30)
while True:             #repeat program
    timint()
    print("Allowing Workserver time to process...")
