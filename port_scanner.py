import socket
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}


def scan_port(target, port):
    """Return True when a TCP connection succeeds."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False


def main():
    print("=" * 50)
    print("        PYTHON TCP PORT SCANNER")
    print("=" * 50)

    target = input("Enter authorized target IP/hostname: ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Could not resolve target.")
        return

    print(f"\nTarget: {target}")
    print(f"IP Address: {target_ip}")
    print(f"Started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    for port, service in COMMON_PORTS.items():
        if scan_port(target_ip, port):
            print(f"[OPEN] {port:<5} {service}")
            open_ports.append((port, service))

    print("-" * 50)
    print(f"Scan completed: {datetime.now()}")
    print(f"Open ports found: {len(open_ports)}")


if __name__ == "__main__":
    main()
