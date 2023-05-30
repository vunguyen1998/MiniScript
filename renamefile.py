import os
import sys

dir_path = "D:\TRUYEN_YY\KHÍ VẬN\BETA"

i = 348
while i != 17:
    oldFileName = os.path.join(dir_path, 'Chương {}.docx'.format(i))
    newFileName = os.path.join(dir_path, 'Chương {}.docx'.format(i+3))
    os.rename(oldFileName, newFileName)
    i+=-1
print('Done')
