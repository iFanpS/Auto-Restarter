from os import name
import sys
import os

copyright = """
==============================
This auto-restarter by iFanpS
100% Made sendiri
(c) iFanpS 2020
==============================
"""
print(copyright)
nama = input("Taruh nama file: ")

def ulang():
    ulang1 = input("File is Crash wanna restart? (y/n) ")
    if ulang1 == "y":
        os.system(f"{nama}.exe")
    if ulang1 == "no":
        exit()

def berjalan():
    os.system(f"{nama}.exe")
    print("Auto restarter has active")

if __name__ == "__main__":
    try:
         berjalan()
         time.sleep(20)
         ulang()
    except OSError:
        sys.exit("Error! please try again")
