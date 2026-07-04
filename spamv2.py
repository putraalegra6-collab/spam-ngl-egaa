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
from datetime import datetime, timedelta
from colorama import init, Fore, Style, Back

init(autoreset=True)
os.system("clear" if os.name == "posix" else "cls")

# ============================================
# 🔥 KONFIGURASI 🔥
# ============================================

VERSION = "VVIP FINAL 6.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"
OWNER_PASSWORD = "alegra ega"
DATA_FILE = os.path.expanduser("~/.alegra_vvip_final_data.json")
LOG_FILE = os.path.expanduser("~/.alegra_final_log.txt")

# ============================================
# 🔥 FUNGSI CUACA & WAKTU 🔥
# ============================================

def get_weather():
    try:
        response = requests.get('https://wttr.in/Indonesia?format=%C+%t', timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        return "Tidak tersedia"
    except:
        return "Tidak tersedia"

def get_datetime():
    now = datetime.now()
    hari = now.strftime('%A')
    tanggal = now.strftime('%d %B %Y')
    jam = now.strftime('%H:%M:%S')
    return hari, tanggal, jam

# ============================================
# 🔥 BANNER ABU-ABU + JAM & CUACA 🔥
# ============================================

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    
    hari, tanggal, jam = get_datetime()
    cuaca = get_weather()
    
    # ── BANNER UTAMA ──
    print(f"{Fore.WHITE}╔══════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.WHITE}║                                                                                      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}   █████╗ ██╗     ███████╗ ██████╗ ██████╗  █████╗     ███╗   ██╗ ██████╗ ██╗     ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ██╔══██╗██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗    ████╗  ██║██╔═══██╗██║     ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ███████║██║     █████╗  ██║  ███╗██████╔╝███████║    ██╔██╗ ██║██║   ██║██║     ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ██╔══██║██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║    ██║╚██╗██║██║   ██║██║     ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ██║  ██║███████╗███████╗╚██████╔╝██║  ██║██║  ██║    ██║ ╚████║╚██████╔╝███████╗║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝║")
    print(f"{Fore.WHITE}║                                                                                      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ███████╗██████╗  █████╗ ███╗   ███╗                                    ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ██╔════╝██╔══██╗██╔══██╗████╗ ████║                                    ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ███████╗██████╔╝███████║██╔████╔██║                                    ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║                                    ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ███████║██║     ██║  ██║██║ ╚═╝ ██║                                    ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                                    ║")
    print(f"{Fore.WHITE}║                                                                                      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ╔══════════════════════════════════════════════════════════════════════╗ ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ║  {Fore.WHITE}📨 ALEGRA NGL SPAM - {Fore.WHITE}{VERSION}{Fore.WHITE} 📨          ║ ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ║  {Fore.WHITE}Script By : {AUTHOR}                                     ║ ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ║  {Fore.WHITE}Telegram : {TELEGRAM}                                       ║ ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ║  {Fore.WHITE}🔥 VVIP FINAL EDITION 🔥                                  ║ ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}  ╚══════════════════════════════════════════════════════════════════════╝ ║")
    print(f"{Fore.WHITE}║                                                                                      ║")
    
    # ── JAM DI KIRI & CUACA DI KANAN ──
    print(f"{Fore.WHITE}║  {Fore.WHITE}┌─────────────────────┐    {Fore.WHITE}┌─────────────────────────┐      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}│  {Fore.WHITE}⏰ {hari:<18} │    {Fore.WHITE}│  {Fore.WHITE}🌤️ {cuaca:<18} │      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}│  {Fore.WHITE}📅 {tanggal:<18} │    {Fore.WHITE}│  {Fore.WHITE}📍 Indonesia           │      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}│  {Fore.WHITE}🕐 {jam:<18} │    {Fore.WHITE}│  {Fore.WHITE}💨 Perkiraan Cuaca     │      ║")
    print(f"{Fore.WHITE}║  {Fore.WHITE}└─────────────────────┘    {Fore.WHITE}└─────────────────────────┘      ║")
    print(f"{Fore.WHITE}║                                                                                      ║")
    print(f"{Fore.WHITE}╚══════════════════════════════════════════════════════════════════════════════════════╝")
    print()

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

def create_password(username, duration_hours):
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
        'duration': durasi_text
    }
    
    save_data(data)
    log_activity(f"Create password untuk {username} ({durasi_text})")
    return password, f"✅ Password dibuat: {password}\n   Expired: {durasi_text}"

def verify_password(username, password):
    data = load_data()
    
    if username not in data:
        return False, "❌ Username tidak terdaftar!"
    
    user_data = data[username]
    expired = datetime.fromisoformat(user_data['expired'])
    
    if expired < datetime.now():
        return False, "❌ Password sudah expired!"
    
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if hashed == user_data['password']:
        log_activity(f"Login berhasil: {username}")
        return True, "✅ Login berhasil!"
    else:
        return False, "❌ Password salah!"

def list_users():
    data = load_data()
    if not data:
        print(f"{Fore.WHITE}⚠️ Belum ada user terdaftar.")
        return
    
    print(f"\n{Fore.WHITE}📋 DAFTAR USER:")
    print(f"{Fore.WHITE}=" * 50)
    for username, info in data.items():
        expired = datetime.fromisoformat(info['expired'])
        status = f"{Fore.WHITE}AKTIF" if expired > datetime.now() else f"{Fore.WHITE}EXPIRED"
        durasi = info.get('duration', 'Unknown')
        print(f"{Fore.WHITE}• {username} {status} {Fore.WHITE}({durasi})")

# ============================================
# 🔥 PUBLIC TOOLS (25 TOOLS) 🔥
# ============================================

def public_tools():
    while True:
        show_banner()
        print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}🌍 PUBLIC TOOLS - 25 TOOLS  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}[1]  🌐 Cek Website Online/Offline
{Fore.WHITE}[2]  🔍 IP Lookup
{Fore.WHITE}[3]  📡 Ping Test
{Fore.WHITE}[4]  🌐 DNS Lookup
{Fore.WHITE}[5]  🎭 Random User-Agent
{Fore.WHITE}[6]  🔐 Base64 Encode/Decode
{Fore.WHITE}[7]  📊 Cek Informasi Sistem
{Fore.WHITE}[8]  📱 Cek Info HP
{Fore.WHITE}[9]  🌍 Cek IP Publik
{Fore.WHITE}[10] ⏰ Cek Waktu & Tanggal
{Fore.WHITE}[11] 📁 Cek Storage HP
{Fore.WHITE}[12] 🔋 Cek Baterai HP
{Fore.WHITE}[13] 📶 Cek Signal/WiFi
{Fore.WHITE}[14] 🧮 Kalkulator Sederhana
{Fore.WHITE}[15] 📝 Random Password Generator
{Fore.WHITE}[16] 🔢 Random Number Generator
{Fore.WHITE}[17] 📊 Cek RAM Usage
{Fore.WHITE}[18] 💻 Cek CPU Usage
{Fore.WHITE}[19] 📂 Cek Folder Size
{Fore.WHITE}[20] 🌐 Cek Domain Age
{Fore.WHITE}[21] 🔍 Cek Port Scanning
{Fore.WHITE}[22] 📧 Email Validator
{Fore.WHITE}[23] 🔗 URL Shortener
{Fore.WHITE}[24] 📝 Text to Binary
{Fore.WHITE}[25] 🔙 Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.WHITE}Pilih [1-25]: {Fore.WHITE}").strip()
        
        if choice == '1':
            check_website()
        elif choice == '2':
            ip_lookup()
        elif choice == '3':
            ping_tool()
        elif choice == '4':
            dns_lookup()
        elif choice == '5':
            user_agent_gen()
        elif choice == '6':
            base64_tool()
        elif choice == '7':
            system_info()
        elif choice == '8':
            device_info()
        elif choice == '9':
            public_ip()
        elif choice == '10':
            show_datetime()
        elif choice == '11':
            check_storage()
        elif choice == '12':
            check_battery()
        elif choice == '13':
            check_signal()
        elif choice == '14':
            calculator()
        elif choice == '15':
            random_password()
        elif choice == '16':
            random_number()
        elif choice == '17':
            check_ram()
        elif choice == '18':
            check_cpu()
        elif choice == '19':
            check_folder_size()
        elif choice == '20':
            check_domain_age()
        elif choice == '21':
            port_scan()
        elif choice == '22':
            email_validator()
        elif choice == '23':
            url_shortener()
        elif choice == '24':
            text_to_binary()
        elif choice == '25':
            break
        else:
            print(f"{Fore.WHITE}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 PUBLIC TOOLS - FUNGSI TAMBAHAN 🔥
# ============================================

def check_storage():
    show_banner()
    print(f"{Fore.WHITE}📁 CEK STORAGE HP")
    try:
        import subprocess
        result = subprocess.getoutput("df -h /data")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal mendapatkan info storage!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_battery():
    show_banner()
    print(f"{Fore.WHITE}🔋 CEK BATERAI HP")
    try:
        result = subprocess.getoutput("termux-battery-status")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal mendapatkan info baterai! (butuh termux-api)")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_signal():
    show_banner()
    print(f"{Fore.WHITE}📶 CEK SIGNAL/WIFI")
    try:
        result = subprocess.getoutput("termux-wifi-connectioninfo")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal mendapatkan info signal! (butuh termux-api)")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def calculator():
    show_banner()
    print(f"{Fore.WHITE}🧮 KALKULATOR SEDERHANA")
    try:
        expr = input(f"{Fore.WHITE}Masukkan operasi (contoh: 2+3): ")
        result = eval(expr)
        print(f"{Fore.WHITE}Hasil: {result}")
    except:
        print(f"{Fore.WHITE}❌ Error! Masukkan operasi yang benar.")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def random_password():
    show_banner()
    print(f"{Fore.WHITE}📝 RANDOM PASSWORD GENERATOR")
    try:
        length = int(input(f"{Fore.WHITE}Panjang password: ") or 12)
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=length))
        print(f"{Fore.WHITE}Password: {password}")
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def random_number():
    show_banner()
    print(f"{Fore.WHITE}🔢 RANDOM NUMBER GENERATOR")
    try:
        min_num = int(input(f"{Fore.WHITE}Min: ") or 1)
        max_num = int(input(f"{Fore.WHITE}Max: ") or 100)
        print(f"{Fore.WHITE}Random: {random.randint(min_num, max_num)}")
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_ram():
    show_banner()
    print(f"{Fore.WHITE}📊 CEK RAM USAGE")
    try:
        import subprocess
        result = subprocess.getoutput("free -h")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal mendapatkan info RAM!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_cpu():
    show_banner()
    print(f"{Fore.WHITE}💻 CEK CPU USAGE")
    try:
        result = subprocess.getoutput("top -bn1 | head -10")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal mendapatkan info CPU!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_folder_size():
    show_banner()
    print(f"{Fore.WHITE}📂 CEK FOLDER SIZE")
    folder = input(f"{Fore.WHITE}Masukkan path folder: ")
    try:
        import subprocess
        result = subprocess.getoutput(f"du -sh {folder} 2>/dev/null")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.WHITE}❌ Gagal!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def check_domain_age():
    show_banner()
    print(f"{Fore.WHITE}🌐 CEK DOMAIN AGE")
    domain = input(f"{Fore.WHITE}Masukkan domain: ")
    try:
        import whois
        w = whois.whois(domain)
        print(f"{Fore.WHITE}Domain: {domain}")
        print(f"{Fore.WHITE}Created: {w.creation_date}")
    except:
        print(f"{Fore.WHITE}❌ Gagal! (butuh python-whois)")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def port_scan():
    show_banner()
    print(f"{Fore.WHITE}🔍 CEK PORT SCANNING")
    ip = input(f"{Fore.WHITE}Masukkan IP: ")
    ports = input(f"{Fore.WHITE}Port (pisah koma): ")
    try:
        for port in ports.split(','):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, int(port)))
            if result == 0:
                print(f"{Fore.WHITE}Port {port} TERBUKA")
            else:
                print(f"{Fore.WHITE}Port {port} TERTUTUP")
            sock.close()
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def email_validator():
    show_banner()
    print(f"{Fore.WHITE}📧 EMAIL VALIDATOR")
    email = input(f"{Fore.WHITE}Masukkan email: ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{Fore.WHITE}✅ Email VALID")
    else:
        print(f"{Fore.WHITE}❌ Email INVALID")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def url_shortener():
    show_banner()
    print(f"{Fore.WHITE}🔗 URL SHORTENER")
    url = input(f"{Fore.WHITE}Masukkan URL: ")
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            print(f"{Fore.WHITE}Short URL: {response.text}")
        else:
            print(f"{Fore.WHITE}❌ Gagal!")
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def text_to_binary():
    show_banner()
    print(f"{Fore.WHITE}📝 TEXT TO BINARY")
    text = input(f"{Fore.WHITE}Masukkan teks: ")
    binary = ' '.join(format(ord(c), '08b') for c in text)
    print(f"{Fore.WHITE}Binary: {binary}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

# ============================================
# 🔥 PUBLIC TOOLS - FUNGSI DASAR 🔥
# ============================================

def check_website():
    show_banner()
    print(f"{Fore.WHITE}🌐 CEK WEBSITE ONLINE/OFFLINE")
    url = input(f"{Fore.WHITE}URL: ").strip()
    if not url:
        print(f"{Fore.WHITE}❌ URL tidak boleh kosong!")
        time.sleep(1)
        return
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{Fore.WHITE}✅ ONLINE! (Status: {response.status_code})")
        else:
            print(f"{Fore.WHITE}⚠️ RESPOND (Status: {response.status_code})")
    except:
        print(f"{Fore.WHITE}❌ OFFLINE / TIDAK TERJANGKAU!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def ip_lookup():
    show_banner()
    print(f"{Fore.WHITE}🔍 IP LOOKUP")
    ip = input(f"{Fore.WHITE}IP: ").strip()
    if not ip:
        print(f"{Fore.WHITE}❌ IP tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        data = response.json()
        if data['status'] == 'success':
            print(f"{Fore.WHITE}📌 INFO IP {ip}:")
            print(f"{Fore.WHITE}  • Negara  : {data.get('country', '-')}")
            print(f"{Fore.WHITE}  • Kota    : {data.get('city', '-')}")
            print(f"{Fore.WHITE}  • ISP     : {data.get('isp', '-')}")
            print(f"{Fore.WHITE}  • Region  : {data.get('regionName', '-')}")
            print(f"{Fore.WHITE}  • Timezone: {data.get('timezone', '-')}")
        else:
            print(f"{Fore.WHITE}❌ Gagal!")
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def ping_tool():
    show_banner()
    print(f"{Fore.WHITE}📡 PING TEST")
    target = input(f"{Fore.WHITE}IP / Domain: ").strip()
    if not target:
        print(f"{Fore.WHITE}❌ Target tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        os.system(f"ping -c 4 {target}")
    except:
        print(f"{Fore.WHITE}❌ Gagal!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def dns_lookup():
    show_banner()
    print(f"{Fore.WHITE}🌐 DNS LOOKUP")
    domain = input(f"{Fore.WHITE}Domain: ").strip()
    if not domain:
        print(f"{Fore.WHITE}❌ Domain tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.WHITE}✅ {domain} → {ip}")
    except:
        print(f"{Fore.WHITE}❌ Gagal!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def user_agent_gen():
    show_banner()
    print(f"{Fore.WHITE}🎭 RANDOM USER-AGENT")
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/20100101 Firefox/119.0",
    ]
    print(f"{Fore.WHITE}📌 Random User-Agent:")
    print(f"{Fore.WHITE}{random.choice(agents)}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def base64_tool():
    show_banner()
    print(f"{Fore.WHITE}🔐 BASE64 ENCODE/DECODE")
    print(f"{Fore.WHITE}[1] Encode")
    print(f"{Fore.WHITE}[2] Decode")
    choice = input(f"{Fore.WHITE}Pilih: ").strip()
    text = input(f"{Fore.WHITE}Teks: ").strip()
    if not text:
        print(f"{Fore.WHITE}❌ Teks tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        import base64
        if choice == '1':
            result = base64.b64encode(text.encode()).decode()
            print(f"{Fore.WHITE}✅ Hasil Encode: {Fore.WHITE}{result}")
        elif choice == '2':
            result = base64.b64decode(text).decode()
            print(f"{Fore.WHITE}✅ Hasil Decode: {Fore.WHITE}{result}")
        else:
            print(f"{Fore.WHITE}❌ Pilihan tidak valid!")
    except:
        print(f"{Fore.WHITE}❌ Error!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def system_info():
    show_banner()
    print(f"{Fore.WHITE}📊 INFO SISTEM")
    print(f"{Fore.WHITE}  • OS      : {platform.system()} {platform.release()}")
    print(f"{Fore.WHITE}  • Hostname: {platform.node()}")
    print(f"{Fore.WHITE}  • Python  : {platform.python_version()}")
    print(f"{Fore.WHITE}  • Arch    : {platform.machine()}")
    print(f"{Fore.WHITE}  • CPU     : {platform.processor() or 'Unknown'}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def device_info():
    show_banner()
    print(f"{Fore.WHITE}📱 INFO HP")
    try:
        model = subprocess.getoutput("getprop ro.product.model")
        brand = subprocess.getoutput("getprop ro.product.brand")
        android = subprocess.getoutput("getprop ro.build.version.release")
        print(f"{Fore.WHITE}  • Model   : {model}")
        print(f"{Fore.WHITE}  • Brand   : {brand}")
        print(f"{Fore.WHITE}  • Android : {android}")
    except:
        print(f"{Fore.WHITE}  • Info HP : Tidak tersedia")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def public_ip():
    show_banner()
    print(f"{Fore.WHITE}🌍 CEK IP PUBLIK")
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"{Fore.WHITE}✅ IP Publik: {Fore.WHITE}{ip}")
    except:
        print(f"{Fore.WHITE}❌ Gagal!")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def show_datetime():
    show_banner()
    print(f"{Fore.WHITE}⏰ WAKTU & TANGGAL")
    now = datetime.now()
    print(f"{Fore.WHITE}  • Tanggal : {now.strftime('%d %B %Y')}")
    print(f"{Fore.WHITE}  • Hari    : {now.strftime('%A')}")
    print(f"{Fore.WHITE}  • Waktu   : {now.strftime('%H:%M:%S')}")
    print(f"{Fore.WHITE}  • Timezone: {time.tzname[0]}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

# ============================================
# 🔥 FUNGSI SPAM NGL 🔥
# ============================================

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/20100101 Firefox/115.0",
]

DEVICE_IDS = [
    "android-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
    "ios-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
    "web-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)),
    "desktop-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
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
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Connection": "keep-alive"
    }

def extract_username(input_text):
    input_text = input_text.strip()
    
    link_pattern = r'https?://ngl\.link/([a-zA-Z0-9_]+)'
    match = re.search(link_pattern, input_text)
    if match:
        return match.group(1)
    
    link_pattern2 = r'https?://www\.ngl\.link/([a-zA-Z0-9_]+)'
    match2 = re.search(link_pattern2, input_text)
    if match2:
        return match2.group(1)
    
    link_pattern3 = r'ngl\.link/([a-zA-Z0-9_]+)'
    match3 = re.search(link_pattern3, input_text)
    if match3:
        return match3.group(1)
    
    if input_text.startswith('@'):
        input_text = input_text[1:]
    
    username = re.sub(r'[^a-zA-Z0-9_]', '', input_text)
    
    if username:
        return username
    
    return None

def send_ngl_message(username, message, retry=0):
    try:
        device_id = random.choice(DEVICE_IDS)
        url = "https://ngl.link/api/submit"
        payload = {
            "username": username.strip().replace("@", ""),
            "question": message,
            "deviceId": device_id
        }
        headers = random_headers()
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get("status") == "success" or data.get("message") == "Question sent successfully":
                    return True, "✅ BERHASIL!"
                else:
                    return False, f"❌ GAGAL: {data.get('message', 'Unknown error')}"
            except:
                return True, "✅ BERHASIL!"
        elif response.status_code == 429:
            time.sleep(2)
            if retry < 3:
                return send_ngl_message(username, message, retry + 1)
            return False, "⏳ RATE LIMIT!"
        elif response.status_code == 400:
            return False, "❌ USERNAME SALAH!"
        elif response.status_code == 404:
            return False, "❌ USERNAME TIDAK DITEMUKAN!"
        else:
            return False, f"❌ ERROR {response.status_code}"
            
    except requests.exceptions.Timeout:
        if retry < 3:
            time.sleep(2)
            return send_ngl_message(username, message, retry + 1)
        return False, "❌ TIMEOUT!"
    except requests.exceptions.ConnectionError:
        if retry < 3:
            time.sleep(2)
            return send_ngl_message(username, message, retry + 1)
        return False, "❌ CONNECTION ERROR!"
    except Exception as e:
        if retry < 3:
            time.sleep(2)
            return send_ngl_message(username, message, retry + 1)
        return False, f"❌ ERROR: {str(e)[:30]}"

# ============================================
# 🔥 TOOLS OWNER (15 TOOLS) 🔥
# ============================================

def tools_owner():
    while True:
        show_banner()
        print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}👑 TOOLS OWNER - 15 TOOLS  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}[1]  👥 Manage User (Create/List/Delete)
{Fore.WHITE}[2]  📊 Lihat Log Aktivitas
{Fore.WHITE}[3]  🔑 Ganti Password User
{Fore.WHITE}[4]  📋 Backup Data User
{Fore.WHITE}[5]  🗑️  Reset Semua Data
{Fore.WHITE}[6]  📈 Statistik User
{Fore.WHITE}[7]  👑 Tambah Owner Baru
{Fore.WHITE}[8]  📋 Lihat Daftar Owner
{Fore.WHITE}[9]  🗑️  Hapus Owner
{Fore.WHITE}[10] 🔄 Ganti Password Owner
{Fore.WHITE}[11] 📊 Log Aktivitas Owner
{Fore.WHITE}[12] 🔒 Lock Tools
{Fore.WHITE}[13] 🔓 Unlock Tools
{Fore.WHITE}[14] 📋 Cek Status Tools
{Fore.WHITE}[15] 🔙 Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.WHITE}Pilih [1-15]: {Fore.WHITE}").strip()
        
        if choice == '1':
            owner_manage_user()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            change_user_password()
        elif choice == '4':
            backup_data()
        elif choice == '5':
            reset_all_data()
        elif choice == '6':
            user_stats()
        elif choice == '7':
            add_owner()
        elif choice == '8':
            list_owners()
        elif choice == '9':
            remove_owner()
        elif choice == '10':
            change_owner_password()
        elif choice == '11':
            owner_logs()
        elif choice == '12':
            lock_tools()
        elif choice == '13':
            unlock_tools()
        elif choice == '14':
            check_tools_status()
        elif choice == '15':
            break
        else:
            print(f"{Fore.WHITE}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 TOOLS OWNER - FUNGSI TAMBAHAN 🔥
# ============================================

OWNER_FILE = os.path.expanduser("~/.alegra_owners.json")

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

def add_owner():
    show_banner()
    print(f"{Fore.WHITE}👑 TAMBAH OWNER BARU")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.WHITE}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    password = input(f"{Fore.WHITE}Password: ").strip()
    if not password:
        print(f"{Fore.WHITE}❌ Password tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username in owners:
        print(f"{Fore.WHITE}❌ Username sudah menjadi owner!")
        time.sleep(1)
        return
    owners[username] = {
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'created': datetime.now().isoformat()
    }
    save_owners(owners)
    log_activity(f"Owner baru: {username}")
    print(f"{Fore.WHITE}✅ Owner {username} berhasil ditambahkan!")
    time.sleep(1)

def list_owners():
    show_banner()
    print(f"{Fore.WHITE}📋 DAFTAR OWNER")
    owners = load_owners()
    if not owners:
        print(f"{Fore.WHITE}⚠️ Belum ada owner terdaftar.")
    else:
        for username, info in owners.items():
            created = datetime.fromisoformat(info['created']).strftime('%d-%m-%Y %H:%M')
            print(f"{Fore.WHITE}• {username} (created: {created})")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def remove_owner():
    show_banner()
    print(f"{Fore.WHITE}🗑️  HAPUS OWNER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.WHITE}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username not in owners:
        print(f"{Fore.WHITE}❌ Username tidak ditemukan!")
        time.sleep(1)
        return
    del owners[username]
    save_owners(owners)
    log_activity(f"Owner dihapus: {username}")
    print(f"{Fore.WHITE}✅ Owner {username} berhasil dihapus!")
    time.sleep(1)

def change_owner_password():
    show_banner()
    print(f"{Fore.WHITE}🔄 GANTI PASSWORD OWNER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.WHITE}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username not in owners:
        print(f"{Fore.WHITE}❌ Username tidak ditemukan!")
        time.sleep(1)
        return
    new_pass = input(f"{Fore.WHITE}Password baru: ").strip()
    if not new_pass:
        print(f"{Fore.WHITE}❌ Password tidak boleh kosong!")
        time.sleep(1)
        return
    owners[username]['password'] = hashlib.sha256(new_pass.encode()).hexdigest()
    save_owners(owners)
    log_activity(f"Password owner diubah: {username}")
    print(f"{Fore.WHITE}✅ Password owner {username} berhasil diubah!")
    time.sleep(1)

def owner_logs():
    show_banner()
    print(f"{Fore.WHITE}📊 LOG AKTIVITAS OWNER")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = f.readlines()
            if logs:
                for log in logs[-20:]:
                    print(f"{Fore.WHITE}{log.strip()}")
            else:
                print(f"{Fore.WHITE}⚠️ Belum ada log.")
    else:
        print(f"{Fore.WHITE}⚠️ Belum ada log.")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def lock_tools():
    show_banner()
    print(f"{Fore.WHITE}🔒 LOCK TOOLS")
    confirm = input(f"{Fore.WHITE}Yakin lock tools? (y/n): ").strip().lower()
    if confirm == 'y':
        with open(os.path.expanduser("~/.alegra_locked"), 'w') as f:
            f.write("locked")
        log_activity("Tools di-lock")
        print(f"{Fore.WHITE}✅ Tools berhasil di-lock!")
    else:
        print(f"{Fore.WHITE}⚠️ Dibatalkan.")
    time.sleep(1)

def unlock_tools():
    show_banner()
    print(f"{Fore.WHITE}🔓 UNLOCK TOOLS")
    confirm = input(f"{Fore.WHITE}Yakin unlock tools? (y/n): ").strip().lower()
    if confirm == 'y':
        os.remove(os.path.expanduser("~/.alegra_locked"))
        log_activity("Tools di-unlock")
        print(f"{Fore.WHITE}✅ Tools berhasil di-unlock!")
    else:
        print(f"{Fore.WHITE}⚠️ Dibatalkan.")
    time.sleep(1)

def check_tools_status():
    show_banner()
    print(f"{Fore.WHITE}📋 CEK STATUS TOOLS")
    if os.path.exists(os.path.expanduser("~/.alegra_locked")):
        print(f"{Fore.WHITE}🔒 Status: LOCKED")
    else:
        print(f"{Fore.WHITE}🔓 Status: UNLOCKED")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def owner_manage_user():
    while True:
        show_banner()
        print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}👥 MANAGE USER  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}[1] Create Password
{Fore.WHITE}[2] List User
{Fore.WHITE}[3] Delete User
{Fore.WHITE}[4] Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.WHITE}Pilih: {Fore.WHITE}").strip()
        
        if choice == '1':
            username = input(f"{Fore.WHITE}Username: ").strip()
            if not username:
                print(f"{Fore.WHITE}❌ Username tidak boleh kosong!")
                time.sleep(1)
                continue
            
            print(f"{Fore.WHITE}Durasi:")
            print(f"  {Fore.WHITE}[1] 24 Jam")
            print(f"  {Fore.WHITE}[2] 2 Hari")
            print(f"  {Fore.WHITE}[3] 7 Hari")
            print(f"  {Fore.WHITE}[4] PERMANEN")
            durasi_choice = input(f"{Fore.WHITE}Pilih durasi [1-4]: ").strip()
            
            if durasi_choice == '1':
                hours = 24
            elif durasi_choice == '2':
                hours = 48
            elif durasi_choice == '3':
                hours = 168
            elif durasi_choice == '4':
                hours = 0
            else:
                print(f"{Fore.WHITE}❌ Pilihan tidak valid! Menggunakan default: 24 jam")
                hours = 24
            
            result, msg = create_password(username, hours)
            print(f"{Fore.WHITE}{msg}")
            time.sleep(2)
            
        elif choice == '2':
            list_users()
            input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")
            
        elif choice == '3':
            username = input(f"{Fore.WHITE}Username yang akan dihapus: ").strip()
            if username:
                data = load_data()
                if username in data:
                    del data[username]
                    save_data(data)
                    log_activity(f"User dihapus: {username}")
                    print(f"{Fore.WHITE}✅ User {username} berhasil dihapus!")
                else:
                    print(f"{Fore.WHITE}❌ User tidak ditemukan!")
                time.sleep(1)
            
        elif choice == '4':
            break
        else:
            print(f"{Fore.WHITE}❌ Pilihan tidak valid!")
            time.sleep(1)

def view_logs():
    show_banner()
    print(f"{Fore.WHITE}📊 LOG AKTIVITAS")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = f.readlines()
            if logs:
                for log in logs[-20:]:
                    print(f"{Fore.WHITE}{log.strip()}")
            else:
                print(f"{Fore.WHITE}⚠️ Belum ada log.")
    else:
        print(f"{Fore.WHITE}⚠️ Belum ada log.")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def change_user_password():
    show_banner()
    print(f"{Fore.WHITE}🔑 GANTI PASSWORD USER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.WHITE}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    data = load_data()
    if username not in data:
        print(f"{Fore.WHITE}❌ User tidak ditemukan!")
        time.sleep(1)
        return
    new_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    data[username]['password'] = hashlib.sha256(new_pass.encode()).hexdigest()
    save_data(data)
    log_activity(f"Password diubah untuk: {username}")
    print(f"{Fore.WHITE}✅ Password baru untuk {username}: {Fore.WHITE}{new_pass}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def backup_data():
    show_banner()
    print(f"{Fore.WHITE}📋 BACKUP DATA USER")
    data = load_data()
    if not data:
        print(f"{Fore.WHITE}⚠️ Tidak ada data untuk di-backup.")
        time.sleep(1)
        return
    backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    log_activity(f"Backup data: {backup_file}")
    print(f"{Fore.WHITE}✅ Backup berhasil! File: {backup_file}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

def reset_all_data():
    show_banner()
    print(f"{Fore.WHITE}🗑️  RESET SEMUA DATA")
    confirm = input(f"{Fore.WHITE}⚠️ Yakin ingin menghapus semua data? (y/n): ").strip().lower()
    if confirm == 'y':
        save_data({})
        log_activity("Semua data direset")
        print(f"{Fore.WHITE}✅ Semua data berhasil direset!")
    else:
        print(f"{Fore.WHITE}⚠️ Dibatalkan.")
    time.sleep(1)

def user_stats():
    show_banner()
    print(f"{Fore.WHITE}📈 STATISTIK USER")
    data = load_data()
    total = len(data)
    aktif = 0
    expired = 0
    for info in data.values():
        if datetime.fromisoformat(info['expired']) > datetime.now():
            aktif += 1
        else:
            expired += 1
    print(f"{Fore.WHITE}📌 Statistik:")
    print(f"{Fore.WHITE}  • Total User : {total}")
    print(f"{Fore.WHITE}  • User Aktif : {Fore.WHITE}{aktif}")
    print(f"{Fore.WHITE}  • User Expired: {Fore.WHITE}{expired}")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

# ============================================
# 🔥 SPAM NGL 🔥
# ============================================

def spam_ngl():
    show_banner()
    print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}📨 SPAM NGL - VVIP FINAL  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}Support 2 tipe input:
{Fore.WHITE}  1. https://ngl.link/*****
{Fore.WHITE}  2. *****
{Fore.WHITE}
""")
    
    raw_input = input(f"{Fore.WHITE}[+] MASUKKAN USERNAME / LINK NGL: {Fore.WHITE}").strip()
    if not raw_input:
        print(f"{Fore.WHITE}❌ Input tidak boleh kosong!")
        time.sleep(1)
        return
    
    username = extract_username(raw_input)
    if not username:
        print(f"{Fore.WHITE}❌ GAGAL! Format username/link tidak valid!")
        time.sleep(1)
        return
    
    print(f"{Fore.WHITE}✅ USERNAME DETEKSI: @{username}")
    
    message = input(f"{Fore.WHITE}[+] MASUKKAN PESAN SPAM: {Fore.WHITE}").strip()
    if not message:
        print(f"{Fore.WHITE}❌ Pesan tidak boleh kosong!")
        time.sleep(1)
        return
    
    try:
        count = int(input(f"{Fore.WHITE}[+] JUMLAH SPAM (1-9999): {Fore.WHITE}").strip())
        if count < 1: count = 1
        if count > 9999: count = 9999
    except:
        count = 100
        print(f"{Fore.WHITE}⚠️ Menggunakan default: 100")
    
    try:
        delay = float(input(f"{Fore.WHITE}[+] DELAY (detik, 0.1-5): {Fore.WHITE}").strip())
        if delay < 0.1: delay = 0.1
        if delay > 5: delay = 5
    except:
        delay = 0.5
        print(f"{Fore.WHITE}⚠️ Menggunakan default: 0.5s")
    
    print(f"{Fore.WHITE}\n[!] PERINGATAN: Ini untuk iseng-iseng!")
    confirm = input(f"{Fore.WHITE}[?] Yakin mau lanjut? (y/n): {Fore.WHITE}").strip().lower()
    if confirm != 'y':
        print(f"{Fore.WHITE}[!] Dibatalkan!")
        time.sleep(1)
        return
    
    print(f"{Fore.WHITE}⏳ Loading...")
    time.sleep(0.5)
    
    print(f"{Fore.WHITE}\n[+] TARGET: @{username}")
    print(f"{Fore.WHITE}[+] PESAN: {message[:50]}...")
    print(f"{Fore.WHITE}[+] JUMLAH: {count}")
    print(f"{Fore.WHITE}[+] DELAY: {delay}s")
    print(f"{Fore.WHITE}=" * 70 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for i in range(1, count + 1):
        try:
            msg_to_send = message
            status, result = send_ngl_message(username, msg_to_send)
            
            if status:
                success_count += 1
                print(f"{Fore.WHITE}[{i}/{count}] ✅ {result}")
            else:
                fail_count += 1
                print(f"{Fore.WHITE}[{i}/{count}] {result}")
            
            progress = (i / count) * 100
            bar_length = 40
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"{Fore.WHITE}Progress: [{bar}] {progress:.1f}%")
            
            if i < count:
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"{Fore.WHITE}\n[!] Spam dihentikan oleh user!")
            break
        except Exception as e:
            print(f"{Fore.WHITE}[{i}/{count}] ❌ Error: {str(e)[:50]}")
            fail_count += 1
            time.sleep(1)
    
    print(f"{Fore.WHITE}\n" + "=" * 70)
    print(f"{Fore.WHITE}📊 HASIL SPAM:")
    print(f"{Fore.WHITE}✅ Berhasil: {success_count}")
    print(f"{Fore.WHITE}❌ Gagal: {fail_count}")
    print(f"{Fore.WHITE}📦 Total: {success_count + fail_count}")
    print(f"{Fore.WHITE}" + "=" * 70)
    
    if success_count > 0:
        print(f"{Fore.WHITE}🔥 SPAM BERHASIL!")
    else:
        print(f"{Fore.WHITE}💀 GAGAL SEMUA! CEK USERNAME ATAU COBA LAGI!")
    
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali...")

# ============================================
# 🔥 LOGIN 🔥
# ============================================

def login():
    show_banner()
    print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}🔐 LOGIN - VVIP FINAL  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}Masukkan Username & Password untuk melanjutkan.
{Fore.WHITE}Belum punya password? Hubungi {TELEGRAM}
{Fore.WHITE}
""")
    
    username = input(f"{Fore.WHITE}Username: {Fore.WHITE}").strip()
    password = input(f"{Fore.WHITE}Password: {Fore.WHITE}").strip()
    
    if not username or not password:
        print(f"{Fore.WHITE}❌ Username dan password tidak boleh kosong!")
        time.sleep(1)
        return False
    
    if password == MASTER_PASSWORD:
        print(f"{Fore.WHITE}✅ Login berhasil (MASTER)!")
        log_activity(f"Login master: {username}")
        time.sleep(1)
        return True
    
    status, msg = verify_password(username, password)
    print(f"{Fore.WHITE}{msg}")
    time.sleep(1)
    
    return status

# ============================================
# 🔥 MAIN MENU 🔥
# ============================================

def main_menu():
    while True:
        show_banner()
        print(f"""
{Fore.WHITE}╔════════════════════════════════════════════╗
{Fore.WHITE}║     {Fore.WHITE}📌 MAIN MENU - VVIP FINAL  {Fore.WHITE}║
{Fore.WHITE}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}[1] 📨 SPAM NGL
{Fore.WHITE}[2] 👑 TOOLS OWNER
{Fore.WHITE}[3] 🌍 PUBLIC TOOLS
{Fore.WHITE}[4] 🔓 LOGOUT
{Fore.WHITE}[5] 🚪 EXIT
{Fore.WHITE}
""")
        choice = input(f"{Fore.WHITE}Pilih [1-5]: {Fore.WHITE}").strip()
        
        if choice == '1':
            spam_ngl()
        elif choice == '2':
            # Cek password owner
            print(f"{Fore.WHITE}🔑 Masukkan Password Owner:")
            pw = input(f"{Fore.WHITE}Password: ").strip()
            if pw == OWNER_PASSWORD:
                tools_owner()
            else:
                print(f"{Fore.WHITE}❌ Password salah!")
                time.sleep(1)
        elif choice == '3':
            public_tools()
        elif choice == '4':
            print(f"{Fore.WHITE}🔓 Logout...")
            time.sleep(1)
            return
        elif choice == '5':
            print(f"{Fore.WHITE}👋 Keluar dari ALEGRA NGL SPAM...")
            sys.exit(0)
        else:
            print(f"{Fore.WHITE}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 MAIN 🔥
# ============================================

def main():
    if login():
        main_menu()
    else:
        print(f"{Fore.WHITE}\n❌ Login gagal! Hubungi {TELEGRAM} untuk password.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.WHITE}\n[!] Keluar...")
    finally:
        print(f"{Fore.WHITE}\n📨 ALEGRA NGL SPAM - VVIP FINAL EDITION")
        print(f"{Fore.WHITE}Script By : Alegra Ega")
        print(f"{Fore.WHITE}Telegram : @egaa_1")
