#file
from nvsmi import nvsmi
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
        printProgressBar(currentValue = gpu.mem_used, maxValue = gpu.mem_total, prefix = "    Memory:", suffix= f"%   {gpu.mem_used} / {gpu.mem_total} MB", length=50, printEnd ="\n")
        printProgressBar(currentValue = gpu.gpu_util, maxValue = 100, prefix = f"      Util:", suffix= f"%", length=50, printEnd ="\n")
        printProgressBar(currentValue = gpu.power_draw, maxValue = gpu.enforced_power_limit, prefix = '     Power:', suffix= f"%   {gpu.power_draw:.1F} / {gpu.enforced_power_limit:.0F} W", length=50, printEnd ="\n")
        #print(f'    Power: {gpu.power_draw:.1F} / {gpu.enforced_power_limit:.0F} W')
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