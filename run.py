import nvsmi
import time
import os
import sys

def clear():
    consoleType = os.name
    if (consoleType == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def printProgressBar (currentValue, maxValue, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        currentValue - Required  : current value (Int)
        maxValue     - Required  : max value (Int)
        prefix       - Optional  : prefix string (Str)
        suffix       - Optional  : suffix string (Str)
        decimals     - Optional  : positive number of decimals in percent complete (Int)
        length       - Optional  : character length of bar (Int)
        fill         - Optional  : bar fill character (Str)
        printEnd     - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (currentValue / float(maxValue)))
    filledLength = int(length * currentValue // maxValue)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'{prefix} |{bar}| {percent} {suffix}', end = printEnd)

def vramToGb(vramMb):
    return round(vramMb/1000,1)

def spinnerWait():
    updatePeriodSeconds = 3 # TODO: args
    spinner = ["/","-","\\","|","/","-","\\","|","/","-"]
    #spinner2 = ["←", "↑", "→", "↓",]
    print("CTRL-C to exit") 
    for i in range(1,len(spinner)):
            print(spinner[i-1], end = "\r")
            time.sleep(updatePeriodSeconds/len(spinner))
    print(" updating...")

def printGpus():
    gpus = nvsmi.get_gpus()
    clear()
    print()

    for gpu in gpus:
        vramGb = vramToGb(vramMb = gpu.mem_total)
        print(f"GPU ID: {gpu.id}, Name: {gpu.name}, VRAM: {vramGb} GB, Temp: {gpu.temperature}C")            
        line2Prefix = f"     GPU Util:"
        printProgressBar(currentValue = gpu.mem_used, maxValue = gpu.mem_total, prefix = "   GPU Memory:", suffix= "%", length=50, printEnd ="\n")
        printProgressBar(currentValue = gpu.gpu_util, maxValue = 100, prefix = line2Prefix, suffix= "%", length=50, printEnd ="\n")
        print()  

def main():
    clear()
    print("Starting Simple NV-SMI monitor...")
    print()

    header = []
    header.append("  ======== Monitoring ========")
    
    header.append("  ============================  ")
    header.append("")

    while 1==1:
        printGpus()        
        spinnerWait()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)