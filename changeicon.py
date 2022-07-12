from asyncio import sleep
import sys
import os
import convert
import time
#attrib +s +h [pathtofolder]\desktop.ini
#attrib +r [pathtofolder]
#[.ShellClassInfo]
#IconResource=C:\FolderIcon.ico,0
def change_icon(folder_Path):
    with open(folder_Path+"/desktop.txt","w") as decorating_file:
        decorating_file.write("[.ShellClassInfo]\n")
        decorating_file.write(f'IconResource="{folder_Path}\icon.ico",0\n')
    os.rename(folder_Path+"\desktop.txt",folder_Path+"\desktop.ini")
    os.system(f'attrib +r "{folder_Path}"')
    os.system(f'attrib +s +h "{folder_Path}\desktop.ini"')
convert.change_size(r"E:\folder project\newfolder")
convert.convert(r"E:\folder project\newfolder")
change_icon(r"E:\folder project\newfolder")