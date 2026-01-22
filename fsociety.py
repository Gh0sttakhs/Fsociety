import os
import sys
import time
import random
import string
import socket
import json
import base64
import threading
import urllib.request
import urllib.parse
import http.server
import socketserver

# --- Colors ---
class Colors:
    RED = "\033[38;5;196m"
    GREEN = "\033[38;5;46m"
    WHITE = "\033[38;5;255m"
    GRAY = "\033[38;5;240m"
    CYAN = "\033[38;5;51m"
    YELLOW = "\033[38;5;226m"
    BG_RED = "\033[48;5;196m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# Global variable για τον server
httpd = None

# --- Animation Tools ---
class Anim:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def decrypt_print(text, delay=0.01, color=Colors.WHITE):
        """Εφέ αποκρυπτογράφησης"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        for i in range(len(text) + 1):
            sys.stdout.write(f"\r{color}")
            sys.stdout.write(text[:i])
            if i < len(text):
                sys.stdout.write(random.choice(chars))
            sys.stdout.flush()
            time.sleep(delay)
        print(Colors.RESET)

    @staticmethod
    def loading_bar(task_name, duration=1.5):
        """Μπάρα φόρτωσης"""
        print(f"{Colors.GRAY}[*] {task_name}...{Colors.RESET}")
        width = 30
        for i in range(width + 1):
            percent = int((i / width) * 100)
            bar = "█" * i + "-" * (width - i)
            color = Colors.RED if percent < 90 else Colors.GREEN
            sys.stdout.write(f"\r{Colors.BOLD}{Colors.WHITE}[{color}{bar}{Colors.WHITE}] {percent}%{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(duration / width)
        print("\n")

    @staticmethod
    def matrix_intro():
        Anim.clear()
        width = 60
        columns = [0] * width
        try:
            # Μικρότερη διάρκεια matrix για να μην κουράζει
            for _ in range(40): 
                output = ""
                for i in range(width):
                    if columns[i] == 0:
                        if random.random() < 0.05:
                            columns[i] = random.randint(5, 15)
                    
                    if columns[i] > 0:
                        output += f"{Colors.GREEN}{random.choice('01')}{Colors.RESET}"
                        columns[i] -= 1
                    else:
                        output += " "
                print(output)
                time.sleep(0.03)
        except KeyboardInterrupt:
            pass
        Anim.clear()

    @staticmethod
    def boot_sequence():
        """Fake Linux/Hacker Boot Logs"""
        logs = [
            "Loading KERNEL_V2.4...",
            "Mounting /dev/sda1 [ENCRYPTED]...",
            "Starting generic networking...",
            "Bypassing local firewalls...",
            "Injecting rootkits...",
            "Establishing secure connection...",
            "Masking MAC address...",
            "Initializing Fsociety Protocol..."
        ]
        for log in logs:
            print(f"{Colors.GREEN}[OK]{Colors.RESET} {log}")
            time.sleep(random.uniform(0.05, 0.2))
        time.sleep(0.5)
        Anim.clear()

    @staticmethod
    def print_cool_banner():
        # Το νέο Minimal ASCII Art
        art = r"""
                                                    ▓ ▓█                                                       
                                                 ▓█      ███                                                   
                                                █░      ██████                                                 
                                               █        ███████                                                
                                              ██     ▓██████████                                               
                                             ██   ░     ▓████████                                              
                                             ███░  ▓██████████████                                             
                                             ████▓           ▒████                                             
                                           ███                  ███▒                                           
                                          ██░                     ██                                           
                                          ██                      ██                                           
                                           ██▓                   ██                                            
                                        ░██████                ███████                                         
                                       ███ █████              ██████████░                                      
                                      ██     █ ███           █░  █   ████░                                     
                                    ░███                    █       ██  ██                                     
                                   ███                              █    ██                                    
                                 ███                                     █████                                 
                                ███      █████████████████████████████    █████                                
                               ███ █░    █▓                          █       ████                              
                            ▒████▓       █░                          █       ████                              
                           ████████      ▓▒                          █      ▒ ▓███                             
                          ██    ███████   ▓         █ █████          ▒      ████████                           
        """
        print(Colors.RED + Colors.BOLD + art + Colors.RESET)
        print(f"{Colors.GRAY}          }}-----{{+}} We Are Finally Free {{+}}-----{{{Colors.RESET}\n")

def boot_animation():
    Anim.matrix_intro()
    Anim.boot_sequence() 

def login():
    # Login prompt χωρίς banner ακόμα
    print(f"{Colors.RED}fsociety00.dat loaded.{Colors.RESET}")
    while True:
        print(f"\n{Colors.GRAY}Authentication Required...{Colors.RESET}")
        try:
            password = input(f"{Colors.RED}Enter Password:{Colors.RESET} ")
        except:
            sys.exit()

        if password == "mr.robot":
            Anim.clear()
            # ΤΩΡΑ εμφανίζεται το banner
            Anim.print_cool_banner()
            Anim.loading_bar("DECRYPTING USER DATA", 1)
            Anim.decrypt_print("ACCESS GRANTED. HELLO FRIEND.", color=Colors.GREEN)
            time.sleep(1)
            return True
        else:
            print(f"{Colors.RED}[!] ACCESS DENIED.{Colors.RESET}")
            time.sleep(0.5)

# --- TOOLS ---

def port_scan(target):
    Anim.decrypt_print(f"Scanning target: {target}", color=Colors.GRAY)
    Anim.loading_bar("CHECKING COMMON PORTS", 1.5)
    
    common_ports = {
        21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS",
        3306: "MYSQL", 8080: "HTTP-PROXY"
    }
    
    found_open = False
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"{Colors.WHITE}Target IP: {target_ip}{Colors.RESET}\n")

        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"{Colors.GREEN}[+] Port {port:<5} OPEN  --> {service}{Colors.RESET}")
                found_open = True
            sock.close()
            
    except socket.gaierror:
        print(f"{Colors.RED}[!] Error: Could not resolve hostname.{Colors.RESET}")
        return
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Scan Cancelled.{Colors.RESET}")
        return

    if not found_open:
        print(f"{Colors.RED}[!] No open ports found (or blocked).{Colors.RESET}")

# --- TRACKING LOGIC ---

class TrapHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args): return
    def do_GET(self):
        client_ip = self.headers.get('X-Forwarded-For', self.client_address[0])
        user_agent = self.headers.get('User-Agent', 'Unknown Device')
        if "," in client_ip: client_ip = client_ip.split(",")[0]
        
        print(f"\n{Colors.BG_RED}{Colors.WHITE} [!] TARGET CAUGHT! [!] {Colors.RESET}")
        print(f"    {Colors.WHITE}Time:{Colors.RESET}   {time.strftime('%H:%M:%S')}")
        print(f"    {Colors.WHITE}IP:{Colors.RESET}     {Colors.CYAN}{client_ip}{Colors.RESET}")
        print(f"    {Colors.WHITE}Device:{Colors.RESET} {Colors.GRAY}{user_agent}{Colors.RESET}")
        print(f"{Colors.RED}    Waiting for next victim... (CTRL+C to stop){Colors.RESET}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<h1>Error 404 - Page Not Found</h1>")

def start_honeytrap():
    global httpd
    PORT = 8080
    Anim.loading_bar("INITIALIZING TRAP SERVER", 1)
    try:
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", PORT), TrapHandler)
        thread = threading.Thread(target=httpd.serve_forever)
        thread.daemon = True
        thread.start()
        print(f"{Colors.GREEN}[✓] Local Server Active on Port {PORT}{Colors.RESET}")
        print(f"\n{Colors.WHITE}--- HOW TO GET THE LINK ---{Colors.RESET}")
        print(f"1. Open a {Colors.RED}NEW SESSION{Colors.RESET} (Swipe left -> New Session)")
        print(f"2. Paste this command:")
        print(f"   {Colors.CYAN}ssh -R 80:localhost:8080 nokey@localhost.run{Colors.RESET}")
        print(f"3. Copy the https link.")
        print(f"{Colors.RED}[*] Listening... (Press CTRL+C to stop){Colors.RESET}")
        
        while True:
            try: 
                time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Stopping Server...{Colors.RESET}")
                httpd.shutdown()
                httpd.server_close()
                httpd = None
                print(f"{Colors.GREEN}[✓] Server Closed. Back to menu.{Colors.RESET}")
                break

    except Exception as e: print(f"{Colors.RED}[!] Error: Port busy.{Colors.RESET}")

def trace_ip(ip):
    Anim.decrypt_print(f"Triangulating target: {ip}...", color=Colors.GRAY)
    Anim.loading_bar("CONNECTING TO SATELLITE", 2)
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if data['status'] == 'fail': print(f"{Colors.RED}[!] Trace Failed.{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}[+] TARGET LOCATED:{Colors.RESET}")
            print(f"    {Colors.WHITE}IP:{Colors.RESET}      {data.get('query')}")
            print(f"    {Colors.WHITE}Country:{Colors.RESET} {data.get('country')}")
            print(f"    {Colors.WHITE}City:{Colors.RESET}    {data.get('city')}")
            print(f"    {Colors.WHITE}ISP:{Colors.RESET}     {data.get('isp')}")
            print(f"{Colors.GREEN}[+] Trace Complete.{Colors.RESET}")     
    except: print(f"{Colors.RED}[!] Connection Error.{Colors.RESET}")

def shorten_url(url):
    Anim.loading_bar("MASKING URL STREAM", 1.5)
    if not url.startswith("http"): url = "http://" + url
    api_url = "http://tinyurl.com/api-create.php?url=" + urllib.parse.quote(url)
    try:
        response = urllib.request.urlopen(api_url)
        short_link = response.read().decode('utf-8')
        print(f"{Colors.GREEN}[+] URL MASKED:{Colors.RESET} {Colors.CYAN}{short_link}{Colors.RESET}")
    except: print(f"{Colors.RED}[!] Error: Could not mask URL.{Colors.RESET}")

def print_menu():
    print(f"\n{Colors.WHITE}COMMAND LIST:{Colors.RESET}")
    print(f"{Colors.RED}trap        {Colors.RESET} : Start Trap Server")
    print(f"{Colors.RED}mask [url]  {Colors.RESET} : Hide URL (TinyURL)")
    print(f"{Colors.RED}trace [ip]  {Colors.RESET} : Geolocate IP Address")
    print(f"{Colors.RED}scan [ip]   {Colors.RESET} : Port Scanner")
    print(f"{Colors.RED}encrypt     {Colors.RESET} : Encrypt message")
    print(f"{Colors.RED}decrypt     {Colors.RESET} : Decrypt message")
    print(f"{Colors.RED}check       {Colors.RESET} : Password check")
    print(f"{Colors.RED}quote       {Colors.RESET} : Wisdom")
    print(f"{Colors.RED}clear       {Colors.RESET} : Clear screen")
    print(f"{Colors.RED}exit        {Colors.RESET} : Logout\n")

def main():
    boot_animation()
    login()
    while True:
        try: 
            cmd_input = input(f"{Colors.RED}root@fsociety:~${Colors.RESET} ").strip()
        except KeyboardInterrupt:
            print(); continue
        except: break
        
        if not cmd_input: continue
        parts = cmd_input.split()
        command = parts[0].lower()
        args = " ".join(parts[1:])

        if command == "scan":
            if not args: print(f"{Colors.GRAY}Usage: scan <ip or domain>{Colors.RESET}")
            else: port_scan(args)
        elif command == "trap": start_honeytrap()
        elif command == "encrypt":
            if not args: print(f"{Colors.GRAY}Usage: encrypt <text>{Colors.RESET}")
            else: 
                encoded = base64.b64encode(args.encode()).decode()
                Anim.decrypt_print(f"OUTPUT: {encoded}", color=Colors.CYAN)
        elif command == "decrypt":
            if not args: print(f"{Colors.GRAY}Usage: decrypt <code>{Colors.RESET}")
            else:
                try: 
                    decoded = base64.b64decode(args.encode()).decode()
                    Anim.decrypt_print(f"MESSAGE: {decoded}", color=Colors.CYAN)
                except: print(f"{Colors.RED}[!] Error: Invalid Code.{Colors.RESET}")
        elif command == "trace":
            if not args: print(f"{Colors.GRAY}Usage: trace <ip>{Colors.RESET}")
            else: trace_ip(args)
        elif command == "mask":
            if not args: print(f"{Colors.GRAY}Usage: mask <url>{Colors.RESET}")
            else: shorten_url(args)
        elif command == "check":
            if not args: print(f"{Colors.GRAY}Usage: check <password>{Colors.RESET}")
            elif len(args) < 8: print(f"{Colors.RED}[-] WEAK PASSWORD{Colors.RESET}")
            else: print(f"{Colors.GREEN}[+] STRONG PASSWORD{Colors.RESET}")
        elif command == "quote":
            quotes = ["Control is an illusion.", "Hello friend.", "We are fsociety.", "Money is not real.", "Annihilation is always the answer."]
            Anim.decrypt_print(f"> {random.choice(quotes)}", color=Colors.WHITE)
        elif command == "exit":
            # Purge Effect
            print(f"\n{Colors.RED}[!] INITIATING SYSTEM PURGE...{Colors.RESET}")
            time.sleep(0.5)
            for i in range(101, 0, -5):
                sys.stdout.write(f"\r{Colors.GRAY}Deleting logs... {i}%{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(0.05)
            Anim.clear()
            print(f"{Colors.RED}System Halted.{Colors.RESET}")
            time.sleep(0.5)
            break
        elif command == "help": print_menu()
        elif command == "clear":
            Anim.clear()
            Anim.print_cool_banner()
            print() 
        else: print(f"{Colors.GRAY}Unknown command.{Colors.RESET}")

if __name__ == "__main__":
    main()