#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random
import time
import json
import os
import sys
import string
import re
import hashlib
import datetime
import subprocess
import platform
import base64
import socket
import threading
from datetime import datetime, timedelta
from colorama import init, Fore, Style, Back

init(autoreset=True)
os.system("clear" if os.name == "posix" else "cls")

# ============================================
# 🔥 KONFIGURASI 🔥
# ============================================

VERSION = "PREMIUM 21.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"
EGAA_PASSWORD = "alegra123"
DEVELOPER_PASSWORD = "9999"

DATA_FILE = os.path.expanduser("~/.alegra_premium_data.json")
LOG_FILE = os.path.expanduser("~/.alegra_premium_log.txt")
OWNER_FILE = os.path.expanduser("~/.alegra_owners.json")
HEAD_OWNER = "egaa"
CHAT_FILE = os.path.expanduser("~/.alegra_chat.json")

# ============================================
# 🔥 BANNER 🔥
# ============================================

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""
{Fore.CYAN}
╔═══════════════════════════════════════════╗
║  █████  ██▓     ██████  ▄████▄   ██▀███  ║
║ ▒█   ▀ ▓██▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██║
║ ░▒███  ▒██░   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒║
║ ▒▓█  ▄ ▒██░     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ║
║ ░▒████▒░██████▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒║
║ ░░ ▒░ ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓║
║  ░ ░  ░░ ░ ▒  ░░ ░▒  ░ ░  ░  ▒    ░▒ ░ ▒║
║    ░     ░ ░   ░  ░  ░  ░         ░░   ░ ║
║    ░  ░    ░  ░      ░  ░ ░        ░     ║
║                          ░                 ║
╚═══════════════════════════════════════════╝
{Fore.YELLOW}     📨 ALEGRA SPAM - PREMIUM EDITION
{Fore.GREEN}          BY {egaaaXc} | {egaa_1}
{Fore.CYAN}         GAS LEK GAS! 🔥
{Fore.RESET}""")

# ============================================
# 🔥 DATA MANAGEMENT 🔥
# ============================================

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_activity(text):
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}\n")
    except:
        pass

def load_owners():
    if os.path.exists(OWNER_FILE):
        try:
            with open(OWNER_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_owners(data):
    with open(OWNER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_user_role(username):
    data = load_data()
    if username in data:
        return data[username].get('role', 'MEMBER')
    owners = load_owners()
    if username in owners:
        return owners[username].get('role', 'ADMIN')
    if username == HEAD_OWNER:
        return "DEVELOPER"
    return "GUEST"

# ============================================
# 🔥 PASSWORD FUNCTIONS 🔥
# ============================================

def create_password(username, duration_hours, role='MEMBER'):
    data = load_data()
    if username in data:
        expired = datetime.fromisoformat(data[username]['expired'])
        if expired > datetime.now():
            return None, "❌ Username sudah punya password aktif!"
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=8))
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if duration_hours == 0:
        expired_time = datetime.now() + timedelta(days=365*100)
        durasi_text = "PERMANEN"
    else:
        expired_time = datetime.now() + timedelta(hours=duration_hours)
        durasi_text = f"{duration_hours} jam"
    data[username] = {
        'password': hashed,
        'expired': expired_time.isoformat(),
        'created': datetime.now().isoformat(),
        'duration': durasi_text,
        'role': role
    }
    save_data(data)
    log_activity(f"Create password untuk {username} ({durasi_text}) role: {role}")
    return password, f"✅ Username: {username}\n Password: {password}\n Role: {role}\n Expired: {durasi_text}"

def verify_password(username, password):
    data = load_data()
    if username in data:
        user_data = data[username]
        expired = datetime.fromisoformat(user_data['expired'])
        if expired < datetime.now():
            return False, "❌ Password sudah expired!"
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if hashed == user_data['password']:
            log_activity(f"Login berhasil: {username}")
            role = user_data.get('role', 'MEMBER')
            return True, f"✅ Login berhasil! Role: {role}"
    if username == HEAD_OWNER and password == DEVELOPER_PASSWORD:
        log_activity(f"Developer login: {username}")
        return True, "✅ Login berhasil! Role: DEVELOPER"
    return False, "❌ Username atau password salah!"

# ============================================
# 🔥 PUBLIC TOOLS 🔥
# ============================================

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        return ip
    except:
        return "Gagal mendapatkan IP"

def check_website():
    show_banner()
    print(f"{Fore.CYAN}🌐 CEK WEBSITE ONLINE/OFFLINE")
    url = input(f"{Fore.WHITE}URL: ").strip()
    if not url:
        print(f"{Fore.RED}❌ URL tidak boleh kosong!")
        time.sleep(1)
        return
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{Fore.GREEN}✅ ONLINE! (Status: {response.status_code})")
        else:
            print(f"{Fore.YELLOW}⚠️ RESPOND (Status: {response.status_code})")
    except:
        print(f"{Fore.RED}❌ OFFLINE / TIDAK TERJANGKAU!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def ip_lookup():
    show_banner()
    print(f"{Fore.CYAN}🔍 IP LOOKUP")
    ip = input(f"{Fore.WHITE}IP: ").strip()
    if not ip:
        print(f"{Fore.RED}❌ IP tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        if data['status'] == 'success':
            print(f"{Fore.GREEN}📌 INFO IP {ip}:")
            print(f"{Fore.WHITE} • Negara : {data.get('country', '-')}")
            print(f"{Fore.WHITE} • Kota : {data.get('city', '-')}")
            print(f"{Fore.WHITE} • ISP : {data.get('isp', '-')}")
            print(f"{Fore.WHITE} • Region : {data.get('regionName', '-')}")
            print(f"{Fore.WHITE} • Timezone: {data.get('timezone', '-')}")
        else:
            print(f"{Fore.RED}❌ Gagal!")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def dns_lookup():
    show_banner()
    print(f"{Fore.CYAN}🌐 DNS LOOKUP")
    domain = input(f"{Fore.WHITE}Domain: ").strip()
    if not domain:
        print(f"{Fore.RED}❌ Domain tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}✅ {domain} → {ip}")
    except:
        print(f"{Fore.RED}❌ Gagal!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def base64_tool():
    show_banner()
    print(f"{Fore.CYAN}🔐 BASE64 ENCODE/DECODE")
    print(f"{Fore.GREEN}[1] {Fore.WHITE}Encode")
    print(f"{Fore.GREEN}[2] {Fore.WHITE}Decode")
    choice = input(f"{Fore.CYAN}Pilih: ").strip()
    text = input(f"{Fore.WHITE}Teks: ").strip()
    if not text:
        print(f"{Fore.RED}❌ Teks tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        if choice == '1':
            result = base64.b64encode(text.encode()).decode()
            print(f"{Fore.GREEN}✅ Hasil Encode: {Fore.WHITE}{result}")
        elif choice == '2':
            result = base64.b64decode(text).decode()
            print(f"{Fore.GREEN}✅ Hasil Decode: {Fore.WHITE}{result}")
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def system_info():
    show_banner()
    print(f"{Fore.CYAN}📊 INFO SISTEM")
    print(f"{Fore.WHITE} • OS : {platform.system()} {platform.release()}")
    print(f"{Fore.WHITE} • Hostname: {platform.node()}")
    print(f"{Fore.WHITE} • Python : {platform.python_version()}")
    print(f"{Fore.WHITE} • Arch : {platform.machine()}")
    print(f"{Fore.WHITE} • CPU : {platform.processor() or 'Unknown'}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def device_info():
    show_banner()
    print(f"{Fore.CYAN}📱 INFO HP")
    try:
        model = subprocess.getoutput("getprop ro.product.model")
        brand = subprocess.getoutput("getprop ro.product.brand")
        android = subprocess.getoutput("getprop ro.build.version.release")
        print(f"{Fore.WHITE} • Model : {model}")
        print(f"{Fore.WHITE} • Brand : {brand}")
        print(f"{Fore.WHITE} • Android : {android}")
    except:
        print(f"{Fore.RED} • Info HP : Tidak tersedia")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def public_ip():
    show_banner()
    print(f"{Fore.CYAN}🌍 CEK IP PUBLIK")
    ip = get_public_ip()
    print(f"{Fore.GREEN}✅ IP Publik: {Fore.WHITE}{ip}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def email_validator():
    show_banner()
    print(f"{Fore.CYAN}📧 EMAIL VALIDATOR")
    email = input(f"{Fore.WHITE}Email: ").strip()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{Fore.GREEN}✅ VALID")
    else:
        print(f"{Fore.RED}❌ INVALID")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def calculator():
    show_banner()
    print(f"{Fore.CYAN}🧮 KALKULATOR")
    try:
        expr = input(f"{Fore.WHITE}Operasi (2+3): ").strip()
        result = eval(expr)
        print(f"{Fore.WHITE}Hasil: {result}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_number():
    show_banner()
    print(f"{Fore.CYAN}🔢 RANDOM NUMBER")
    try:
        min_num = int(input(f"{Fore.WHITE}Min: ").strip() or "1")
        max_num = int(input(f"{Fore.WHITE}Max: ").strip() or "100")
        print(f"{Fore.WHITE}Random: {random.randint(min_num, max_num)}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_password():
    show_banner()
    print(f"{Fore.CYAN}📝 RANDOM PASSWORD")
    try:
        length = int(input(f"{Fore.WHITE}Panjang: ").strip() or "12")
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=length))
        print(f"{Fore.WHITE}Password: {password}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def reverse_text():
    show_banner()
    print(f"{Fore.CYAN}📝 REVERSE TEXT")
    text = input(f"{Fore.WHITE}Teks: ").strip()
    print(f"{Fore.WHITE}Reverse: {text[::-1]}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def case_converter():
    show_banner()
    print(f"{Fore.CYAN}📝 CASE CONVERTER")
    print(f"{Fore.GREEN}[1] {Fore.WHITE}UPPER")
    print(f"{Fore.GREEN}[2] {Fore.WHITE}lower")
    print(f"{Fore.GREEN}[3] {Fore.WHITE}Title")
    choice = input(f"{Fore.CYAN}Pilih: ").strip()
    text = input(f"{Fore.WHITE}Teks: ").strip()
    if choice == '1':
        print(f"{Fore.WHITE}{text.upper()}")
    elif choice == '2':
        print(f"{Fore.WHITE}{text.lower()}")
    elif choice == '3':
        print(f"{Fore.WHITE}{text.title()}")
    else:
        print(f"{Fore.RED}❌ Pilihan tidak valid!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def cek_nomor_telpon():
    show_banner()
    print(f"{Fore.CYAN}📱 CEK NOMOR TELPON")
    nomor = input(f"{Fore.WHITE}Nomor (contoh: 6281234567890): ").strip()
    if not nomor:
        print(f"{Fore.RED}❌ Nomor tidak boleh kosong!")
        time.sleep(1)
        return
    nomor = re.sub(r'[^0-9]', '', nomor)
    if nomor.startswith('0'):
        nomor = '62' + nomor[1:]
    elif not nomor.startswith('62'):
        nomor = '62' + nomor
    print(f"{Fore.CYAN}⏳ Mengecek nomor {nomor}...")
    time.sleep(1)
    operators = ["Telkomsel", "Indosat", "XL", "Tri", "Smartfren", "By.U", "Axis"]
    status_options = ["AKTIF", "OFFLINE", "TERBLOKIR", "TIDAK TERDAFTAR"]
    status = random.choice(status_options)
    operator = random.choice(operators)
    if status == "AKTIF":
        status_color = Fore.GREEN
        info = "✅ Nomor terdaftar dan aktif"
    elif status == "OFFLINE":
        status_color = Fore.YELLOW
        info = "⚠️ Nomor terdaftar tapi sedang offline"
    elif status == "TERBLOKIR":
        status_color = Fore.RED
        info = "❌ Nomor diblokir"
    else:
        status_color = Fore.RED
        info = "❌ Nomor tidak terdaftar"
    print(f"\n{Fore.GREEN}📌 HASIL CEK NOMOR:")
    print(f"{Fore.WHITE} • Nomor : {nomor}")
    print(f"{Fore.WHITE} • Status : {status_color}{status}{Fore.WHITE}")
    print(f"{Fore.WHITE} • Operator : {operator}")
    print(f"{Fore.WHITE} • Info : {info}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def chat_global():
    show_banner()
    print(f"{Fore.CYAN}💬 CHAT GLOBAL")
    username = input(f"{Fore.WHITE}Nama kamu: ").strip() or "Anonim"
    while True:
        print(f"\n{Fore.CYAN}┌────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│ {Fore.YELLOW}[1] {Fore.WHITE}Lihat Pesan {Fore.YELLOW}[2] {Fore.WHITE}Kirim {Fore.YELLOW}[3] {Fore.WHITE}Exit {Fore.CYAN}│")
        print(f"{Fore.CYAN}└────────────────────────────────────────────────┘")
        choice = input(f"{Fore.CYAN}Pilih: ").strip()
        if choice == '1':
            if os.path.exists(CHAT_FILE):
                try:
                    with open(CHAT_FILE, 'r') as f:
                        chat_data = json.load(f)
                    if chat_data:
                        print(f"\n{Fore.CYAN}📋 PESAN TERBARU:")
                        print(f"{Fore.CYAN}" + "═" * 50)
                        for msg in chat_data[-20:]:
                            waktu = msg.get('time', '')
                            nama = msg.get('name', 'Anonim')
                            pesan = msg.get('message', '')
                            print(f"{Fore.WHITE}[{waktu}] {Fore.GREEN}{nama}{Fore.WHITE}: {pesan}")
                        print(f"{Fore.CYAN}" + "═" * 50)
                    else:
                        print(f"{Fore.YELLOW}⚠️ Belum ada pesan.")
                except:
                    print(f"{Fore.YELLOW}⚠️ Belum ada pesan.")
            else:
                print(f"{Fore.YELLOW}⚠️ Belum ada pesan.")
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
        elif choice == '2':
            pesan = input(f"{Fore.CYAN}[+] Pesan: {Fore.WHITE}").strip()
            if pesan:
                chat_data = []
                if os.path.exists(CHAT_FILE):
                    try:
                        with open(CHAT_FILE, 'r') as f:
                            chat_data = json.load(f)
                    except:
                        chat_data = []
                chat_data.append({
                    'name': username,
                    'message': pesan,
                    'time': datetime.now().strftime('%H:%M:%S')
                })
                with open(CHAT_FILE, 'w') as f:
                    json.dump(chat_data, f, indent=2)
                print(f"{Fore.GREEN}✅ Pesan terkirim!")
            else:
                print(f"{Fore.RED}❌ Pesan tidak boleh kosong!")
            time.sleep(1)
        elif choice == '3':
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

def public_tools():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}🌍 PUBLIC TOOLS {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}🌐 Cek Website {Fore.GREEN}[8] {Fore.WHITE}📱 Info HP {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}🔍 IP Lookup {Fore.GREEN}[9] {Fore.WHITE}🌍 IP Publik {Fore.CYAN}│
│ {Fore.GREEN}[3] {Fore.WHITE}🌐 DNS Lookup {Fore.GREEN}[10]{Fore.WHITE}📧 Email Valid {Fore.CYAN}│
│ {Fore.GREEN}[4] {Fore.WHITE}🔐 Base64 {Fore.GREEN}[11]{Fore.WHITE}🧮 Kalkulator {Fore.CYAN}│
│ {Fore.GREEN}[5] {Fore.WHITE}📊 Info Sistem {Fore.GREEN}[12]{Fore.WHITE}🔢 Random Number {Fore.CYAN}│
│ {Fore.GREEN}[6] {Fore.WHITE}📱 Cek Nomor {Fore.GREEN}[13]{Fore.WHITE}📝 Random Password {Fore.CYAN}│
│ {Fore.GREEN}[7] {Fore.WHITE}💬 Chat Global {Fore.GREEN}[14]{Fore.WHITE}📝 Reverse Text {Fore.CYAN}│
│ {Fore.GREEN}[15]{Fore.WHITE}📝 Case Converter {Fore.GREEN}[16]{Fore.WHITE}🔙 EXIT {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}""")
        choice = input(f"{Fore.CYAN}Pilih [1-16]: {Fore.WHITE}").strip()
        if choice == '1': check_website()
        elif choice == '2': ip_lookup()
        elif choice == '3': dns_lookup()
        elif choice == '4': base64_tool()
        elif choice == '5': system_info()
        elif choice == '6': cek_nomor_telpon()
        elif choice == '7': chat_global()
        elif choice == '8': device_info()
        elif choice == '9': public_ip()
        elif choice == '10': email_validator()
        elif choice == '11': calculator()
        elif choice == '12': random_number()
        elif choice == '13': random_password()
        elif choice == '14': reverse_text()
        elif choice == '15': case_converter()
        elif choice == '16':
            print(f"{Fore.YELLOW}🔙 Kembali...")
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 SPAM NGL 🔥
# ============================================

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/605.1.15 Version/16.0",
    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/20100101 Firefox/115.0",
]

DEVICE_IDS = [
    "android-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
    "ios-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
    "web-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
]

def random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": "https://ngl.link",
        "Origin": "https://ngl.link",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Connection": "keep-alive"
    }

def extract_username(input_text):
    input_text = input_text.strip()
    patterns = [
        r'https?://ngl\.link/([a-zA-Z0-9_]+)',
        r'https?://www\.ngl\.link/([a-zA-Z0-9_]+)',
        r'ngl\.link/([a-zA-Z0-9_]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, input_text)
        if match:
            return match.group(1)
    if input_text.startswith('@'):
        input_text = input_text[1:]
    username = re.sub(r'[^a-zA-Z0-9_]', '', input_text)
    return username if username else None

def send_ngl_message(username, message, retry=0):
    try:
        device_id = random.choice(DEVICE_IDS)
        payload = {
            "username": username.strip().replace("@", ""),
            "question": message,
            "deviceId": device_id
        }
        headers = random_headers()
        response = requests.post("https://ngl.link/api/submit", json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("status") == "success" or data.get("message") == "Question sent successfully":
                    return True, "✅ BERHASIL!"
                return False, f"❌ GAGAL: {data.get('message', 'Unknown error')}"
            except:
                return True, "✅ BERHASIL!"
        elif response.status_code == 429:
            if retry < 3:
                time.sleep(2)
                return send_ngl_message(username, message, retry + 1)
            return False, "⏳ RATE LIMIT!"
        elif response.status_code == 400:
            return False, "❌ USERNAME SALAH!"
        elif response.status_code == 404:
            return False, "❌ USERNAME TIDAK DITEMUKAN!"
        else:
            return False, f"❌ ERROR {response.status_code}"
    except Exception as e:
        if retry < 3:
            time.sleep(2)
            return send_ngl_message(username, message, retry + 1)
        return False, f"❌ ERROR: {str(e)[:30]}"

def spam_ngl():
    show_banner()
    print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}📨 SPAM NGL - PREMIUM EDITION {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
Support 2 tipe input:
{Fore.YELLOW} 1. https://ngl.link/username
{Fore.YELLOW} 2. username
{Fore.WHITE}""")
    raw_input = input(f"{Fore.CYAN}[+] USERNAME / LINK: {Fore.WHITE}").strip()
    if not raw_input:
        print(f"{Fore.RED}❌ Input tidak boleh kosong!")
        time.sleep(1)
        return
    username = extract_username(raw_input)
    if not username:
        print(f"{Fore.RED}❌ GAGAL! Format tidak valid!")
        time.sleep(1)
        return
    print(f"{Fore.GREEN}✅ USERNAME: @{username}")
    message = input(f"{Fore.CYAN}[+] PESAN SPAM: {Fore.WHITE}").strip()
    if not message:
        print(f"{Fore.RED}❌ Pesan tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        count = int(input(f"{Fore.CYAN}[+] JUMLAH (1-9999): {Fore.WHITE}").strip() or "100")
        count = max(1, min(9999, count))
    except:
        count = 100
        print(f"{Fore.YELLOW}⚠️ Default: 100")
    try:
        delay = float(input(f"{Fore.CYAN}[+] DELAY (0.1-5): {Fore.WHITE}").strip() or "0.5")
        delay = max(0.1, min(5, delay))
    except:
        delay = 0.5
        print(f"{Fore.YELLOW}⚠️ Default: 0.5s")
    print(f"{Fore.RED}\n[!] PERINGATAN: Untuk iseng-iseng!")
    confirm = input(f"{Fore.YELLOW}[?] Lanjut? (y/n): {Fore.WHITE}").strip().lower()
    if confirm != 'y':
        print(f"{Fore.YELLOW}[!] Dibatalkan!")
        time.sleep(1)
        return
    print(f"{Fore.GREEN}\n[+] TARGET: @{username}")
    print(f"{Fore.GREEN}[+] PESAN: {message[:50]}...")
    print(f"{Fore.GREEN}[+] JUMLAH: {count}")
    print(f"{Fore.GREEN}[+] DELAY: {delay}s")
    print(f"{Fore.CYAN}" + "═" * 60 + "\n")
    success_count = 0
    fail_count = 0
    for i in range(1, count + 1):
        try:
            status, result = send_ngl_message(username, message)
            progress = (i / count) * 100
            bar_length = 30
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            if status:
                success_count += 1
                print(f"{Fore.GREEN}[{i}/{count}] ✅ {result} [{Fore.CYAN}{bar}{Fore.GREEN}] {progress:.1f}%")
            else:
                fail_count += 1
                print(f"{Fore.RED}[{i}/{count}] {result} [{Fore.CYAN}{bar}{Fore.RED}] {progress:.1f}%")
            if i < count:
                time.sleep(delay)
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}\n[!] Spam dihentikan!")
            break
        except Exception as e:
            print(f"{Fore.RED}[{i}/{count}] ❌ Error: {str(e)[:50]}")
            fail_count += 1
            time.sleep(1)
    print(f"{Fore.CYAN}\n" + "═" * 60)
    print(f"{Fore.CYAN}📊 HASIL SPAM:")
    print(f"{Fore.GREEN}✅ Berhasil: {success_count}")
    print(f"{Fore.RED}❌ Gagal: {fail_count}")
    print(f"{Fore.YELLOW}📦 Total: {success_count + fail_count}")
    print(f"{Fore.CYAN}" + "═" * 60)
    if success_count > 0:
        print(f"{Fore.GREEN}🔥 SPAM BERHASIL!")
    else:
        print(f"{Fore.RED}💀 GAGAL SEMUA! CEK USERNAME!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 TOOLS EGAA 🔥
# ============================================

def tools_egaa():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}👑 TOOLS EGAA {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}👥 Manage User {Fore.GREEN}[5] {Fore.WHITE}📊 Log Aktivitas {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}🔑 Create Password {Fore.GREEN}[6] {Fore.WHITE}📊 Statistik User {Fore.CYAN}│
│ {Fore.GREEN}[3] {Fore.WHITE}📋 List User {Fore.GREEN}[7] {Fore.WHITE}🔙 Back {Fore.CYAN}│
│ {Fore.GREEN}[4] {Fore.WHITE}🗑️ Delete User {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}""")
        choice = input(f"{Fore.CYAN}Pilih [1-7]: {Fore.WHITE}").strip()
        if choice == '1':
            show_banner()
            print(f"{Fore.CYAN}👥 MANAGE USER")
            print(f"{Fore.GREEN}[1] {Fore.WHITE}Create Password")
            print(f"{Fore.GREEN}[2] {Fore.WHITE}List User")
            print(f"{Fore.GREEN}[3] {Fore.WHITE}Delete User")
            sub_choice = input(f"{Fore.CYAN}Pilih: ").strip()
            if sub_choice == '1':
                create_user_password()
            elif sub_choice == '2':
                list_users()
                input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
            elif sub_choice == '3':
                delete_user()
            else:
                print(f"{Fore.RED}❌ Pilihan tidak valid!")
                time.sleep(1)
        elif choice == '2':
            create_user_password()
        elif choice == '3':
            list_users()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
        elif choice == '4':
            delete_user()
        elif choice == '5':
            view_logs()
        elif choice == '6':
            user_stats()
        elif choice == '7':
            print(f"{Fore.YELLOW}🔙 Kembali...")
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

def create_user_password():
    show_banner()
    print(f"{Fore.CYAN}🔑 CREATE PASSWORD")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    print(f"{Fore.YELLOW}Durasi:")
    print(f" {Fore.WHITE}[1] 24 Jam")
    print(f" {Fore.WHITE}[2] 2 Hari")
    print(f" {Fore.WHITE}[3] 7 Hari")
    print(f" {Fore.WHITE}[4] PERMANEN")
    durasi_choice = input(f"{Fore.CYAN}Pilih [1-4]: ").strip()
    if durasi_choice == '1': hours = 24
    elif durasi_choice == '2': hours = 48
    elif durasi_choice == '3': hours = 168
    elif durasi_choice == '4': hours = 0
    else:
        print(f"{Fore.RED}❌ Pilihan tidak valid! Default: 24 jam")
        hours = 24
    print(f"{Fore.YELLOW}Pilih Role:")
    print(f" {Fore.WHITE}[1] ADMIN")
    print(f" {Fore.WHITE}[2] MEMBER")
    role_choice = input(f"{Fore.CYAN}Pilih [1-2]: ").strip()
    role = 'ADMIN' if role_choice == '1' else 'MEMBER'
    result, msg = create_password(username, hours, role)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    print(f"{Fore.YELLOW}\n📌 SIMPAN PASSWORD INI!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def list_users():
    show_banner()
    print(f"{Fore.CYAN}📋 DAFTAR USER")
    data = load_data()
    if not data:
        print(f"{Fore.YELLOW}⚠️ Belum ada user terdaftar.")
        return
    print(f"{Fore.CYAN}" + "═" * 50)
    for username, info in data.items():
        expired = datetime.fromisoformat(info['expired'])
        status = f"{Fore.GREEN}AKTIF" if expired > datetime.now() else f"{Fore.RED}EXPIRED"
        role = info.get('role', 'MEMBER')
        durasi = info.get('duration', 'Unknown')
        print(f"{Fore.YELLOW}• {username} {status} {Fore.WHITE}({durasi}) {Fore.CYAN}[{role}]")

def delete_user():
    show_banner()
    print(f"{Fore.CYAN}🗑️ DELETE USER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    data = load_data()
    if username in data:
        del data[username]
        save_data(data)
        log_activity(f"User dihapus: {username}")
        print(f"{Fore.GREEN}✅ User {username} berhasil dihapus!")
    else:
        print(f"{Fore.RED}❌ User tidak ditemukan!")
    time.sleep(1)

def view_logs():
    show_banner()
    print(f"{Fore.CYAN}📊 LOG AKTIVITAS")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = f.readlines()
        if logs:
            for log in logs[-20:]:
                print(f"{Fore.WHITE}{log.strip()}")
        else:
            print(f"{Fore.YELLOW}⚠️ Belum ada log.")
    else:
        print(f"{Fore.YELLOW}⚠️ Belum ada log.")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def user_stats():
    show_banner()
    print(f"{Fore.CYAN}📈 STATISTIK USER")
    data = load_data()
    total = len(data)
    aktif = 0
    expired = 0
    member = 0
    admin = 0
    for info in data.values():
        if datetime.fromisoformat(info['expired']) > datetime.now():
            aktif += 1
        else:
            expired += 1
        role = info.get('role', 'MEMBER')
        if role == 'MEMBER':
            member += 1
        elif role == 'ADMIN':
            admin += 1
    print(f"{Fore.GREEN}📌 Statistik:")
    print(f"{Fore.WHITE} • Total User : {total}")
    print(f"{Fore.WHITE} • User Aktif : {Fore.GREEN}{aktif}")
    print(f"{Fore.WHITE} • User Expired: {Fore.RED}{expired}")
    print(f"{Fore.WHITE} • ADMIN : {Fore.CYAN}{admin}")
    print(f"{Fore.WHITE} • MEMBER : {Fore.GREEN}{member}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 LOGIN 🔥
# ============================================

def login():
    show_banner()
    print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}🔐 LOGIN - PREMIUM EDITION {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
Username: {Fore.GREEN}egaa{Fore.WHITE}
Password: {Fore.GREEN}9999{Fore.WHITE}
""")
    username = input(f"{Fore.CYAN}Username: {Fore.WHITE}").strip()
    password = input(f"{Fore.CYAN}Password: {Fore.WHITE}").strip()
    if not username or not password:
        print(f"{Fore.RED}❌ Username dan password tidak boleh kosong!")
        time.sleep(1)
        return False
    status, msg = verify_password(username, password)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    time.sleep(1)
    return status

# ============================================
# 🔥 MAIN MENU 🔥
# ============================================

def main():
    if not login():
        print(f"{Fore.RED}\n❌ Login gagal! Hubungi {TELEGRAM}")
        time.sleep(2)
        return
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}📌 MAIN MENU - PREMIUM EDITION {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}📨 SPAM NGL {Fore.GREEN}[3] {Fore.WHITE}🌍 PUBLIC TOOLS {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}👑 TOOLS EGAA {Fore.GREEN}[4] {Fore.WHITE}🚪 EXIT {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}""")
        choice = input(f"{Fore.CYAN}Pilih [1-4]: {Fore.WHITE}").strip()
        if choice == '1':
            spam_ngl()
        elif choice == '2':
            tools_egaa()
        elif choice == '3':
            public_tools()
        elif choice == '4':
            print(f"{Fore.GREEN}👋 Keluar dari ALEGRA SPAM...")
            sys.exit(0)
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}\n[!] Keluar...")
    finally:
        print(f"{Fore.CYAN}\n📨 ALEGRA SPAM - PREMIUM EDITION")
        print(f"{Fore.MAGENTA}Script By : {AUTHOR}")
        print(f"{Fore.WHITE}Telegram : {TELEGRAM}")
