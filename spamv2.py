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

VERSION = "ULTIMATE 4.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"
ADMIN_PASSWORD = "alegra ega"
DATA_FILE = os.path.expanduser("~/.alegra_ultimate_data.json")

# ============================================
# 🔥 BANNER ULTIMATE + RGB 🔥
# ============================================

def rgb_text(text, speed=0.02):
    """Animasi RGB sederhana"""
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Fore.RESET)

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    
    # Banner atas dengan RGB
    print()
    rgb_text("██████████████████████████████████████████████████████████████████████████████")
    print()
    rgb_text("██╗  ██╗██╗██████╗  ██████╗ ██╗   ██╗██╗")
    rgb_text("██║  ██║██║██╔══██╗██╔═══██╗╚██╗ ██╔╝██║")
    rgb_text("███████║██║██████╔╝██║   ██║ ╚████╔╝ ██║")
    rgb_text("██╔══██║██║██╔═══╝ ██║   ██║  ╚██╔╝  ██║")
    rgb_text("██║  ██║██║██║     ╚██████╔╝   ██║   ██║")
    rgb_text("╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝    ╚═╝   ╚═╝")
    print()
    rgb_text("██████████████████████████████████████████████████████████████████████████████")
    print()
    
    # Logo / Ikon (tempat foto lo nanti)
    print(f"{Fore.CYAN}╔════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║     {Fore.YELLOW}📸 [ IKON ALEGRA ] 📸                {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚════════════════════════════════════════════╝")
    print()
    
    print(f"{Fore.GREEN}╔══════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.GREEN}║                                                                  ║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}██████╗ ██╗   ██╗██████╗ ██╗     ███████╗██████╗ {Fore.GREEN}║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}██╔══██╗╚██╗ ██╔╝██╔══██╗██║     ██╔════╝██╔══██╗{Fore.GREEN}║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}██████╔╝ ╚████╔╝ ██████╔╝██║     █████╗  ██████╔╝{Fore.GREEN}║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}██╔══██╗  ╚██╔╝  ██╔══██╗██║     ██╔══╝  ██╔══██╗{Fore.GREEN}║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}██████╔╝   ██║   ██████╔╝███████╗███████╗██║  ██║{Fore.GREEN}║")
    print(f"{Fore.GREEN}║     {Fore.YELLOW}╚═════╝    ╚═╝   ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝{Fore.GREEN}║")
    print(f"{Fore.GREEN}║                                                                  ║")
    print(f"{Fore.GREEN}║           {Fore.CYAN}📨 ALEGRA SPAM NGL - {Fore.YELLOW}{VERSION}{Fore.CYAN} 📨       {Fore.GREEN}║")
    print(f"{Fore.GREEN}║              {Fore.MAGENTA}Script By : {AUTHOR}                       {Fore.GREEN}║")
    print(f"{Fore.GREEN}║              {Fore.WHITE}Telegram : {TELEGRAM}                         {Fore.GREEN}║")
    print(f"{Fore.GREEN}║              {Fore.RED}🔥 ULTIMATE EDITION - SUPER VIP 🔥              {Fore.GREEN}║")
    print(f"{Fore.GREEN}╚══════════════════════════════════════════════════════════════════╝")
    print()

# ============================================
# 🔥 ANIMASI RGB BERJALAN 🔥
# ============================================

def rgb_loading():
    """Loading dengan efek RGB"""
    chars = "█▓▒░▄▀"
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i in range(25):
        color = colors[i % len(colors)]
        sys.stdout.write(f"\r{color}[+] LOADING {chars[i % len(chars)] * 20}")
        sys.stdout.flush()
        time.sleep(0.05)
    print(Fore.RESET)

def rgb_progress(i, total):
    """Progress bar dengan efek RGB"""
    progress = (i / total) * 100
    bar_length = 40
    filled = int(bar_length * progress / 100)
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    color = colors[i % len(colors)]
    bar = f"{color}█{Fore.RESET}" * filled + f"{Fore.WHITE}░{Fore.RESET}" * (bar_length - filled)
    sys.stdout.write(f"\r{Fore.CYAN}Progress: [{bar}] {progress:.1f}% {Fore.YELLOW}[{i}/{total}]")
    sys.stdout.flush()

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
        return True, "✅ Login berhasil!"
    else:
        return False, "❌ Password salah!"

def list_users():
    data = load_data()
    if not data:
        print(f"{Fore.YELLOW}⚠️ Belum ada user terdaftar.")
        return
    
    print(f"\n{Fore.CYAN}📋 DAFTAR USER:")
    print(f"{Fore.MAGENTA}=" * 50)
    for username, info in data.items():
        expired = datetime.fromisoformat(info['expired'])
        status = f"{Fore.GREEN}AKTIF" if expired > datetime.now() else f"{Fore.RED}EXPIRED"
        durasi = info.get('duration', 'Unknown')
        print(f"{Fore.YELLOW}• {username} {status} {Fore.WHITE}({durasi})")

# ============================================
# 🔥 TOOLS PUBLIC (Tanpa Password) 🔥
# ============================================

def public_tools():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🌍 PUBLIC TOOLS - GRATIS!  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.GREEN}[1] {Fore.WHITE}🌐 Cek Website Online/Offline
{Fore.GREEN}[2] {Fore.WHITE}🔍 IP Lookup
{Fore.GREEN}[3] {Fore.WHITE}📡 Ping Test
{Fore.GREEN}[4] {Fore.WHITE}🌐 DNS Lookup
{Fore.GREEN}[5] {Fore.WHITE}🎭 Random User-Agent
{Fore.GREEN}[6] {Fore.WHITE}🔐 Base64 Encode/Decode
{Fore.GREEN}[7] {Fore.WHITE}📊 Cek Informasi Sistem
{Fore.GREEN}[8] {Fore.WHITE}📱 Cek Info HP (IMEI/Model)
{Fore.GREEN}[9] {Fore.WHITE}🌍 Cek IP Publik
{Fore.GREEN}[10] {Fore.WHITE}⏰ Cek Waktu & Tanggal
{Fore.GREEN}[11] {Fore.WHITE}🔙 Back
{Fore.RESET}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-11]: {Fore.WHITE}").strip()
        
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
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 TOOLS PUBLIC - FUNGSI-FUNGSI 🔥
# ============================================

def check_website():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🌐 CEK WEBSITE ONLINE/OFFLINE  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    url = input(f"{Fore.CYAN}[+] Masukkan URL: {Fore.WHITE}").strip()
    if not url:
        print(f"{Fore.RED}❌ URL tidak boleh kosong!")
        time.sleep(1)
        return
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{Fore.GREEN}✅ Website ONLINE! (Status: {response.status_code})")
        else:
            print(f"{Fore.YELLOW}⚠️ Website RESPOND (Status: {response.status_code})")
    except:
        print(f"{Fore.RED}❌ Website OFFLINE / TIDAK TERJANGKAU!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def ip_lookup():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🔍 IP LOOKUP TOOL  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    ip = input(f"{Fore.CYAN}[+] Masukkan IP: {Fore.WHITE}").strip()
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
            print(f"{Fore.RED}❌ Gagal mendapatkan info IP!")
    except:
        print(f"{Fore.RED}❌ Error! Cek koneksi internet.")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def ping_tool():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📡 PING TEST  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    target = input(f"{Fore.CYAN}[+] Masukkan IP / Domain: {Fore.WHITE}").strip()
    if not target:
        print(f"{Fore.RED}❌ Target tidak boleh kosong!")
        time.sleep(1)
        return
    
    try:
        response = os.system(f"ping -c 4 {target}")
        print(f"{Fore.GREEN}✅ Ping selesai!")
    except:
        print(f"{Fore.RED}❌ Gagal melakukan ping!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def dns_lookup():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🌐 DNS LOOKUP  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    domain = input(f"{Fore.CYAN}[+] Masukkan Domain: {Fore.WHITE}").strip()
    if not domain:
        print(f"{Fore.RED}❌ Domain tidak boleh kosong!")
        time.sleep(1)
        return
    
    try:
        import socket
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}✅ {domain} → {ip}")
    except:
        print(f"{Fore.RED}❌ Gagal resolve domain!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def user_agent_gen():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🎭 RANDOM USER-AGENT  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/15.0",
    ]
    print(f"{Fore.GREEN}📌 Random User-Agent:")
    print(f"{Fore.WHITE}{random.choice(agents)}")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def base64_tool():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🔐 BASE64 ENCODE/DECODE  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    print(f"{Fore.GREEN}[1] {Fore.WHITE}Encode")
    print(f"{Fore.GREEN}[2] {Fore.WHITE}Decode")
    choice = input(f"{Fore.CYAN}Pilih: {Fore.WHITE}").strip()
    
    text = input(f"{Fore.CYAN}Masukkan teks: {Fore.WHITE}").strip()
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
        print(f"{Fore.RED}❌ Error! Pastikan input benar.")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def system_info():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📊 INFO SISTEM  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    print(f"{Fore.GREEN}📌 Informasi Sistem:")
    print(f"{Fore.WHITE}  • OS      : {platform.system()} {platform.release()}")
    print(f"{Fore.WHITE}  • Hostname: {platform.node()}")
    print(f"{Fore.WHITE}  • Python  : {platform.python_version()}")
    print(f"{Fore.WHITE}  • Arch    : {platform.machine()}")
    print(f"{Fore.WHITE}  • CPU     : {platform.processor() or 'Unknown'}")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def device_info():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📱 INFO HP  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    print(f"{Fore.GREEN}📌 Informasi HP (Termux):")
    try:
        import subprocess
        model = subprocess.getoutput("getprop ro.product.model")
        brand = subprocess.getoutput("getprop ro.product.brand")
        android = subprocess.getoutput("getprop ro.build.version.release")
        print(f"{Fore.WHITE}  • Model   : {model}")
        print(f"{Fore.WHITE}  • Brand   : {brand}")
        print(f"{Fore.WHITE}  • Android : {android}")
    except:
        print(f"{Fore.WHITE}  • Info HP : Tidak tersedia (bukan Android)")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def public_ip():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🌍 CEK IP PUBLIK  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        print(f"{Fore.GREEN}✅ IP Publik Anda: {Fore.YELLOW}{ip}")
    except:
        print(f"{Fore.RED}❌ Gagal mendapatkan IP publik!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def show_datetime():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}⏰ WAKTU & TANGGAL  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    now = datetime.now()
    print(f"{Fore.GREEN}📌 Waktu Sekarang:")
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
# 🔥 TOOLS ADMIN 🔥
# ============================================

def tools_admin():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🛠️  TOOLS ADMIN - ULTIMATE  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.GREEN}[1] {Fore.WHITE}👥 Manage User (Create/List/Delete)
{Fore.GREEN}[2] {Fore.WHITE}📊 Lihat Log Aktivitas
{Fore.GREEN}[3] {Fore.WHITE}🔑 Ganti Password User
{Fore.GREEN}[4] {Fore.WHITE}📋 Backup Data User
{Fore.GREEN}[5] {Fore.WHITE}🗑️  Reset Semua Data
{Fore.GREEN}[6] {Fore.WHITE}📈 Statistik User
{Fore.GREEN}[7] {Fore.WHITE}🔙 Back
{Fore.RESET}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-7]: {Fore.WHITE}").strip()
        
        if choice == '1':
            admin_manage_user()
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
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

def admin_manage_user():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}👥 MANAGE USER  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.GREEN}[1] {Fore.WHITE}Create Password
{Fore.GREEN}[2] {Fore.WHITE}List User
{Fore.GREEN}[3] {Fore.WHITE}Delete User
{Fore.GREEN}[4] {Fore.WHITE}Back
{Fore.RESET}
""")
        choice = input(f"{Fore.CYAN}Pilih: {Fore.WHITE}").strip()
        
        if choice == '1':
            username = input(f"{Fore.CYAN}Username: {Fore.WHITE}").strip()
            if not username:
                print(f"{Fore.RED}❌ Username tidak boleh kosong!")
                time.sleep(1)
                continue
            
            print(f"{Fore.YELLOW}Durasi:")
            print(f"  {Fore.WHITE}[1] 24 Jam")
            print(f"  {Fore.WHITE}[2] 2 Hari")
            print(f"  {Fore.WHITE}[3] 7 Hari")
            print(f"  {Fore.WHITE}[4] PERMANEN")
            durasi_choice = input(f"{Fore.CYAN}Pilih durasi [1-4]: {Fore.WHITE}").strip()
            
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
            username = input(f"{Fore.CYAN}Username yang akan dihapus: {Fore.WHITE}").strip()
            if username:
                data = load_data()
                if username in data:
                    del data[username]
                    save_data(data)
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
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📊 LOG AKTIVITAS  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    log_file = os.path.expanduser("~/.alegra_log.txt")
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()
            if logs:
                for log in logs[-20:]:  # Tampilkan 20 log terakhir
                    print(f"{Fore.WHITE}{log.strip()}")
            else:
                print(f"{Fore.YELLOW}⚠️ Belum ada log.")
    else:
        print(f"{Fore.YELLOW}⚠️ Belum ada log.")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def change_user_password():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🔑 GANTI PASSWORD USER  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    username = input(f"{Fore.CYAN}Username: {Fore.WHITE}").strip()
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
    print(f"{Fore.GREEN}✅ Password baru untuk {username}: {Fore.YELLOW}{new_pass}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def backup_data():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📋 BACKUP DATA USER  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    data = load_data()
    if not data:
        print(f"{Fore.YELLOW}⚠️ Tidak ada data untuk di-backup.")
        time.sleep(1)
        return
    
    backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_file, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"{Fore.GREEN}✅ Backup berhasil! File: {backup_file}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def reset_all_data():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🗑️  RESET SEMUA DATA  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
    confirm = input(f"{Fore.RED}⚠️ Yakin ingin menghapus semua data? (y/n): {Fore.WHITE}").strip().lower()
    if confirm == 'y':
        save_data({})
        print(f"{Fore.GREEN}✅ Semua data berhasil direset!")
    else:
        print(f"{Fore.YELLOW}⚠️ Dibatalkan.")
    time.sleep(1)

def user_stats():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📈 STATISTIK USER  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
""")
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
# 🔥 SPAM NGL 🔥
# ============================================

def spam_ngl():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📨 SPAM NGL - ULTIMATE EDITION  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.WHITE}Support 2 tipe input:
{Fore.YELLOW}  1. https://ngl.link/*****
{Fore.YELLOW}  2. *****
{Fore.RESET}
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
    
    rgb_loading()
    
    print(f"{Fore.GREEN}\n[+] TARGET: @{username}")
    print(f"{Fore.GREEN}[+] PESAN: {message[:50]}...")
    print(f"{Fore.GREEN}[+] JUMLAH: {count}")
    print(f"{Fore.GREEN}[+] DELAY: {delay}s")
    print(f"{Fore.MAGENTA}=" * 70 + "\n")
    
    success_count = 0
    fail_count = 0
    
    for i in range(1, count + 1):
        try:
            msg_to_send = message
            status, result = send_ngl_message(username, msg_to_send)
            
            if status:
                success_count += 1
                print(f"{Fore.GREEN}[{i}/{count}] ✅ {result}")
            else:
                fail_count += 1
                print(f"{Fore.RED}[{i}/{count}] {result}")
            
            rgb_progress(i, count)
            
            if i < count:
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}\n[!] Spam dihentikan oleh user!")
            break
        except Exception as e:
            print(f"{Fore.RED}[{i}/{count}] ❌ Error: {str(e)[:50]}")
            fail_count += 1
            time.sleep(1)
    
    print(f"\n{Fore.MAGENTA}" + "=" * 70)
    print(f"{Fore.CYAN}📊 HASIL SPAM:")
    print(f"{Fore.GREEN}✅ Berhasil: {success_count}")
    print(f"{Fore.RED}❌ Gagal: {fail_count}")
    print(f"{Fore.YELLOW}📦 Total: {success_count + fail_count}")
    print(f"{Fore.MAGENTA}" + "=" * 70)
    
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
{Fore.CYAN}║     {Fore.YELLOW}🔐 LOGIN - ULTIMATE EDITION  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.WHITE}Masukkan Username & Password untuk melanjutkan.
{Fore.YELLOW}Belum punya password? Hubungi {TELEGRAM}
{Fore.RESET}
""")
    
    username = input(f"{Fore.CYAN}Username: {Fore.WHITE}").strip()
    password = input(f"{Fore.CYAN}Password: {Fore.WHITE}").strip()
    
    if not username or not password:
        print(f"{Fore.RED}❌ Username dan password tidak boleh kosong!")
        time.sleep(1)
        return False
    
    if password == MASTER_PASSWORD:
        print(f"{Fore.GREEN}✅ Login berhasil (MASTER)!")
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
{Fore.CYAN}║     {Fore.YELLOW}📌 MAIN MENU - ULTIMATE EDITION  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.GREEN}[1] {Fore.WHITE}📨 SPAM NGL
{Fore.GREEN}[2] {Fore.WHITE}🛠️  TOOLS ADMIN
{Fore.GREEN}[3] {Fore.WHITE}🌍 PUBLIC TOOLS
{Fore.GREEN}[4] {Fore.WHITE}🔓 LOGOUT
{Fore.GREEN}[5] {Fore.WHITE}🚪 EXIT
{Fore.RESET}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-5]: {Fore.WHITE}").strip()
        
        if choice == '1':
            spam_ngl()
        elif choice == '2':
            tools_admin()
        elif choice == '3':
            public_tools()
        elif choice == '4':
            print(f"{Fore.YELLOW}🔓 Logout...")
            time.sleep(1)
            return
        elif choice == '5':
            print(f"{Fore.GREEN}👋 Keluar dari ALEGRA SPAM NGL ULTIMATE...")
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
        print(f"{Fore.CYAN}\n📨 ALEGRA SPAM NGL - ULTIMATE EDITION")
        print(f"{Fore.MAGENTA}Script By : Alegra Ega")
        print(f"{Fore.WHITE}Telegram : @egaa_1")
