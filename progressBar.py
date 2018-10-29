import time, sys


def progressBar(pValue):
    barSize = 40 
    if(isinstance(pValue, int)):
        progress = float(pValue)

        
    block = int(round(barSize*pValue))
    if(block > barSize):
        block = barSize
        pValue = 0.99

        
    progress = "\rDownloading: [{0}] {1}% ".format( "#"*block + "_"*(barSize-block), pValue*100)
    sys.stdout.write(progress)
    sys.stdout.flush()


count  = 1
while True:
    time.sleep(0.1)
    progressBar(count/1000.0)
    count += 1

    if(count == 10000):
        break


print("\nDownload completed\n")
time.sleep(1)
