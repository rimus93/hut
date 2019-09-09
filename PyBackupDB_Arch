# PyBackupDB_Arch 0.1

import os
import time
import shutil
import glob
import subprocess

# Указываем папку Прогресса
dlcbin = 'C:\\Progress10B\\bin\\'
# Указываем папку БД
db = 'C:\\DB\\ub'
# Определяем текущую дату
day = int(time.strftime('%d'))
# Указываем, сколько хранить бекапы
if int(day) <= 14:
    pastday = day + 17
else:
    pastday = day - 14
# Определяем разрядность даты/новый бекап
bkpfile = 'ub.bkp_' + str(day)
# Определяем старый заархивированный бекап
bkpfileold = 'ub.bkp_' + str(pastday) + '.7z'
# Указываем папку для нового бэкапа
newbkp = 'C:\\backup_BD\\'
# Указываем папку для старого бэкапа
oldbkp = 'C:\\backup_BD\OLD_BKP\\'
# Указываем папку для бэкапа на сетевом диске
extbkp = 'C:\\Murmansk_DB_Backup\\'
# Указываем папку для хранения логов
logdir = 'C:\\backup_BD\\'
# Указываем папку архиватора
archdir = 'C:\\backup_BD\\7-Zip\\'

print(dlcbin)
print(db)
print(day)
print(pastday)
print(bkpfile)
print(bkpfileold)
print(newbkp)
print(oldbkp)
print(extbkp)
print(logdir)
print(archdir)

if not os.path.isdir(newbkp):
    os.mkdir(newbkp)
    print('Папка ' + newbkp + ' создана')
else:
    print('Папка ' + newbkp + ' существует')

if not os.path.isdir(oldbkp):
    os.mkdir(oldbkp)
    print('Папка ' + oldbkp + ' создана')
else:
    print('Папка ' + oldbkp + ' существует')

if not os.path.isdir(extbkp):
    os.mkdir(extbkp)
    print('Папка ' + extbkp + ' создана')
else:
    print('Папка ' + extbkp + ' существует')

if not os.path.isdir(logdir):
    os.mkdir(logdir)
    print('Папка ' + logdir + ' создана')
else:
    print('Папка ' + logdir + ' существует')

if not os.path.isdir(archdir):
    os.mkdir(archdir)
    print('Папка ' + archdir + ' создана')
else:
    print('Папка ' + archdir + ' существует')

if os.path.exists(newbkp + 'ub.st'):
    shutil.copy(newbkp + 'ub.st', oldbkp)
    print('Файл ' + newbkp + 'ub.st' + ' скопирован в ' + oldbkp)
else:
    print('Файл ' + newbkp + 'ub.st' + ' отсутствует')

if True:
    oldarchs = glob.glob(oldbkp + '*7z')
    for arch7 in oldarchs:
        os.remove(arch7)
        print('Файл ' + arch7 + ' удалён из ' + oldbkp)
        break
    else:
        print('Файлы ' + oldbkp + '*.7z' + ' отсутствуют')

if True:
    for arch7 in glob.glob(newbkp + '*.7z'):
        shutil.move(arch7, oldbkp)
        print('Файл ' + arch7 + ' перемещён в ' + oldbkp)
        break
    else:
        print('Файлы ' + newbkp + '*.7z' + ' отсутствуют')

# subprocess.call([dlcbin + 'probkup', 'online', db, oldbkp + bkpfile])

subprocess.call([archdir + '7z.exe', 'a', newbkp + bkpfile + '.7z', newbkp + bkpfile, '-y', '-sdel'])

if os.path.exists(db + '.st'):
    shutil.copy(db + '.st', newbkp)
    print('Файл ' + db + '.st' + ' скопирован в ' + newbkp)
else:
    print('Файл ' + db + '.st' + ' отсутствует')

# subprocess.call('cmd /c "net use X: \\\\172.168.0.1\\backup /172.168.0.1\user userpassword"')

if os.path.exists(newbkp + 'ub.st'):
    shutil.copy(newbkp + 'ub.st', extbkp)
    print('Файл ' + newbkp + 'ub.st' + ' скопирован в ' + extbkp)
else:
    print('Файл ' + newbkp + 'ub.st' + ' отсутствует')

if os.path.exists(extbkp + bkpfileold):
    os.remove(extbkp + bkpfileold)
    print('Файл ' + bkpfileold + ' удалён из ' + extbkp)
else:
    print('Файл ' + extbkp + bkpfileold + ' отсутствует')

if os.path.exists(newbkp + bkpfile + '.7z'):
    shutil.copy(newbkp + bkpfile + '.7z', extbkp)
    print('Файл ' + newbkp + bkpfile + '.7z' + ' скопирован в ' + extbkp)
else:
    print('Файл ' + newbkp + bkpfile + '.7z' + ' отсутствует')

# Бэкапирование завершено!
