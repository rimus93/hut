# PyBackupDB_Arch 0.2
# -*- coding: utf-8 -*-

import os
import time
import shutil
import glob
import subprocess

# Указываем папку СУБД Прогресс
dlcbin = 'C:\\Progress10B\\bin\\'
# Указываем папку БД
db = 'C:\\DB\\ub'
# Определяем текущий день месяца
day = int(time.strftime('%d'))
# Определяем текущий момент времени для логирования
now = time.strftime("%Y-%m-%d-%H:%M:%S ")
# Указываем, сколько дней хранить бекапы, в данном случае - 14 дней
if int(day) <= 14:
    pastday = day + 17
else:
    pastday = day - 14
# Исходный файл для проверки нового бекапа
bkpverify = 'backup_online.db'
# Определяем разрядность даты/название нового бекапа
bkpfile = 'backup_online.db_' + str(day)
# Определяем старый заархивированный бекап
bkpfileold = 'backup_online.db_' + str(pastday) + '.7z'
# Указываем папку для нового бэкапа
newbkp = 'C:\\backup_BD\\'
# Указываем папку для старого бэкапа
oldbkp = 'C:\\backup_BD\OLD_BKP\\'
# Указываем папку для бэкапа на внешнем хранилище
extbkp = 'C:\\Murmansk_DB_Backup\\'
# Указываем файл для логирования
log = open('C:\\backup_BD\\log_backup.txt', 'a')
# Указываем папку для хранения логов
logdir = 'C:\\backup_BD\\'
# Указываем папку архиватора
archdir = 'C:\\backup_BD\\7-Zip\\'

print('Папка СУБД Прогресс: ' + dlcbin, file = log)
print('Папка БД: ' + db, file = log)
print('Сегодняшний день месяца: ' + str(day), file = log)
print('Бекап будет удалён за ' + str(pastday) + ' день месяца', file = log)
print('Новый бэкап: ' + bkpfile, file = log)
print('Старый бэкап для удаления: ' + bkpfileold, file = log)
print('Папка нового бэкапа: ' + newbkp, file = log)
print('Папка старого бэкапа: ' + oldbkp, file = log)
print('Папка внешнего хранилища: ' + extbkp, file = log)
print('Папка для хранения логов: ' + logdir, file = log)
print('Папка архиватора: ' + archdir, file = log)

print(now + '***Бекапирование начато!***', file = log)

if not os.path.isdir(newbkp):
    os.mkdir(newbkp)
    print('Папка ' + newbkp + ' создана', file = log)
else:
    print('Папка ' + newbkp + ' существует', file = log)

if not os.path.isdir(oldbkp):
    os.mkdir(oldbkp)
    print('Папка ' + oldbkp + ' создана', file = log)
else:
    print('Папка ' + oldbkp + ' существует', file = log)

if not os.path.isdir(extbkp):
    os.mkdir(extbkp)
    print('Папка ' + extbkp + ' создана', file = log)
else:
    print('Папка ' + extbkp + ' существует', file = log)

if not os.path.isdir(logdir):
    os.mkdir(logdir)
    print('Папка ' + logdir + ' создана', file = log)
else:
    print('Папка ' + logdir + ' существует', file = log)

if not os.path.isdir(archdir):
    os.mkdir(archdir)
    print('Папка ' + archdir + ' создана', file = log)
else:
    print('Папка ' + archdir + ' существует', file = log)

if os.path.exists(newbkp + 'ub.st'):
    shutil.copy(newbkp + 'ub.st', oldbkp)
    print(now + 'Файл ' + newbkp + 'ub.st' + ' скопирован в ' + oldbkp, file = log)
else:
    print(now + 'Файл ' + newbkp + 'ub.st' + ' отсутствует', file = log)

if True:
    oldarchs = glob.glob(oldbkp + '*7z')
    for arch7 in oldarchs:
        os.remove(arch7)
        print(now + 'Файл ' + arch7 + ' удалён из ' + oldbkp, file = log)
        break
    else:
        print(now + 'Файлы ' + oldbkp + '*.7z' + ' отсутствуют', file = log)

if True:
    for arch7 in glob.glob(newbkp + '*.7z'):
        shutil.move(arch7, oldbkp)
        print(now + 'Файл ' + arch7 + ' перемещён в ' + oldbkp, file = log)
        break
    else:
        print(now + 'Файлы ' + newbkp + '*.7z' + ' отсутствуют', file = log)

with open ('log', 'a') as f:
    subprocess.call([dlcbin + 'probkup.bat', 'online', db + '.db', newbkp + bkpverify, '-Bp', '20'], stdout = f, shell = True)
print(now + 'Файл бекапа ' + newbkp + bkpverify + ' создан', file = log)

with open ('log', 'a') as f:
    subprocess.call([dlcbin + 'prorest.bat', db, newbkp + bkpverify, '-Bp', '20', '-vp'], stdout = f, shell = True)
print(now + 'Файл бекапа ' + newbkp + bkpverify + ' проверен', file = log)

os.rename(newbkp + bkpverify, newbkp + bkpfile)
print(now + 'Проверенный файл бекапа ' + newbkp + bkpverify + ' переименован в ' + newbkp + bkpfile, file = log)

with open ('log', 'a') as f:
    subprocess.call([archdir + '7z.exe', 'a', newbkp + bkpfile + '.7z', newbkp + bkpfile, '-y', '-sdel'], stdout = f, shell = True)
print(now + 'Файл бэкапа ' + newbkp + bkpfile + ' заархивирован в ' + newbkp + '*.7z', file = log)

if os.path.exists(db + '.st'):
    shutil.copy(db + '.st', newbkp)
    print(now + 'Файл ' + db + '.st' + ' скопирован в ' + newbkp, file = log)
else:
    print(now + 'Файл ' + db + '.st' + ' отсутствует', file = log)

if os.path.exists(newbkp + 'ub.st'):
    shutil.copy(newbkp + 'ub.st', extbkp)
    print(now + 'Файл ' + newbkp + 'ub.st' + ' скопирован в ' + extbkp, file = log)
else:
    print(now + 'Файл ' + newbkp + 'ub.st' + ' отсутствует', file = log)

if os.path.exists(extbkp + bkpfileold):
    os.remove(extbkp + bkpfileold)
    print(now + 'Файл ' + bkpfileold + ' удалён из ' + extbkp, file = log)
else:
    print(now + 'Файл ' + extbkp + bkpfileold + ' отсутствует', file = log)

if os.path.exists(newbkp + bkpfile + '.7z'):
    shutil.copy(newbkp + bkpfile + '.7z', extbkp)
    print(now + 'Файл ' + newbkp + bkpfile + '.7z' + ' скопирован в ' + extbkp, file = log)
else:
    print(now + 'Файл ' + newbkp + bkpfile + '.7z' + ' отсутствует', file = log)

print(now + '***Бэкапирование успешно завершено!***', file = log)
