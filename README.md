# TOR and ProxyChain Privacy Tool

This Python script provides a terminal-based privacy tool for users who want to use TOR or proxy chains to protect their identity online. The tool includes interactive features, robust error handling, and a sleek ASCII art branding. It is optimized for efficiency and user experience.

## Features
- **TOR Mode**
  - Automatically connects to the TOR network.
  - Displays your current IP address every 20 seconds.
  - Ensures a stable connection by refreshing the TOR circuit periodically.

- **ProxyChain Mode**
  - Tests a list of proxies provided by the user.
  - Automatically skips failed proxies and tests the next in line.
  - Provides real-time feedback for working and non-working proxies.

- **Interactive Interface**
  - Simple user input to select between modes.
  - ASCII art branding for an engaging terminal experience.

## Prerequisites
Make sure you have the following dependencies installed:

- Python 3.7+
- `stem`
- `colorama`
- `pyfiglet`
- `curl` command-line tool

You can install the required Python packages using pip:
```bash
pip install stem colorama pyfiglet
```

## Usage
1. Clone the repository or copy the script to your local machine.
2. Open a terminal and navigate to the script's directory.
3. Run the script using Python:
   ```bash
   python tor_proxy_tool.py
   ```
4. Follow the on-screen instructions to select a mode:
   - **Option 1**: TOR Mode
     - Connects to the TOR network and periodically displays your IP address.
   - **Option 2**: ProxyChain Mode
     - Prompts you to upload a file containing proxies in `IP:PORT` format and tests each proxy sequentially.

## Example Proxy File Format
Ensure your proxy file follows this format:
```
192.168.1.1:8080
10.0.0.1:3128
203.0.113.5:1080
```

## Features in Detail
### TOR Mode
- Launches a TOR process using `stem`.
- Fetches your IP address through the TOR network using `curl`.
- Signals a new TOR circuit periodically to refresh the IP address.

### ProxyChain Mode
- Reads a list of proxies from a user-provided file.
- Validates the format of each proxy.
- Tests connectivity using `curl`.
- Displays the status of each proxy:
  - **Working**: Shown in green.
  - **Failed**: Shown in red.

### Mode Selection
```plaintext
Select Privacy Mode:
1. TOR Mode
2. ProxyChain Mode
Enter your choice (1 or 2):
```

### TOR Mode Output
```plaintext
Starting TOR...
TOR connected! Monitoring IP changes every 20 seconds.
Connected IP: 185.220.101.1
```

### ProxyChain Mode Output
```plaintext
Enter the path to your proxy list file: proxies.txt
Testing proxy: 192.168.1.1:8080
Working Proxy IP: 203.0.113.45
Testing proxy: 10.0.0.1:3128
Proxy failed: 10.0.0.1:3128
```

## Keyboard Interrupt
You can terminate the program at any time by pressing `CTRL+C`. The program will shut down gracefully.

## Notes
- Ensure the TOR service is installed and properly configured on your system.
- For the best experience, run the script in a terminal that supports ANSI colors.

## License
This project is open-source and available for modification and distribution.

---
Enjoy safe and anonymous browsing with **ZZCODEOFFICIAL Privacy Tool**!

