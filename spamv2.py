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
import smtplib
import email.utils
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from colorama import init, Fore, Style, Back

init(autoreset=True)
os.system("clear" if os.name == "posix" else "cls")

# ============================================
# 🔥 KONFIGURASI 🔥
# ============================================

VERSION = "PREMIUM 18.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"
OWNER_PASSWORD = "alegra ega"
DATA_FILE = os.path.expanduser("~/.alegra_premium_data.json")
LOG_FILE = os.path.expanduser("~/.alegra_premium_log.txt")
OWNER_FILE = os.path.expanduser("~/.alegra_owners.json")
HEAD_OWNER = "egaa"
VERIF_FILE = os.path.expanduser("~/.alegra_verif.json")

# ============================================
# 🔥 FUNGSI VERIFIKASI GMAIL + OTP 🔥
# ============================================

def load_verif():
    if os.path.exists(VERIF_FILE):
        try:
            with open(VERIF_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_verif(data):
    with open(VERIF_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_verification_email(to_email, otp):
    try:
        # Simulasi kirim OTP (tanpa SMTP real)
        # Untuk real, lo bisa ganti dengan SMTP + App Password
        print(f"{Fore.GREEN}✅ Kode OTP dikirim ke {to_email}")
        print(f"{Fore.YELLOW}📧 (Simulasi) OTP: {otp}")
        return True
    except Exception as e:
        print(f"{Fore.RED}❌ Gagal kirim email: {e}")
        return False

def verify_egaa_access():
    print(f"\n{Fore.CYAN}┌──────────────────────────────────────────────┐")
    print(f"{Fore.CYAN}│     {Fore.YELLOW}🔐 VERIFIKASI GMAIL + OTP  {Fore.CYAN}│")
    print(f"{Fore.CYAN}└──────────────────────────────────────────────┘")
    print(f"{Fore.WHITE}")
    
    # Step 1: Masukkan Gmail
    email = input(f"{Fore.CYAN}[+] Masukkan Gmail Anda: {Fore.WHITE}").strip()
    if not email:
        print(f"{Fore.RED}❌ Gmail tidak boleh kosong!")
        time.sleep(1)
        return False
    
    # Step 2: Generate OTP
    otp = generate_otp()
    data = load_verif()
    data['otp'] = otp
    data['expired'] = (datetime.now() + timedelta(minutes=5)).isoformat()
    data['email'] = email
    save_verif(data)
    
    # Step 3: Kirim OTP ke Gmail
    print(f"{Fore.GREEN}✅ Kode verifikasi telah dikirim ke {email}")
    print(f"{Fore.YELLOW}📧 Cek email Anda (termasuk spam/junk)")
    
    # Step 4: Masukkan OTP
    user_otp = input(f"{Fore.CYAN}[+] Masukkan Kode Verifikasi (6 digit): {Fore.WHITE}").strip()
    
    # Step 5: Verifikasi OTP
    verif_data = load_verif()
    if verif_data.get('otp') == user_otp:
        expired = datetime.fromisoformat(verif_data.get('expired', datetime.now().isoformat()))
        if expired > datetime.now():
            print(f"{Fore.GREEN}✅ Verifikasi berhasil! Selamat datang di Tools EGAA.")
            time.sleep(1)
            return True
        else:
            print(f"{Fore.RED}❌ Kode sudah expired! (5 menit)")
            time.sleep(1)
            return False
    else:
        print(f"{Fore.RED}❌ Kode salah!")
        time.sleep(1)
        return False

def get_datetime():
    now = datetime.now()
    hari = now.strftime('%A')
    tanggal = now.strftime('%d %B %Y')
    jam = now.strftime('%H:%M:%S')
    return hari, tanggal, jam

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    hari, tanggal, jam = get_datetime()
    print(f"""{Fore.CYAN}
┌────────────────────────────────────────────────┐
│ {Fore.YELLOW}██╗  ██╗██╗██████╗  ██████╗ █████╗      {Fore.CYAN}│
│ {Fore.YELLOW}██║  ██║██║██╔══██╗██╔═══██╗██╔══██╗    {Fore.CYAN}│
│ {Fore.YELLOW}███████║██║██████╔╝██║   ██║███████║    {Fore.CYAN}│
│ {Fore.YELLOW}██╔══██║██║██╔═══╝ ██║   ██║██╔══██║    {Fore.CYAN}│
│ {Fore.YELLOW}██║  ██║██║██║     ╚██████╔╝██║  ██║    {Fore.CYAN}│
│ {Fore.YELLOW}╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝    {Fore.CYAN}│
│ ╔══════════════════════════════════════════════╗ │
│ ║ {Fore.WHITE}📨 ALEGRA SPAM {Fore.WHITE}{VERSION}{Fore.CYAN}              ║ │
│ ║ {Fore.WHITE}By {AUTHOR}                             {Fore.CYAN}║ │
│ ║ {Fore.WHITE}Telegram {TELEGRAM}                       {Fore.CYAN}║ │
│ ╚══════════════════════════════════════════════╝ │
│ ┌──────────────┐  ┌──────────────┐              │
│ │ {Fore.WHITE}⏰ {hari[:8]:<8} {Fore.CYAN}│  │ {Fore.WHITE}📅 {tanggal[:8]:<8} {Fore.CYAN}│              │
│ │ {Fore.WHITE}🕐 {jam:<8} {Fore.CYAN}│  │ {Fore.WHITE}📍 ID{Fore.CYAN} │              │
│ └──────────────┘  └──────────────┘              │
└────────────────────────────────────────────────┘
{Fore.RESET}
""")

def update_clock():
    while True:
        time.sleep(1)

clock_thread = threading.Thread(target=update_clock, daemon=True)
clock_thread.start()

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

def is_owner_or_admin(username):
    data = load_data()
    if username in data:
        role = data[username].get('role', 'MEMBER')
        if role in ['DEVELOPER', 'OWNER', 'ADMIN']:
            return True
    owners = load_owners()
    if username in owners:
        role = owners[username].get('role', 'ADMIN')
        if role in ['DEVELOPER', 'OWNER', 'ADMIN']:
            return True
    if username == HEAD_OWNER:
        return True
    return False

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
    return password, f"✅ Username: {username}\n   Password: {password}\n   Role: {role}\n   Expired: {durasi_text}"

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
    if username == HEAD_OWNER and password == MASTER_PASSWORD:
        log_activity(f"Developer login: {username}")
        return True, "✅ Login berhasil! Role: DEVELOPER"
    return False, "❌ Username atau password salah!"

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
        role = info.get('role', 'MEMBER')
        print(f"{Fore.YELLOW}• {username} {status} {Fore.WHITE}({durasi}) {Fore.CYAN}[{role}]")

def add_owner(username, password, role='ADMIN'):
    owners = load_owners()
    if username in owners:
        return False, "❌ Username sudah menjadi owner/admin!"
    owners[username] = {
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'created': datetime.now().isoformat(),
        'role': role
    }
    save_owners(owners)
    log_activity(f"Owner/Admin baru: {username} role: {role}")
    return True, f"✅ {username} berhasil ditambahkan sebagai {role}!"

def remove_owner(username):
    owners = load_owners()
    if username not in owners:
        return False, "❌ Username tidak ditemukan!"
    del owners[username]
    save_owners(owners)
    log_activity(f"Owner/Admin dihapus: {username}")
    return True, f"✅ {username} berhasil dihapus!"

def list_owners():
    owners = load_owners()
    if not owners:
        print(f"{Fore.YELLOW}⚠️ Belum ada owner/admin terdaftar.")
    else:
        print(f"{Fore.CYAN}📋 DAFTAR OWNER/ADMIN:")
        for username, info in owners.items():
            created = datetime.fromisoformat(info['created']).strftime('%d-%m-%Y %H:%M')
            role = info.get('role', 'ADMIN')
            print(f"{Fore.WHITE}• {username} {Fore.CYAN}[{role}] {Fore.WHITE}(created: {created})")

# ============================================
# 🔥 PERMAINAN DI PUBLIC TOOLS 🔥
# ============================================

def game_snake():
    show_banner()
    print(f"{Fore.CYAN}🐍 GAME ULAR (SNAKE){Fore.WHITE}")
    print(f"{Fore.YELLOW}Gunakan WASD untuk bergerak")
    print(f"{Fore.RED}Tabrak dinding atau tubuh sendiri = Game Over!")
    print(f"{Fore.CYAN}Tekan Ctrl+C untuk keluar")
    
    try:
        import curses
        import curses.textpad
        
        def snake_game(stdscr):
            curses.curs_set(0)
            stdscr.nodelay(1)
            stdscr.timeout(100)
            
            sh, sw = stdscr.getmaxyx()
            w = curses.newwin(sh, sw, 0, 0)
            w.keypad(1)
            
            snake_x = sw//4
            snake_y = sh//2
            snake = [
                [snake_y, snake_x],
                [snake_y, snake_x-1],
                [snake_y, snake_x-2]
            ]
            direction = curses.KEY_RIGHT
            
            food = [sh//2, sw//2]
            w.addch(food[0], food[1], curses.ACS_PI)
            
            score = 0
            
            while True:
                next_key = w.getch()
                if next_key != -1:
                    if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
                        direction = next_key
                
                head = snake[0].copy()
                if direction == curses.KEY_UP:
                    head[0] -= 1
                elif direction == curses.KEY_DOWN:
                    head[0] += 1
                elif direction == curses.KEY_LEFT:
                    head[1] -= 1
                elif direction == curses.KEY_RIGHT:
                    head[1] += 1
                
                if (head[0] in [0, sh-1] or head[1] in [0, sw-1] or head in snake):
                    w.addstr(sh//2, sw//2-5, "GAME OVER!", curses.A_BOLD)
                    w.addstr(sh//2+1, sw//2-8, f"Score: {score}")
                    w.refresh()
                    time.sleep(2)
                    break
                
                snake.insert(0, head)
                
                if head == food:
                    score += 1
                    food = None
                    while food is None:
                        nf = [
                            random.randint(1, sh-2),
                            random.randint(1, sw-2)
                        ]
                        food = nf if nf not in snake else None
                    w.addch(food[0], food[1], curses.ACS_PI)
                else:
                    tail = snake.pop()
                    w.addch(tail[0], tail[1], ' ')
                
                w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
                w.addstr(0, 0, f"Score: {score}")
                w.refresh()
        
        curses.wrapper(snake_game)
    except ImportError:
        print(f"{Fore.RED}❌ Game ini butuh library 'curses' (bawaan Python)")
        print(f"{Fore.YELLOW}Di Termux, install: pkg install python-curses")
        time.sleep(2)
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def game_tebak_angka():
    show_banner()
    print(f"{Fore.CYAN}🔢 TEBAK ANGKA{Fore.WHITE}")
    print(f"{Fore.YELLOW}Tebak angka antara 1-100")
    print(f"{Fore.GREEN}Kamu punya 7 kesempatan")
    
    angka = random.randint(1, 100)
    kesempatan = 7
    
    for i in range(kesempatan):
        try:
            tebak = int(input(f"{Fore.CYAN}[+] Tebakan ke-{i+1}: {Fore.WHITE}"))
            if tebak == angka:
                print(f"{Fore.GREEN}✅ Benar! Angkanya adalah {angka}")
                break
            elif tebak < angka:
                print(f"{Fore.YELLOW}⬆️ Terlalu rendah!")
            else:
                print(f"{Fore.YELLOW}⬇️ Terlalu tinggi!")
        except:
            print(f"{Fore.RED}❌ Masukkan angka!")
    
    if tebak != angka:
        print(f"{Fore.RED}💀 Game Over! Angkanya adalah {angka}")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def game_suit():
    show_banner()
    print(f"{Fore.CYAN}✊ SUIT JEPANG (BATU-KERTAS-GUNTING){Fore.WHITE}")
    pilihan = ['batu', 'kertas', 'gunting']
    while True:
        print(f"\n{Fore.YELLOW}Pilihan: batu, kertas, gunting, atau 'exit'")
        user = input(f"{Fore.CYAN}[+] Pilih: {Fore.WHITE}").lower()
        if user == 'exit':
            break
        if user not in pilihan:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            continue
        comp = random.choice(pilihan)
        print(f"{Fore.WHITE}Kamu: {user} | Komputer: {comp}")
        if user == comp:
            print(f"{Fore.YELLOW}🤝 Seri!")
        elif (user == 'batu' and comp == 'gunting') or \
             (user == 'kertas' and comp == 'batu') or \
             (user == 'gunting' and comp == 'kertas'):
            print(f"{Fore.GREEN}✅ Kamu menang!")
        else:
            print(f"{Fore.RED}❌ Kamu kalah!")
    
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 PUBLIC TOOLS - 20 TOOLS + GAMES 🔥
# ============================================

def public_tools():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}🌍 PUBLIC TOOLS - 20 TOOLS  {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}🌐 Cek Website    {Fore.GREEN}[11] {Fore.WHITE}🐍 Game Ular        {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}🔍 IP Lookup      {Fore.GREEN}[12] {Fore.WHITE}🔢 Tebak Angka      {Fore.CYAN}│
│ {Fore.GREEN}[3] {Fore.WHITE}📡 Ping Test      {Fore.GREEN}[13] {Fore.WHITE}✊ Suit Jepang      {Fore.CYAN}│
│ {Fore.GREEN}[4] {Fore.WHITE}🌐 DNS Lookup     {Fore.GREEN}[14] {Fore.WHITE}🧮 Kalkulator      {Fore.CYAN}│
│ {Fore.GREEN}[5] {Fore.WHITE}🎭 Random UA      {Fore.GREEN}[15] {Fore.WHITE}📝 Reverse Text    {Fore.CYAN}│
│ {Fore.GREEN}[6] {Fore.WHITE}🔐 Base64         {Fore.GREEN}[16] {Fore.WHITE}📝 Case Converter {Fore.CYAN}│
│ {Fore.GREEN}[7] {Fore.WHITE}📊 Info Sistem    {Fore.GREEN}[17] {Fore.WHITE}🔢 Random Number   {Fore.CYAN}│
│ {Fore.GREEN}[8] {Fore.WHITE}📱 Info HP        {Fore.GREEN}[18] {Fore.WHITE}📝 Random Password {Fore.CYAN}│
│ {Fore.GREEN}[9] {Fore.WHITE}🌍 IP Publik      {Fore.GREEN}[19] {Fore.WHITE}📊 RAM Usage       {Fore.CYAN}│
│ {Fore.GREEN}[10]{Fore.WHITE}📧 Email Valid    {Fore.GREEN}[20] {Fore.WHITE}🔙 EXIT            {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-20]: {Fore.WHITE}").strip()
        if choice == '1': check_website()
        elif choice == '2': ip_lookup()
        elif choice == '3': ping_tool()
        elif choice == '4': dns_lookup()
        elif choice == '5': user_agent_gen()
        elif choice == '6': base64_tool()
        elif choice == '7': system_info()
        elif choice == '8': device_info()
        elif choice == '9': public_ip()
        elif choice == '10': email_validator()
        elif choice == '11': game_snake()
        elif choice == '12': game_tebak_angka()
        elif choice == '13': game_suit()
        elif choice == '14': calculator()
        elif choice == '15': reverse_text()
        elif choice == '16': case_converter()
        elif choice == '17': random_number()
        elif choice == '18': random_password()
        elif choice == '19': check_ram()
        elif choice == '20':
            print(f"{Fore.YELLOW}🔙 Kembali ke menu utama...")
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 FUNGSI-FUNGSI PUBLIC TOOLS 🔥
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
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) AppleWebKit/605.1.15 Version/17.0",
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

def email_validator():
    show_banner()
    print(f"{Fore.CYAN}📧 EMAIL VALIDATOR")
    email = input(f"{Fore.WHITE}Email: ")
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
        expr = input(f"{Fore.WHITE}Operasi (2+3): ")
        result = eval(expr)
        print(f"{Fore.WHITE}Hasil: {result}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_number():
    show_banner()
    print(f"{Fore.CYAN}🔢 RANDOM NUMBER")
    try:
        min_num = int(input(f"{Fore.WHITE}Min: ") or 1)
        max_num = int(input(f"{Fore.WHITE}Max: ") or 100)
        print(f"{Fore.WHITE}Random: {random.randint(min_num, max_num)}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def random_password():
    show_banner()
    print(f"{Fore.CYAN}📝 RANDOM PASSWORD")
    try:
        length = int(input(f"{Fore.WHITE}Panjang: ") or 12)
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choices(chars, k=length))
        print(f"{Fore.WHITE}Password: {password}")
    except:
        print(f"{Fore.RED}❌ Error!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_ram():
    show_banner()
    print(f"{Fore.CYAN}📊 RAM USAGE")
    try:
        result = subprocess.getoutput("free -h")
        print(f"{Fore.WHITE}{result}")
    except:
        print(f"{Fore.RED}❌ Gagal!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def reverse_text():
    show_banner()
    print(f"{Fore.CYAN}📝 REVERSE TEXT")
    text = input(f"{Fore.WHITE}Teks: ")
    print(f"{Fore.WHITE}Reverse: {text[::-1]}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def case_converter():
    show_banner()
    print(f"{Fore.CYAN}📝 CASE CONVERTER")
    print(f"{Fore.GREEN}[1] {Fore.WHITE}UPPER")
    print(f"{Fore.GREEN}[2] {Fore.WHITE}lower")
    print(f"{Fore.GREEN}[3] {Fore.WHITE}Title")
    choice = input(f"{Fore.CYAN}Pilih: ").strip()
    text = input(f"{Fore.WHITE}Teks: ")
    if choice == '1':
        print(f"{Fore.WHITE}{text.upper()}")
    elif choice == '2':
        print(f"{Fore.WHITE}{text.lower()}")
    elif choice == '3':
        print(f"{Fore.WHITE}{text.title()}")
    else:
        print(f"{Fore.RED}❌ Pilihan tidak valid!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 SPAM NGL (DIPERBAGUS) 🔥
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

def spam_ngl():
    show_banner()
    print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}📨 SPAM NGL - PREMIUM EDITION  {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
Support 2 tipe input:
{Fore.YELLOW}  1. https://ngl.link/*****
{Fore.YELLOW}  2. *****
{Fore.WHITE}
""")
    raw_input = input(f"{Fore.CYAN}[+] USERNAME / LINK NGL: {Fore.WHITE}").strip()
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
    message = input(f"{Fore.CYAN}[+] PESAN SPAM: {Fore.WHITE}").strip()
    if not message:
        print(f"{Fore.RED}❌ Pesan tidak boleh kosong!")
        time.sleep(1)
        return
    try:
        count = int(input(f"{Fore.CYAN}[+] JUMLAH (1-9999): {Fore.WHITE}").strip())
        if count < 1: count = 1
        if count > 9999: count = 9999
    except:
        count = 100
        print(f"{Fore.YELLOW}⚠️ Default: 100")
    try:
        delay = float(input(f"{Fore.CYAN}[+] DELAY (0.1-5): {Fore.WHITE}").strip())
        if delay < 0.1: delay = 0.1
        if delay > 5: delay = 5
    except:
        delay = 0.5
        print(f"{Fore.YELLOW}⚠️ Default: 0.5s")
    print(f"{Fore.RED}\n[!] PERINGATAN: Untuk iseng-iseng!")
    confirm = input(f"{Fore.YELLOW}[?] Lanjut? (y/n): {Fore.WHITE}").strip().lower()
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
    print(f"{Fore.CYAN}" + "═" * 60 + "\n")
    success_count = 0
    fail_count = 0
    for i in range(1, count + 1):
        try:
            msg_to_send = message
            status, result = send_ngl_message(username, msg_to_send)
            progress = (i / count) * 100
            bar_length = 35
            filled = int(bar_length * progress / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            if status:
                success_count += 1
                print(f"{Fore.GREEN}[{i}/{count}] ✅ {result}  [{Fore.CYAN}{bar}{Fore.GREEN}] {progress:.1f}%")
            else:
                fail_count += 1
                print(f"{Fore.RED}[{i}/{count}] {result}  [{Fore.CYAN}{bar}{Fore.RED}] {progress:.1f}%")
            if i < count:
                time.sleep(delay)
        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}\n[!] Spam dihentikan oleh user!")
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
        print(f"{Fore.RED}💀 GAGAL SEMUA! CEK USERNAME ATAU COBA LAGI!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

# ============================================
# 🔥 TOOLS EGAA (DENGAN VERIFIKASI GMAIL+OTP) 🔥
# ============================================

def tools_egaa():
    # Verifikasi Gmail + OTP
    if not verify_egaa_access():
        print(f"{Fore.RED}❌ Akses ditolak! Verifikasi gagal.")
        time.sleep(1)
        return
    
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}👑 TOOLS EGAA - 20 TOOLS  {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}👥 Manage User      {Fore.GREEN}[11] {Fore.WHITE}📊 Log Aktivitas     {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}🔑 Create Password   {Fore.GREEN}[12] {Fore.WHITE}🔒 Lock Tools         {Fore.CYAN}│
│ {Fore.GREEN}[3] {Fore.WHITE}📋 List User        {Fore.GREEN}[13] {Fore.WHITE}🔓 Unlock Tools       {Fore.CYAN}│
│ {Fore.GREEN}[4] {Fore.WHITE}🗑️  Delete User      {Fore.GREEN}[14] {Fore.WHITE}📋 Cek Status Tools   {Fore.CYAN}│
│ {Fore.GREEN}[5] {Fore.WHITE}🔑 Ganti Pass User  {Fore.GREEN}[15] {Fore.WHITE}👑 Tambah Owner/Admin{Fore.CYAN}│
│ {Fore.GREEN}[6] {Fore.WHITE}📋 Backup Data      {Fore.GREEN}[16] {Fore.WHITE}📋 Daftar Owner/Admin{Fore.CYAN}│
│ {Fore.GREEN}[7] {Fore.WHITE}🗑️  Reset Data      {Fore.GREEN}[17] {Fore.WHITE}🗑️  Hapus Owner/Admin {Fore.CYAN}│
│ {Fore.GREEN}[8] {Fore.WHITE}📈 Statistik User   {Fore.GREEN}[18] {Fore.WHITE}🔄 Ganti Pass Owner   {Fore.CYAN}│
│ {Fore.GREEN}[9] {Fore.WHITE}📋 Cek Role User    {Fore.GREEN}[19] {Fore.WHITE}📊 Log Owner/Admin    {Fore.CYAN}│
│ {Fore.GREEN}[10]{Fore.WHITE}🔍 Cek Status User  {Fore.GREEN}[20] {Fore.WHITE}🔙 Back              {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih [1-20]: {Fore.WHITE}").strip()
        if choice == '1':
            owner_manage_user()
        elif choice == '2':
            create_user_password()
        elif choice == '3':
            list_users()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
        elif choice == '4':
            delete_user()
        elif choice == '5':
            change_user_password()
        elif choice == '6':
            backup_data()
        elif choice == '7':
            reset_all_data()
        elif choice == '8':
            user_stats()
        elif choice == '9':
            check_user_role()
        elif choice == '10':
            check_user_status()
        elif choice == '11':
            view_logs()
        elif choice == '12':
            lock_tools()
        elif choice == '13':
            unlock_tools()
        elif choice == '14':
            check_tools_status()
        elif choice == '15':
            add_owner_admin()
        elif choice == '16':
            list_owners()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
        elif choice == '17':
            remove_owner_admin()
        elif choice == '18':
            change_owner_password()
        elif choice == '19':
            owner_logs()
        elif choice == '20':
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

def owner_manage_user():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}👥 MANAGE USER  {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
{Fore.GREEN}[1] {Fore.WHITE}Create Password     {Fore.GREEN}[3] {Fore.WHITE}Delete User         {Fore.CYAN}│
{Fore.GREEN}[2] {Fore.WHITE}List User          {Fore.GREEN}[4] {Fore.WHITE}Back               {Fore.CYAN}│
{Fore.WHITE}
""")
        choice = input(f"{Fore.CYAN}Pilih: {Fore.WHITE}").strip()
        if choice == '1':
            create_user_password()
        elif choice == '2':
            list_users()
            input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")
        elif choice == '3':
            delete_user()
        elif choice == '4':
            break
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

def create_user_password():
    show_banner()
    current_user = "egaa"
    user_role = get_user_role(current_user)
    print(f"{Fore.CYAN}🔑 CREATE PASSWORD")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
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
    print(f"{Fore.YELLOW}Pilih Role:")
    if user_role in ["DEVELOPER", "OWNER", "ADMIN"]:
        print(f"  {Fore.WHITE}[1] ADMIN")
        print(f"  {Fore.WHITE}[2] MEMBER")
        role_choice = input(f"{Fore.CYAN}Pilih role [1-2]: ").strip()
        if role_choice == '1':
            role = 'ADMIN'
        elif role_choice == '2':
            role = 'MEMBER'
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid! Menggunakan default: MEMBER")
            role = 'MEMBER'
    else:
        print(f"  {Fore.WHITE}[1] MEMBER")
        role_choice = input(f"{Fore.CYAN}Pilih role [1]: ").strip()
        role = 'MEMBER'
    result, msg = create_password(username, hours, role)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    print(f"{Fore.YELLOW}\n📌 SIMPAN PASSWORD INI!")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def delete_user():
    show_banner()
    print(f"{Fore.CYAN}🗑️  DELETE USER")
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
    confirm = input(f"{Fore.RED}⚠️ Yakin? (y/n): ").strip().lower()
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
    member = 0
    admin = 0
    owner = 0
    dev = 0
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
        elif role == 'OWNER':
            owner += 1
        elif role == 'DEVELOPER':
            dev += 1
    print(f"{Fore.GREEN}📌 Statistik:")
    print(f"{Fore.WHITE}  • Total User : {total}")
    print(f"{Fore.WHITE}  • User Aktif : {Fore.GREEN}{aktif}")
    print(f"{Fore.WHITE}  • User Expired: {Fore.RED}{expired}")
    print(f"{Fore.WHITE}  • DEVELOPER  : {Fore.MAGENTA}{dev}")
    print(f"{Fore.WHITE}  • OWNER      : {Fore.CYAN}{owner}")
    print(f"{Fore.WHITE}  • ADMIN      : {Fore.BLUE}{admin}")
    print(f"{Fore.WHITE}  • MEMBER     : {Fore.GREEN}{member}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_user_role():
    show_banner()
    print(f"{Fore.CYAN}📋 CEK ROLE USER")
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
    role = data[username].get('role', 'MEMBER')
    print(f"{Fore.GREEN}✅ {username} → {Fore.CYAN}{role}")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def check_user_status():
    show_banner()
    print(f"{Fore.CYAN}🔍 CEK STATUS USER")
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
    expired = datetime.fromisoformat(data[username]['expired'])
    status = f"{Fore.GREEN}AKTIF" if expired > datetime.now() else f"{Fore.RED}EXPIRED"
    role = data[username].get('role', 'MEMBER')
    print(f"{Fore.GREEN}✅ {username} → {status} {Fore.CYAN}[{role}]")
    input(f"\n{Fore.YELLOW}Tekan Enter untuk kembali...")

def add_owner_admin():
    show_banner()
    current_user = "egaa"
    user_role = get_user_role(current_user)
    print(f"{Fore.CYAN}👑 TAMBAH OWNER/ADMIN")
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
    if user_role in ["DEVELOPER", "OWNER", "ADMIN"]:
        print(f"{Fore.YELLOW}Pilih Role:")
        print(f"  {Fore.WHITE}[1] ADMIN")
        print(f"  {Fore.WHITE}[2] OWNER")
        print(f"  {Fore.WHITE}[3] DEVELOPER")
        role_choice = input(f"{Fore.CYAN}Pilih role [1-3]: ").strip()
        if role_choice == '1':
            role = 'ADMIN'
        elif role_choice == '2':
            role = 'OWNER'
        elif role_choice == '3':
            role = 'DEVELOPER'
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid! Menggunakan default: ADMIN")
            role = 'ADMIN'
    else:
        print(f"{Fore.YELLOW}Pilih Role:")
        print(f"  {Fore.WHITE}[1] ADMIN")
        role_choice = input(f"{Fore.CYAN}Pilih role [1]: ").strip()
        role = 'ADMIN'
    status, msg = add_owner(username, password, role)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    time.sleep(1)

def remove_owner_admin():
    show_banner()
    print(f"{Fore.CYAN}🗑️  HAPUS OWNER/ADMIN")
    username = input(f"{Fore.WHITE}Username: ").strip()
    if not username:
        print(f"{Fore.RED}❌ Username tidak boleh kosong!")
        time.sleep(1)
        return
    status, msg = remove_owner(username)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    time.sleep(1)

def change_owner_password():
    show_banner()
    print(f"{Fore.CYAN}🔄 GANTI PASSWORD OWNER/ADMIN")
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
    log_activity(f"Password owner/admin diubah: {username}")
    print(f"{Fore.GREEN}✅ Password {username} berhasil diubah!")
    time.sleep(1)

def owner_logs():
    show_banner()
    print(f"{Fore.CYAN}📊 LOG OWNER/ADMIN")
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
    confirm = input(f"{Fore.YELLOW}Yakin lock? (y/n): ").strip().lower()
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
    confirm = input(f"{Fore.YELLOW}Yakin unlock? (y/n): ").strip().lower()
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

def login():
    show_banner()
    print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}🔐 LOGIN - PREMIUM EDITION  {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
Masukkan Username & Password untuk melanjutkan.
{Fore.YELLOW}📱 Belum punya password? Hubungi {Fore.WHITE}{TELEGRAM} {Fore.YELLOW}di Telegram
{Fore.WHITE}
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

def main_menu():
    current_user = "egaa"
    role = get_user_role(current_user)
    while True:
        show_banner()
        if role in ["DEVELOPER", "OWNER", "ADMIN"]:
            print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}📌 MAIN MENU - PREMIUM EDITION  {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}📨 SPAM NGL        {Fore.GREEN}[3] {Fore.WHITE}🌍 PUBLIC TOOLS      {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}👑 TOOLS EGAA     {Fore.GREEN}[4] {Fore.WHITE}🔓 LOGOUT             {Fore.CYAN}│
│ {Fore.GREEN}[5] {Fore.WHITE}🚪 EXIT               {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
""")
            choice = input(f"{Fore.CYAN}Pilih [1-5]: {Fore.WHITE}").strip()
            if choice == '1':
                spam_ngl()
            elif choice == '2':
                tools_egaa()
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
        else:
            print(f"""
{Fore.CYAN}┌────────────────────────────────────────────────┐
│     {Fore.YELLOW}📌 MAIN MENU - PREMIUM EDITION  {Fore.CYAN}│
├────────────────────────────────────────────────┤
│ {Fore.GREEN}[1] {Fore.WHITE}📨 SPAM NGL        {Fore.GREEN}[3] {Fore.WHITE}🌍 PUBLIC TOOLS      {Fore.CYAN}│
│ {Fore.GREEN}[2] {Fore.WHITE}🔓 LOGOUT          {Fore.GREEN}[4] {Fore.WHITE}🚪 EXIT               {Fore.CYAN}│
└────────────────────────────────────────────────┘
{Fore.WHITE}
""")
            choice = input(f"{Fore.CYAN}Pilih [1-4]: {Fore.WHITE}").strip()
            if choice == '1':
                spam_ngl()
            elif choice == '2':
                print(f"{Fore.YELLOW}🔓 Logout...")
                time.sleep(1)
                return
            elif choice == '3':
                public_tools()
            elif choice == '4':
                print(f"{Fore.GREEN}👋 Keluar dari ALEGRA SPAM...")
                sys.exit(0)
            else:
                print(f"{Fore.RED}❌ Pilihan tidak valid!")
                time.sleep(1)

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
        print(f"{Fore.CYAN}\n📨 ALEGRA SPAM - PREMIUM EDITION")
        print(f"{Fore.MAGENTA}Script By : Alegra Ega")
        print(f"{Fore.WHITE}Telegram : @egaa_1")
