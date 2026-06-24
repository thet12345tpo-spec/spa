import sys
import os

# ANSI color codes
g = "\033[32m"
w = "\033[37m"
r = "\033[31m"

def mock_logo():
    print(f"{g}--- SPA Tool Mock Logo ---{w}")

def mock_run_session(encrypted_str, new_mac):
    print(f"{g}[+] Processing encrypted string: {encrypted_str}")
    print(f"{g}[+] Using MAC address: {new_mac}")
    print(f"{r}[!] Note: The actual processing logic is in a compiled .so file.")
    print(f"{r}[!] The current environment is x86_64, but the .so file is for aarch64 (Android).")

try:
    import m1
except ImportError:
    print(f"{r}[!] Error: Could not import module 'm1'.")
    print(f"{r}[!] The file 'm1.cpython-313-aarch64-linux-android.so' is for Android (aarch64).")
    print(f"{r}[!] You are currently running on {os.uname().machine} with Python {sys.version.split()[0]}.")
    print(f"{w}[*] Using mock functions for demonstration purposes...\n")
    m1 = type('Mock', (), {'Logo': mock_logo, 'run_session': mock_run_session})

if __name__ == "__main__":
    m1.Logo() 
    
    try:
        user_input = input(f"{g}[?] Enter the encrypted string: {w}")
        mac_input = input(f"{g}[?] Enter MAC address (e.g. 24:06:aa:4d:3f:13): {w}")
        
        m1.run_session(encrypted_str=user_input, new_mac=mac_input)
    except KeyboardInterrupt:
        print(f"\n{r}[!] Exiting...")
