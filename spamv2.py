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

VERSION = "FINAL FIX 8.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"
OWNER_PASSWORD = "alegra ega"
DATA_FILE = os.path.expanduser("~/.alegra_fix_data.json")
LOG_FILE = os.path.expanduser("~/.alegra_fix_log.txt")

# ============================================
# 🔥 FUNGSI WAKTU REAL-TIME 🔥
# ============================================

def get_datetime():
    now = datetime.now()
    hari = now.strftime('%A')
    tanggal = now.strftime('%d %B %Y')
    jam = now.strftime('%H:%M:%S')
    return hari, tanggal, jam

# ============================================
# 🔥 BANNER RAPIH KECIL 🔥
# ============================================

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    
    hari, tanggal, jam = get_datetime()
    
    print(f"""{Fore.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {Fore.YELLOW}█████╗ ██╗     ███████╗ ██████╗ ██████╗  █████╗ {Fore.CYAN} ║
║  {Fore.YELLOW}██╔══██╗██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗{Fore.CYAN} ║
║  {Fore.YELLOW}███████║██║     █████╗  ██║  ███╗██████╔╝███████║{Fore.CYAN} ║
║  {Fore.YELLOW}██╔══██║██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║{Fore.CYAN} ║
║  {Fore.YELLOW}██║  ██║███████╗███████╗╚██████╔╝██║  ██║██║  ██║{Fore.CYAN} ║
║  {Fore.YELLOW}╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{Fore.CYAN} ║
║                                                              ║
║  {Fore.GREEN}███████╗██████╗  █████╗ ███╗   ███╗             {Fore.CYAN} ║
║  {Fore.GREEN}██╔════╝██╔══██╗██╔══██╗████╗ ████║             {Fore.CYAN} ║
║  {Fore.GREEN}███████╗██████╔╝███████║██╔████╔██║             {Fore.CYAN} ║
║  {Fore.GREEN}╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║             {Fore.CYAN} ║
║  {Fore.GREEN}███████║██║     ██║  ██║██║ ╚═╝ ██║             {Fore.CYAN} ║
║  {Fore.GREEN}╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝             {Fore.CYAN} ║
║                                                              ║
║  ╔══════════════════════════════════════════════════════════╗ ║
║  ║  {Fore.WHITE}📨 ALEGRA SPAM - {Fore.WHITE}{VERSION}{Fore.WHITE}         {Fore.CYAN}║ ║
║  ║  {Fore.WHITE}Script By : {AUTHOR}                         {Fore.CYAN}║ ║
║  ║  {Fore.WHITE}Telegram : {TELEGRAM}                           {Fore.CYAN}║ ║
║  ╚══════════════════════════════════════════════════════════╝ ║
║                                                              ║
║  ┌────────────────────┐    ┌────────────────────┐           ║
║  │ {Fore.WHITE}⏰ {hari:<14}  {Fore.CYAN}│    │ {Fore.WHITE}📅 {tanggal:<14} {Fore.CYAN}│           ║
║  │ {Fore.WHITE}🕐 {jam:<14}  {Fore.CYAN}│    │ {Fore.WHITE}📍 Indonesia {Fore.CYAN} │           ║
║  └────────────────────┘    └────────────────────┘           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Fore.RESET}
""")

# ── THREAD BUAT UPDATE JAM ──
def update_clock():
    while True:
        # Cek apakah ada input user (biar gak ganggu)
        time.sleep(1)

clock_thread = threading.Thread(target=update_clock, daemon=True)
clock_thread.start()

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
        print(f"{Fore.YELLOW}⚠️ Belum ada user terdaftar.")
        return
    
    print(f"\n{Fore.CYAN}📋 DAFTAR USER:")
    print(f"{Fore.CYAN}=" * 50)
    for username, info in data.items():
        expired = datetime.fromisoformat(info['expired'])
        status = f"{Fore.GREEN}AKTIF" if expired > datetime.now() else f"{Fore.RED}EXPIRED"
        durasi = info.get('duration', 'Unknown')
        print(f"{Fore.YELLOW}• {username} {status} {Fore.WHITE}({durasi})")

# ============================================
# 🔥 PUBLIC TOOLS (25 TOOLS) 🔥
# ============================================

def public_tools():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🌍 PUBLIC TOOLS - 25 TOOLS  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.GREEN}[1]  {Fore.WHITE}🌐 Cek Website Online/Offline
{Fore.GREEN}[2]  {Fore.WHITE}🔍 IP Lookup
{Fore.GREEN}[3]  {Fore.WHITE}📡 Ping Test
{Fore.GREEN}[4]  {Fore.WHITE}🌐 DNS Lookup
{Fore.GREEN}[5]  {Fore.WHITE}🎭 Random User-Agent
{Fore.GREEN}[6]  {Fore.WHITE}🔐 Base64 Encode/Decode
{Fore.GREEN}[7]  {Fore.WHITE}📊 Cek Informasi Sistem
{Fore.GREEN}[8]  {Fore.WHITE}📱 Cek Info HP
{Fore.GREEN}[9]  {Fore.WHITE}🌍 Cek IP Publik
{Fore.GREEN}[10] {Fore.WHITE}⏰ Cek Waktu & Tanggal
{Fore.GREEN}[11] {Fore.WHITE}📁 Cek Storage HP
{Fore.GREEN}[12] {Fore.WHITE}🔋 Cek Baterai HP
{Fore.GREEN}[13] {Fore.WHITE}📶 Cek Signal/WiFi
{Fore.GREEN}[14] {Fore.WHITE}🧮 Kalkulator Sederhana
{Fore.GREEN}[15] {Fore.WHITE}📝 Random Password Generator
{Fore.GREEN}[16] {Fore.WHITE}🔢 Random Number Generator
{Fore.GREEN}[17] {Fore.WHITE}📊 Cek RAM Usage
{Fore.GREEN}[18] {Fore.WHITE}💻 Cek CPU Usage
{Fore.GREEN}[19] {Fore.WHITE}📂 Cek Folder Size
{Fore.GREEN}[20] {Fore.WHITE}🌐 Cek Domain Age
{Fore.GREEN}[21] {Fore.WHITE}🔍 Cek Port Scanning
{Fore.GREEN}[22] {Fore.WHITE}📧 Email Validator
{Fore.GREEN}[23] {Fore.WHITE}🔗 URL Shortener
{Fore.GREEN}[24] {Fore.WHITE}📝 Text to Binary
{Fore.GREEN}[25] {Fore.WHITE}🔙 Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-25]: {Fore.WHITE}").strip()
        
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
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 PUBLIC TOOLS - FUNGSI TAMBAHAN 🔥
# ============================================

def check_storage():
    show_banner()
    print(f"{Fore.CYAN}📁 CEK STORAGE HP")
    try:
        import subprocess
        result = subprocess.getoutput("df -h /data")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan info storage!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_battery():
    show_banner()
    print(f"{Fore.CYAN}🔋 CEK BATERAI HP")
    try:
        result = subprocess.getoutput("termux-battery-status")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan info baterai! (butuh termux-api)")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_signal():
    show_banner()
    print(f"{Fore.CYAN}📶 CEK SIGNAL/WIFI")
    try:
        result = subprocess.getoutput("termux-wifi-connectioninfo")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan info signal! (butuh termux-api)")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def calculator():
    show_banner()
    print(f"{Fore.CYAN}🧮 KALKULATOR SEDERHANA")
    try:
        expr = input(f"{Fore.WHITE}Masukkan operasi (contoh: 2+3): ")
        result = eval(expr)
        print(f"{Fore.WHITE}Hasil: {result}")
    except:
        print(f"{Fore.RED}❌ Error! Masukkan operasi yang benar.")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_password():
    show_banner()
    print(f"{Fore.CYAN}📝 RANDOM PASSWORD GENERATOR")
    try:
        length = int(input(f"{Fore.WHITE}Panjang password: ") or 12)
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=length))
        print(f"{Fore.WHITE}Password: {password}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_number():
    show_banner()
    print(f"{Fore.CYAN}🔢 RANDOM NUMBER GENERATOR")
    try:
        min_num = int(input(f"{Fore.WHITE}Min: ") or 1)
        max_num = int(input(f"{Fore.WHITE}Max: ") or 100)
        print(f"{Fore.WHITE}Random: {random.randint(min_num, max_num)}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_ram():
    show_banner()
    print(f"{Fore.CYAN}📊 CEK RAM USAGE")
    try:
        import subprocess
        result = subprocess.getoutput("free -h")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan info RAM!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_cpu():
    show_banner()
    print(f"{Fore.CYAN}💻 CEK CPU USAGE")
    try:
        result = subprocess.getoutput("top -bn1 | head -10")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan info CPU!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_folder_size():
    show_banner()
    print(f"{Fore.CYAN}📂 CEK FOLDER SIZE")
    folder = input(f"{Fore.WHITE}Masukkan path folder: ")
    try:
        import subprocess
        result = subprocess.getoutput(f"du -sh {folder} 2>/dev/null")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_domain_age():
    show_banner()
    print(f"{Fore.CYAN}🌐 CEK DOMAIN AGE")
    domain = input(f"{Fore.WHITE}Masukkan domain: ")
    try:
        import whois
        w = whois.whois(domain)
        print(f"{Fore.WHITE}Domain: {domain}")
        print(f"{Fore.WHITE}Created: {w.creation_date}")
    except:
        print(f"{Fore.RED}❌ Gagal! (butuh python-whois)")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def port_scan():
    show_banner()
    print(f"{Fore.CYAN}🔍 CEK PORT SCANNING")
    ip = input(f"{Fore.WHITE}Masukkan IP: ")
    ports = input(f"{Fore.WHITE}Port (pisah koma): ")
    try:
        for port in ports.split(','):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, int(port)))
            if result == 0:
                print(f"{Fore.GREEN}Port {port} TERBUKA")
            else:
                print(f"{Fore.RED}Port {port} TERTUTUP")
            sock.close()
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def email_validator():
    show_banner()
    print(f"{Fore.CYAN}📧 EMAIL VALIDATOR")
    email = input(f"{Fore.WHITE}Masukkan email: ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{Fore.GREEN}✅ Email VALID")
    else:
        print(f"{Fore.RED}❌ Email INVALID")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def url_shortener():
    show_banner()
    print(f"{Fore.CYAN}🔗 URL SHORTENER")
    url = input(f"{Fore.WHITE}Masukkan URL: ")
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            print(f"{Fore.GREEN}Short URL: {response.text}")
        else:
            print(f"{Fore.RED}❌ Gagal!")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def text_to_binary():
    show_banner()
    print(f"{Fore.CYAN}📝 TEXT TO BINARY")
    text = input(f"{Fore.WHITE}Masukkan teks: ")
    binary = ' '.join(format(ord(c), '08b') for c in text)
    print(f"{Fore.WHITE}Binary: {binary}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 PUBLIC TOOLS - FUNGSI DASAR 🔥
# ============================================

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
            print(f"{Fore.WHITE}  • Negara  : {data.get('country', '-')}")
            print(f"{Fore.WHITE}  • Kota    : {data.get('city', '-')}")
            print(f"{Fore.WHITE}  • ISP     : {data.get('isp', '-')}")
            print(f"{Fore.WHITE}  • Region  : {data.get('regionName', '-')}")
            print(f"{Fore.WHITE}  • Timezone: {data.get('timezone', '-')}")
        else:
            print(f"{Fore.RED}❌ Gagal!")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def ping_tool():
    show_banner()
    print(f"{Fore.CYAN}📡 PING TEST")
    target = input(f"{Fore.WHITE}IP / Domain: ").strip()
    if not target:
        print(f"{Fore.RED}❌ Target tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        os.system(f"ping -c 4 {target}")
    except:
        print(f"{Fore.RED}❌ Gagal!")
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

def user_agent_gen():
    show_banner()
    print(f"{Fore.CYAN}🎭 RANDOM USER-AGENT")
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/20100101 Firefox/119.0",
    ]
    print(f"{Fore.GREEN}📌 Random User-Agent:")
    print(f"{Fore.WHITE}{random.choice(agents)}")
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
        import base64
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
    print(f"{Fore.WHITE}  • OS      : {platform.system()} {platform.release()}")
    print(f"{Fore.WHITE}  • Hostname: {platform.node()}")
    print(f"{Fore.WHITE}  • Python  : {platform.python_version()}")
    print(f"{Fore.WHITE}  • Arch    : {platform.machine()}")
    print(f"{Fore.WHITE}  • CPU     : {platform.processor() or 'Unknown'}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def device_info():
    show_banner()
    print(f"{Fore.CYAN}📱 INFO HP")
    try:
        model = subprocess.getoutput("getprop ro.product.model")
        brand = subprocess.getoutput("getprop ro.product.brand")
        android = subprocess.getoutput("getprop ro.build.version.release")
        print(f"{Fore.WHITE}  • Model   : {model}")
        print(f"{Fore.WHITE}  • Brand   : {brand}")
        print(f"{Fore.WHITE}  • Android : {android}")
    except:
        print(f"{Fore.RED}  • Info HP : Tidak tersedia")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def public_ip():
    show_banner()
    print(f"{Fore.CYAN}🌍 CEK IP PUBLIK")
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"{Fore.GREEN}✅ IP Publik: {Fore.WHITE}{ip}")
    except:
        print(f"{Fore.RED}❌ Gagal!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def show_datetime():
    show_banner()
    print(f"{Fore.CYAN}⏰ WAKTU & TANGGAL")
    now = datetime.now()
    print(f"{Fore.WHITE}  • Tanggal : {now.strftime('%d %B %Y')}")
    print(f"{Fore.WHITE}  • Hari    : {now.strftime('%A')}")
    print(f"{Fore.WHITE}  • Waktu   : {now.strftime('%H:%M:%S')}")
    print(f"{Fore.WHITE}  • Timezone: {time.tzname[0]}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

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
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}👑 TOOLS OWNER - 15 TOOLS  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.GREEN}[1]  {Fore.WHITE}👥 Manage User (Create/List/Delete)
{Fore.GREEN}[2]  {Fore.WHITE}📊 Lihat Log Aktivitas
{Fore.GREEN}[3]  {Fore.WHITE}🔑 Ganti Password User
{Fore.GREEN}[4]  {Fore.WHITE}📋 Backup Data User
{Fore.GREEN}[5]  {Fore.WHITE}🗑️  Reset Semua Data
{Fore.GREEN}[6]  {Fore.WHITE}📈 Statistik User
{Fore.GREEN}[7]  {Fore.WHITE}👑 Tambah Owner Baru
{Fore.GREEN}[8]  {Fore.WHITE}📋 Lihat Daftar Owner
{Fore.GREEN}[9]  {Fore.WHITE}🗑️  Hapus Owner
{Fore.GREEN}[10] {Fore.WHITE}🔄 Ganti Password Owner
{Fore.GREEN}[11] {Fore.WHITE}📊 Log Aktivitas Owner
{Fore.GREEN}[12] {Fore.WHITE}🔒 Lock Tools
{Fore.GREEN}[13] {Fore.WHITE}🔓 Unlock Tools
{Fore.GREEN}[14] {Fore.WHITE}📋 Cek Status Tools
{Fore.GREEN}[15] {Fore.WHITE}🔙 Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-15]: {Fore.WHITE}").strip()
        
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
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
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
    print(f"{Fore.CYAN}👑 TAMBAH OWNER BARU")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    password = input(f"{Fore.WHITE}Password: ").strip()
    if not password:
        print(f"{Fore.RED}❌ Password tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username in owners:
        print(f"{Fore.RED}❌ Username sudah menjadi owner!")
        time.sleep(1)
        return
    owners[username] = {
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'created': datetime.now().isoformat()
    }
    save_owners(owners)
    log_activity(f"Owner baru: {username}")
    print(f"{Fore.GREEN}✅ Owner {username} berhasil ditambahkan!")
    time.sleep(1)

def list_owners():
    show_banner()
    print(f"{Fore.CYAN}📋 DAFTAR OWNER")
    owners = load_owners()
    if not owners:
        print(f"{Fore.YELLOW}⚠️ Belum ada owner terdaftar.")
    else:
        for username, info in owners.items():
            created = datetime.fromisoformat(info['created']).strftime('%d-%m-%Y %H:%M')
            print(f"{Fore.WHITE}• {username} (created: {created})")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def remove_owner():
    show_banner()
    print(f"{Fore.CYAN}🗑️  HAPUS OWNER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username not in owners:
        print(f"{Fore.RED}❌ Username tidak ditemukan!")
        time.sleep(1)
        return
    del owners[username]
    save_owners(owners)
    log_activity(f"Owner dihapus: {username}")
    print(f"{Fore.GREEN}✅ Owner {username} berhasil dihapus!")
    time.sleep(1)

def change_owner_password():
    show_banner()
    print(f"{Fore.CYAN}🔄 GANTI PASSWORD OWNER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    owners = load_owners()
    if username not in owners:
        print(f"{Fore.RED}❌ Username tidak ditemukan!")
        time.sleep(1)
        return
    new_pass = input(f"{Fore.WHITE}Password baru: ").strip()
    if not new_pass:
        print(f"{Fore.RED}❌ Password tidak boleh kosong!")
        time.sleep(1)
        return
    owners[username]['password'] = hashlib.sha256(new_pass.encode()).hexdigest()
    save_owners(owners)
    log_activity(f"Password owner diubah: {username}")
    print(f"{Fore.GREEN}✅ Password owner {username} berhasil diubah!")
    time.sleep(1)

def owner_logs():
    show_banner()
    print(f"{Fore.CYAN}📊 LOG AKTIVITAS OWNER")
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

def lock_tools():
    show_banner()
    print(f"{Fore.CYAN}🔒 LOCK TOOLS")
    confirm = input(f"{Fore.YELLOW}Yakin lock tools? (y/n): ").strip().lower()
    if confirm == 'y':
        with open(os.path.expanduser("~/.alegra_locked"), 'w') as f:
            f.write("locked")
        log_activity("Tools di-lock")
        print(f"{Fore.GREEN}✅ Tools berhasil di-lock!")
    else:
        print(f"{Fore.YELLOW}⚠️ Dibatalkan.")
    time.sleep(1)

def unlock_tools():
    show_banner()
    print(f"{Fore.CYAN}🔓 UNLOCK TOOLS")
    confirm = input(f"{Fore.YELLOW}Yakin unlock tools? (y/n): ").strip().lower()
    if confirm == 'y':
        os.remove(os.path.expanduser("~/.alegra_locked"))
        log_activity("Tools di-unlock")
        print(f"{Fore.GREEN}✅ Tools berhasil di-unlock!")
    else:
        print(f"{Fore.YELLOW}⚠️ Dibatalkan.")
    time.sleep(1)

def check_tools_status():
    show_banner()
    print(f"{Fore.CYAN}📋 CEK STATUS TOOLS")
    if os.path.exists(os.path.expanduser("~/.alegra_locked")):
        print(f"{Fore.RED}🔒 Status: LOCKED")
    else:
        print(f"{Fore.GREEN}🔓 Status: UNLOCKED")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def owner_manage_user():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}👥 MANAGE USER  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.GREEN}[1] {Fore.WHITE}Create Password
{Fore.GREEN}[2] {Fore.WHITE}List User
{Fore.GREEN}[3] {Fore.WHITE}Delete User
{Fore.GREEN}[4] {Fore.WHITE}Back
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih: {Fore.WHITE}").strip()
        
        if choice == '1':
            username = input(f"{Fore.WHITE}Username: ").strip()
            if not username:
                print(f"{Fore.RED}❌ Username tidak boleh kosong!")
                time.sleep(1)
                continue
            
            print(f"{Fore.YELLOW}Durasi:")
            print(f"  {Fore.WHITE}[1] 24 Jam")
            print(f"  {Fore.WHITE}[2] 2 Hari")
            print(f"  {Fore.WHITE}[3] 7 Hari")
            print(f"  {Fore.WHITE}[4] PERMANEN")
            durasi_choice = input(f"{Fore.CYAN}Pilih durasi [1-4]: ").strip()
            
            if durasi_choice == '1':
                hours = 24
            elif durasi_choice == '2':
                hours = 48
            elif durasi_choice == '3':
                hours = 168
            elif durasi_choice == '4':
                hours = 0
            else:
                print(f"{Fore.RED}❌ Pilihan tidak valid! Menggunakan default: 24 jam")
                hours = 24
            
            result, msg = create_password(username, hours)
            print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
            time.sleep(2)
            
        elif choice == '2':
            list_users()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
            
        elif choice == '3':
            username = input(f"{Fore.WHITE}Username yang akan dihapus: ").strip()
            if username:
                data = load_data()
                if username in data:
                    del data[username]
                    save_data(data)
                    log_activity(f"User dihapus: {username}")
                    print(f"{Fore.GREEN}✅ User {username} berhasil dihapus!")
                else:
                    print(f"{Fore.RED}❌ User tidak ditemukan!")
                time.sleep(1)
            
        elif choice == '4':
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
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

def change_user_password():
    show_banner()
    print(f"{Fore.CYAN}🔑 GANTI PASSWORD USER")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    data = load_data()
    if username not in data:
        print(f"{Fore.RED}❌ User tidak ditemukan!")
        time.sleep(1)
        return
    new_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    data[username]['password'] = hashlib.sha256(new_pass.encode()).hexdigest()
    save_data(data)
    log_activity(f"Password diubah untuk: {username}")
    print(f"{Fore.GREEN}✅ Password baru untuk {username}: {Fore.WHITE}{new_pass}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def backup_data():
    show_banner()
    print(f"{Fore.CYAN}📋 BACKUP DATA USER")
    data = load_data()
    if not data:
        print(f"{Fore.YELLOW}⚠️ Tidak ada data untuk di-backup.")
        time.sleep(1)
        return
    backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    log_activity(f"Backup data: {backup_file}")
    print(f"{Fore.GREEN}✅ Backup berhasil! File: {backup_file}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def reset_all_data():
    show_banner()
    print(f"{Fore.CYAN}🗑️  RESET SEMUA DATA")
    confirm = input(f"{Fore.RED}⚠️ Yakin ingin menghapus semua data? (y/n): ").strip().lower()
    if confirm == 'y':
        save_data({})
        log_activity("Semua data direset")
        print(f"{Fore.GREEN}✅ Semua data berhasil direset!")
    else:
        print(f"{Fore.YELLOW}⚠️ Dibatalkan.")
    time.sleep(1)

def user_stats():
    show_banner()
    print(f"{Fore.CYAN}📈 STATISTIK USER")
    data = load_data()
    total = len(data)
    aktif = 0
    expired = 0
    for info in data.values():
        if datetime.fromisoformat(info['expired']) > datetime.now():
            aktif += 1
        else:
            expired += 1
    print(f"{Fore.GREEN}📌 Statistik:")
    print(f"{Fore.WHITE}  • Total User : {total}")
    print(f"{Fore.WHITE}  • User Aktif : {Fore.GREEN}{aktif}")
    print(f"{Fore.WHITE}  • User Expired: {Fore.RED}{expired}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 SPAM NGL - ANIMASI RAPIH 🔥
# ============================================

def spam_ngl():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📨 SPAM NGL - FINAL FIX  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}Support 2 tipe input:
{Fore.YELLOW}  1. https://ngl.link/*****
{Fore.YELLOW}  2. *****
{Fore.WHITE}
""")
    
    raw_input = input(f"{Fore.CYAN}[+] MASUKKAN USERNAME / LINK NGL: {Fore.WHITE}").strip()
    if not raw_input:
        print(f"{Fore.RED}❌ Input tidak boleh kosong!")
        time.sleep(1)
        return
    
    username = extract_username(raw_input)
    if not username:
        print(f"{Fore.RED}❌ GAGAL! Format username/link tidak valid!")
        time.sleep(1)
        return
    
    print(f"{Fore.GREEN}✅ USERNAME DETEKSI: @{username}")
    
    message = input(f"{Fore.CYAN}[+] MASUKKAN PESAN SPAM: {Fore.WHITE}").strip()
    if not message:
        print(f"{Fore.RED}❌ Pesan tidak boleh kosong!")
        time.sleep(1)
        return
    
    try:
        count = int(input(f"{Fore.CYAN}[+] JUMLAH SPAM (1-9999): {Fore.WHITE}").strip())
        if count < 1: count = 1
        if count > 9999: count = 9999
    except:
        count = 100
        print(f"{Fore.YELLOW}⚠️ Menggunakan default: 100")
    
    try:
        delay = float(input(f"{Fore.CYAN}[+] DELAY (detik, 0.1-5): {Fore.WHITE}").strip())
        if delay < 0.1: delay = 0.1
        if delay > 5: delay = 5
    except:
        delay = 0.5
        print(f"{Fore.YELLOW}⚠️ Menggunakan default: 0.5s")
    
    print(f"{Fore.RED}\n[!] PERINGATAN: Ini untuk iseng-iseng!")
    confirm = input(f"{Fore.YELLOW}[?] Yakin mau lanjut? (y/n): {Fore.WHITE}").strip().lower()
    if confirm != 'y':
        print(f"{Fore.YELLOW}[!] Dibatalkan!")
        time.sleep(1)
        return
    
    print(f"{Fore.CYAN}⏳ Loading...")
    time.sleep(0.5)
    
    print(f"{Fore.GREEN}\n[+] TARGET: @{username}")
    print(f"{Fore.GREEN}[+] PESAN: {message[:50]}...")
    print(f"{Fore.GREEN}[+] JUMLAH: {count}")
    print(f"{Fore.GREEN}[+] DELAY: {delay}s")
    print(f"{Fore.CYAN}" + "=" * 60 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for i in range(1, count + 1):
        try:
            msg_to_send = message
            status, result = send_ngl_message(username, msg_to_send)
            
            progress = (i / count) * 100
            bar_length = 30
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            if status:
                success_count += 1
                print(f"{Fore.GREEN}[{i}/{count}] ✅ {result}  [{bar}] {progress:.1f}%")
            else:
                fail_count += 1
                print(f"{Fore.RED}[{i}/{count}] {result}  [{bar}] {progress:.1f}%")
            
            if i < count:
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}\n[!] Spam dihentikan oleh user!")
            break
        except Exception as e:
            print(f"{Fore.RED}[{i}/{count}] ❌ Error: {str(e)[:50]}")
            fail_count += 1
            time.sleep(1)
    
    print(f"{Fore.CYAN}\n" + "=" * 60)
    print(f"{Fore.CYAN}📊 HASIL SPAM:")
    print(f"{Fore.GREEN}✅ Berhasil: {success_count}")
    print(f"{Fore.RED}❌ Gagal: {fail_count}")
    print(f"{Fore.YELLOW}📦 Total: {success_count + fail_count}")
    print(f"{Fore.CYAN}" + "=" * 60)
    
    if success_count > 0:
        print(f"{Fore.GREEN}🔥 SPAM BERHASIL!")
    else:
        print(f"{Fore.RED}💀 GAGAL SEMUA! CEK USERNAME ATAU COBA LAGI!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 LOGIN 🔥
# ============================================

def login():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🔐 LOGIN - FINAL FIX  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.WHITE}Masukkan Username & Password untuk melanjutkan.
{Fore.YELLOW}Belum punya password? Hubungi {TELEGRAM}
{Fore.WHITE}
""")
    
    username = input(f"{Fore.CYAN}Username: {Fore.WHITE}").strip()
    password = input(f"{Fore.CYAN}Password: {Fore.WHITE}").strip()
    
    if not username or not password:
        print(f"{Fore.RED}❌ Username dan password tidak boleh kosong!")
        time.sleep(1)
        return False
    
    if password == MASTER_PASSWORD:
        print(f"{Fore.GREEN}✅ Login berhasil (MASTER)!")
        log_activity(f"Login master: {username}")
        time.sleep(1)
        return True
    
    status, msg = verify_password(username, password)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    time.sleep(1)
    
    return status

# ============================================
# 🔥 MAIN MENU 🔥
# ============================================

def main_menu():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📌 MAIN MENU - FINAL FIX  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.WHITE}
{Fore.GREEN}[1] {Fore.WHITE}📨 SPAM NGL
{Fore.GREEN}[2] {Fore.WHITE}👑 TOOLS OWNER
{Fore.GREEN}[3] {Fore.WHITE}🌍 PUBLIC TOOLS
{Fore.GREEN}[4] {Fore.WHITE}🔓 LOGOUT
{Fore.GREEN}[5] {Fore.WHITE}🚪 EXIT
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-5]: {Fore.WHITE}").strip()
        
        if choice == '1':
            spam_ngl()
        elif choice == '2':
            print(f"{Fore.YELLOW}🔑 Masukkan Password Owner:")
            pw = input(f"{Fore.WHITE}Password: ").strip()
            if pw == OWNER_PASSWORD:
                tools_owner()
            else:
                print(f"{Fore.RED}❌ Password salah!")
                time.sleep(1)
        elif choice == '3':
            public_tools()
        elif choice == '4':
            print(f"{Fore.YELLOW}🔓 Logout...")
            time.sleep(1)
            return
        elif choice == '5':
            print(f"{Fore.GREEN}👋 Keluar dari ALEGRA SPAM...")
            sys.exit(0)
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 MAIN 🔥
# ============================================

def main():
    if login():
        main_menu()
    else:
        print(f"{Fore.RED}\n❌ Login gagal! Hubungi {TELEGRAM} untuk password.")
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}\n[!] Keluar...")
    finally:
        print(f"{Fore.CYAN}\n📨 ALEGRA SPAM - FINAL FIX EDITION")
        print(f"{Fore.MAGENTA}Script By : Alegra Ega")
        print(f"{Fore.WHITE}Telegram : @egaa_1")
