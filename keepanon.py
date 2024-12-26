import os
import time
import stem.process
from stem.control import Controller
from stem import Signal
from colorama import Fore, Style, init
import subprocess
from pyfiglet import figlet_format

# Initialize Colorama for automatic reset of styles
init(autoreset=True)

def ascii_art():
def ascii_art():
    ascii_art =         """
                          _..._      .-'''-.                                     .-'''-.                           _..._                     
                       .-'_..._''.  '   _    \_______                           '   _    \                      .-'_..._''.            .---. 
                     .' .'      './   /` '.   \  ___ `'.        __.....__     /   /` '.   \              .--. .' .'      '..--.        |   | 
                    / .'         .   |     \  '' |--.\  \   .-''         '.  .   |     \  '  _.._    _.._|__|/ .'          |__|        |   | 
                   . '           |   '      |  | |    \  ' /     .-''"'-.  `.|   '      |  .' .._| .' .._.--. '            .--.        |   | 
                   | |           \    \     / /| |     |  /     /________\   \    \     / /| '     | '   |  | |            |  |   __   |   | 
.--------..--------| |            `.   ` ..' / | |     |  |                  |`.   ` ..' __| |__ __| |__ |  | |            |  |.:--.'. |   | 
|____    ||____    . '               '-...-'`  | |     ' .\    .-------------'   '-...-'|__   __|__   __||  . '            |  / |   \ ||   | 
    /   /     /   / \ '.          .            | |___.' /' \    '-.____...---.             | |     | |   |  |\ '.          |  `" __ | ||   | 
  .'   /    .'   /   '. `._____.-'/           /_______.'/   `.             .'              | |     | |   |__| '. `._____.-'|__|.'.''| ||   | 
 /    /___ /    /___   `-.______ /            \_______|/      `''-...... -'                | |     | |          `-.______ /   / /   | |'---' 
|         |         |           `                                                          | |     | |                   `    \ \._,\ '/     
|_________|_________|                                                                      |_|     |_|                         `--'  `"      
    """
    print(ascii_art)

def start_tor():
    """Starts the TOR process and initializes a new TOR circuit."""
    print(Fore.YELLOW + "Starting TOR..." + Style.RESET_ALL)
    tor_process = stem.process.launch_tor_with_config(config={
        'SocksPort': '9050',
    })
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    return tor_process

def get_ip_via_tor():
    """Fetches the current IP address using TOR."""
    try:
        response = subprocess.check_output([
            "curl", "--socks5", "127.0.0.1:9050", "https://check.torproject.org/api/ip"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return response
    except subprocess.CalledProcessError:
        return None

def tor_mode():
    """Executes the TOR mode, displaying the IP address every 20 seconds."""
    tor_process = start_tor()
    try:
        print(Fore.GREEN + "TOR connected! Monitoring IP changes every 20 seconds." + Style.RESET_ALL)
        while True:
            ip = get_ip_via_tor()
            if ip:
                print(Fore.GREEN + f"Connected IP: {ip}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Unable to fetch IP through TOR." + Style.RESET_ALL)
            time.sleep(20)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "Shutting down TOR..." + Style.RESET_ALL)
        tor_process.kill()

def validate_proxy_format(proxy):
    """Validates the proxy format (IP:Port)."""
    proxy_parts = proxy.split(':')
    return len(proxy_parts) == 2

def proxychain_mode():
    """Executes the ProxyChain mode by testing proxies from a file."""
    proxy_file = input(Fore.CYAN + "Enter the path to your proxy list file: " + Style.RESET_ALL)
    if not os.path.exists(proxy_file):
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        return

    with open(proxy_file, 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

    if not proxies:
        print(Fore.RED + "No proxies found in the file!" + Style.RESET_ALL)
        return

    for proxy in proxies:
        if not validate_proxy_format(proxy):
            print(Fore.RED + f"Invalid proxy format: {proxy}" + Style.RESET_ALL)
            continue

        ip, port = proxy.split(':')
        try:
            print(Fore.YELLOW + f"Testing proxy: {proxy}" + Style.RESET_ALL)
            response = subprocess.check_output([
                "curl", "--proxy", f"{ip}:{port}", "https://check.torproject.org/api/ip"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
            print(Fore.GREEN + f"Working Proxy IP: {response}" + Style.RESET_ALL)
        except subprocess.CalledProcessError:
            print(Fore.RED + f"Proxy failed: {proxy}" + Style.RESET_ALL)

def main():
    """Main function to handle user choice and execute corresponding mode."""
    display_ascii_art()
    print(Fore.CYAN + "Select Privacy Mode:" + Style.RESET_ALL)
    print("1. TOR Mode")
    print("2. ProxyChain Mode")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        tor_mode()
    elif choice == "2":
        proxychain_mode()
    else:
        print(Fore.RED + "Invalid choice. Exiting." + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProgram terminated by user." + Style.RESET_ALL)
