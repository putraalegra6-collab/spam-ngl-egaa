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
from datetime import datetime, timedelta
from colorama import init, Fore, Style, Back

init(autoreset=True)
os.system("clear" if os.name == "posix" else "cls")

# ============================================
# 🔥 KONFIGURASI 🔥
# ============================================

VERSION = "VIP 2.0"
AUTHOR = "Alegra Ega"
TELEGRAM = "@egaa_1"
MASTER_PASSWORD = "9999"  # PERMANEN
ADMIN_PASSWORD = "alegra ega"
DATA_FILE = os.path.expanduser("~/.alegra_vip_data.json")

# ============================================
# 🔥 BANNER 🔥
# ============================================

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════╗
{Fore.RED}║                                                                      ║
{Fore.RED}║  {Fore.YELLOW}    █████╗ ██╗     ███████╗ ██████╗ ██████╗  █████╗     {Fore.MAGENTA} ║
{Fore.RED}║  {Fore.YELLOW}   ██╔══██╗██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗    {Fore.MAGENTA} ║
{Fore.RED}║  {Fore.YELLOW}   ███████║██║     █████╗  ██║  ███╗██████╔╝███████║    {Fore.MAGENTA} ║
{Fore.RED}║  {Fore.YELLOW}   ██╔══██║██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║    {Fore.MAGENTA} ║
{Fore.RED}║  {Fore.YELLOW}   ██║  ██║███████╗███████╗╚██████╔╝██║  ██║██║  ██║    {Fore.MAGENTA} ║
{Fore.RED}║  {Fore.YELLOW}   ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    {Fore.MAGENTA} ║
{Fore.RED}║                                                                      ║
{Fore.RED}║  {Fore.CYAN}   ███████╗██████╗  █████╗ ███╗   ███╗                    {Fore.RED}║
{Fore.RED}║  {Fore.CYAN}   ██╔════╝██╔══██╗██╔══██╗████╗ ████║                    {Fore.RED}║
{Fore.RED}║  {Fore.CYAN}   ███████╗██████╔╝███████║██╔████╔██║                    {Fore.RED}║
{Fore.RED}║  {Fore.CYAN}   ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║                    {Fore.RED}║
{Fore.RED}║  {Fore.CYAN}   ███████║██║     ██║  ██║██║ ╚═╝ ██║                    {Fore.RED}║
{Fore.RED}║  {Fore.CYAN}   ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝                    {Fore.RED}║
{Fore.RED}║                                                                      ║
{Fore.RED}║           {Fore.GREEN}📨 ALEGRA SPAM NGL - {Fore.YELLOW}{VERSION}{Fore.GREEN} 📨              {Fore.RED}║
{Fore.RED}║              {Fore.MAGENTA}Script By : {AUTHOR}                       {Fore.RED}║
{Fore.RED}║              {Fore.CYAN}Telegram : {TELEGRAM}                         {Fore.RED}║
{Fore.RED}╚══════════════════════════════════════════════════════════════════╝
{Fore.RESET}
""")

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
    
    # Cek apakah username sudah punya password aktif
    if username in data:
        expired = datetime.fromisoformat(data[username]['expired'])
        if expired > datetime.now():
            return None, "❌ Username sudah punya password aktif!"
    
    # Generate password unik
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=8))
    
    # Hash password
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    # Set expired
    if duration_hours == 0:
        expired_time = datetime.now() + timedelta(days=365*100)  # Permanen
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
# 🔥 ANIMASI 🔥
# ============================================

def loading_animation():
    chars = "█▓▒░▄▀"
    for i in range(20):
        sys.stdout.write(f"\r{Fore.CYAN}[+] LOADING {chars[i % len(chars)] * 20}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def spam_animation(i, total):
    progress = (i / total) * 100
    bar_length = 40
    filled = int(bar_length * progress / 100)
    bar = f"{Fore.GREEN}█{Fore.RESET}" * filled + f"{Fore.WHITE}░{Fore.RESET}" * (bar_length - filled)
    sys.stdout.write(f"\r{Fore.CYAN}Progress: [{bar}] {progress:.1f}% {Fore.YELLOW}[{i}/{total}]")
    sys.stdout.flush()

# ============================================
# 🔥 FUNGSI SPAM 🔥
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
{Fore.CYAN}║     {Fore.YELLOW}🛠️  TOOLS ADMIN - VIP EDITION  {Fore.CYAN}║
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

# ============================================
# 🔥 LOGIN 🔥
# ============================================

def login():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}🔐 LOGIN - VIP EDITION  {Fore.CYAN}║
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
    
    # Cek master password (9999) - PERMANEN
    if password == MASTER_PASSWORD:
        print(f"{Fore.GREEN}✅ Login berhasil (MASTER)!")
        time.sleep(1)
        return True
    
    status, msg = verify_password(username, password)
    print(f"{Fore.GREEN if '✅' in msg else Fore.RED}{msg}")
    time.sleep(1)
    
    return status

# ============================================
# 🔥 SPAM NGL 🔥
# ============================================

def spam_ngl():
    show_banner()
    print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📨 SPAM NGL - VIP EDITION  {Fore.CYAN}║
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
    
    loading_animation()
    
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
            
            spam_animation(i, count)
            
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
# 🔥 MAIN MENU 🔥
# ============================================

def main_menu():
    while True:
        show_banner()
        print(f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
{Fore.CYAN}║     {Fore.YELLOW}📌 MAIN MENU - VIP EDITION  {Fore.CYAN}║
{Fore.CYAN}╚════════════════════════════════════════════╝
{Fore.RESET}
{Fore.GREEN}[1] {Fore.WHITE}SPAM NGL
{Fore.GREEN}[2] {Fore.WHITE}TOOLS ADMIN
{Fore.GREEN}[3] {Fore.WHITE}LOGOUT
{Fore.GREEN}[4] {Fore.WHITE}EXIT
{Fore.RESET}
""")
        choice = input(f"{Fore.CYAN}Pilih: {Fore.WHITE}").strip()
        
        if choice == '1':
            spam_ngl()
        elif choice == '2':
            tools_admin()
        elif choice == '3':
            print(f"{Fore.YELLOW}🔓 Logout...")
            time.sleep(1)
            return
        elif choice == '4':
            print(f"{Fore.GREEN}👋 Keluar dari ALEGRA SPAM NGL VIP...")
            sys.exit(0)
        else:
            print(f"{Fore.RED}❌ Pilihan tidak valid!")
            time.sleep(1)

# ============================================
# 🔥 MAIN 🔥
# ============================================

def main():
    # Login
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
        print(f"{Fore.CYAN}\n📨 ALEGRA SPAM NGL - VIP EDITION")
        print(f"{Fore.MAGENTA}Script By : Alegra Ega")
        print(f"{Fore.WHITE}Telegram : @egaa_1")
