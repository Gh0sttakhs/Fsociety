import os
import base64
import random
import sys
import time
import json
import urllib.request
import http.server
import socketserver
import threading
import socket

# --- Colors ---
RED = "\033[1;31m"
GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
GRAY = "\033[0;37m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

BANNER_TEXT = r"""
  __              _      _
 / _|___  ___  ___ (_) ___| |_ _   _
| |_/ __|/ _ \/ __|| |/ _ \ __| | | |
|  _\__ \ (_) \__ \| |  __/ |_| |_| |
|_| |___/\___/|___/|_|\___|\__|\__, |
                               |___/
"""

# Global variable για τον server
httpd = None

def clear_screen():
    os.system('clear')

def type_effect(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def boot_animation():
    for _ in range(3):
        clear_screen()
        print(WHITE + BANNER_TEXT + RESET)
        time.sleep(0.4) 
        clear_screen()
        print(RED + BANNER_TEXT + RESET)
        time.sleep(0.4)
    print(RED + "   }-----{+} Fsociety Protocol {+}-----{" + RESET)
    time.sleep(0.5)

def login():
    while True:
        print(f"\n{GRAY}Authentication Required...{RESET}")
        try:
            password = input(f"{RED}Enter Password:{RESET} ")
        except:
            sys.exit()

        if password == "mr.robot":
            clear_screen()
            print(RED + BANNER_TEXT + RESET) 
            print(f"{GREEN}[*] ACCESS GRANTED.{RESET}")
            time.sleep(1)
            print(f"{RED}       We are finally free.{RESET}\n")
            time.sleep(1)
            return True
        else:
            print(f"{RED}[!] ACCESS DENIED.{RESET}")
            time.sleep(0.5)

# --- TOOLS ---

def port_scan(target):
    """Πραγματικό Port Scanner"""
    print(f"{GRAY}Scanning target: {target}...{RESET}")
    print(f"{GRAY}Checking common ports...{RESET}\n")
    
    common_ports = {
        21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS",
        3306: "MYSQL", 8080: "HTTP-PROXY"
    }
    
    found_open = False
    start_time = time.time()
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"{WHITE}Target IP: {target_ip}{RESET}\n")

        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"{GREEN}[+] Port {port:<5} OPEN  --> {service}{RESET}")
                found_open = True
            sock.close()
            
    except socket.gaierror:
        print(f"{RED}[!] Error: Could not resolve hostname.{RESET}")
        return
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Scan Cancelled.{RESET}")
        return

    duration = round(time.time() - start_time, 2)
    print(f"\n{GRAY}Scan completed in {duration}s.{RESET}")
    if not found_open:
        print(f"{RED}[!] No open ports found (or blocked).{RESET}")

# --- TRACKING LOGIC ---

class TrapHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args): return
    def do_GET(self):
        client_ip = self.headers.get('X-Forwarded-For', self.client_address[0])
        user_agent = self.headers.get('User-Agent', 'Unknown Device')
        if "," in client_ip: client_ip = client_ip.split(",")[0]
        print(f"\n{GREEN}[+] TARGET CAUGHT!{RESET}")
        print(f"    {WHITE}Time:{RESET}   {time.strftime('%H:%M:%S')}")
        print(f"    {WHITE}IP:{RESET}     {CYAN}{client_ip}{RESET}")
        print(f"    {WHITE}Device:{RESET} {GRAY}{user_agent}{RESET}")
        print(f"{RED}    Waiting for next victim... (CTRL+C to stop){RESET}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<h1>Error 404 - Page Not Found</h1>")

def start_honeytrap():
    global httpd
    PORT = 8080
    print(f"{RED}[*] INITIALIZING TRAP SERVER...{RESET}")
    try:
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", PORT), TrapHandler)
        thread = threading.Thread(target=httpd.serve_forever)
        thread.daemon = True
        thread.start()
        print(f"{GREEN}[✓] Local Server Active on Port {PORT}{RESET}")
        print(f"\n{WHITE}--- HOW TO GET THE LINK ---{RESET}")
        print(f"1. Open a {RED}NEW SESSION{RESET} (Swipe left -> New Session)")
        print(f"2. Paste this command:")
        print(f"   {CYAN}ssh -R 80:localhost:8080 nokey@localhost.run{RESET}")
        print(f"3. Copy the https link.")
        print(f"{RED}[*] Listening... (Press CTRL+C to stop){RESET}")
        while True:
            try: time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{RED}[!] Stopping Server...{RESET}")
                break
        httpd.shutdown()
        httpd.server_close()
        print(f"{GREEN}[✓] Server Closed.{RESET}")
    except Exception as e: print(f"{RED}[!] Error: Port busy.{RESET}")

def trace_ip(ip):
    print(f"{GRAY}Triangulating target: {ip}...{RESET}")
    time.sleep(1)
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if data['status'] == 'fail': print(f"{RED}[!] Trace Failed.{RESET}")
        else:
            print(f"{GREEN}[+] TARGET LOCATED:{RESET}")
            print(f"    {WHITE}IP:{RESET}      {data.get('query')}")
            print(f"    {WHITE}Country:{RESET} {data.get('country')}")
            print(f"    {WHITE}City:{RESET}    {data.get('city')}")
            print(f"    {WHITE}ISP:{RESET}     {data.get('isp')}")
            print(f"{GREEN}[+] Trace Complete.{RESET}")     
    except: print(f"{RED}[!] Connection Error.{RESET}")

def shorten_url(url):
    print(f"{GRAY}Masking URL stream...{RESET}")
    time.sleep(1)
    if not url.startswith("http"): url = "http://" + url
    api_url = "http://tinyurl.com/api-create.php?url=" + urllib.parse.quote(url)
    try:
        response = urllib.request.urlopen(api_url)
        short_link = response.read().decode('utf-8')
        print(f"{GREEN}[+] URL MASKED:{RESET} {CYAN}{short_link}{RESET}")
    except: print(f"{RED}[!] Error: Could not mask URL.{RESET}")

def print_menu():
    print(f"\n{WHITE}COMMAND LIST:{RESET}")
    # Η νέα σειρά: Trap -> Mask -> Trace -> Scan
    print(f"{RED}trap        {RESET} : Start Trap Server")
    print(f"{RED}mask [url]  {RESET} : Hide URL (TinyURL)")
    print(f"{RED}trace [ip]  {RESET} : Geolocate IP Address")
    print(f"{RED}scan [ip]   {RESET} : Port Scanner")
    print(f"{RED}encrypt     {RESET} : Encrypt message")
    print(f"{RED}decrypt     {RESET} : Decrypt message")
    print(f"{RED}check       {RESET} : Password check")
    print(f"{RED}quote       {RESET} : Wisdom")
    print(f"{RED}clear       {RESET} : Clear screen")
    print(f"{RED}exit        {RESET} : Logout\n")

def main():
    boot_animation()
    login()
    while True:
        try: cmd_input = input(f"{RED}root@fsociety:~${RESET} ").strip()
        except KeyboardInterrupt:
            print(); continue
        except: break
        if not cmd_input: continue
        parts = cmd_input.split()
        command = parts[0].lower()
        args = " ".join(parts[1:])

        if command == "scan":
            if not args: print(f"{GRAY}Usage: scan <ip or domain>{RESET}")
            else: port_scan(args)
        elif command == "trap": start_honeytrap()
        elif command == "encrypt":
            if not args: print(f"{GRAY}Usage: encrypt <text>{RESET}")
            else: print(f"{CYAN}[+] OUTPUT:{RESET} {base64.b64encode(args.encode()).decode()}")
        elif command == "decrypt":
            if not args: print(f"{GRAY}Usage: decrypt <code>{RESET}")
            else:
                try: print(f"{CYAN}[+] MESSAGE:{RESET} {base64.b64decode(args.encode()).decode()}")
                except: print(f"{RED}[!] Error: Invalid Code.{RESET}")
        elif command == "trace":
            if not args: print(f"{GRAY}Usage: trace <ip>{RESET}")
            else: trace_ip(args)
        elif command == "mask":
            if not args: print(f"{GRAY}Usage: mask <url>{RESET}")
            else: shorten_url(args)
        elif command == "check":
            if not args: print(f"{GRAY}Usage: check <password>{RESET}")
            elif len(args) < 8: print(f"{RED}[-] WEAK PASSWORD{RESET}")
            else: print(f"{GREEN}[+] STRONG PASSWORD{RESET}")
        elif command == "quote":
            quotes = ["Control is an illusion.", "Hello friend.", "We are fsociety.", "Money is not real.", "Annihilation is always the answer."]
            type_effect(f"{WHITE}> {random.choice(quotes)}{RESET}")
        elif command == "exit":
            type_effect(f"{RED}Goodbye, friend.{RESET}", speed=0.1)
            time.sleep(0.5); break
        elif command == "help": print_menu()
        elif command == "clear":
            clear_screen(); print(RED + BANNER_TEXT + RESET); print() 
        else: print(f"{GRAY}Unknown command.{RESET}")

if __name__ == "__main__":
    main()
