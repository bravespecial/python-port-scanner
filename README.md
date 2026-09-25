# 🔐 Python TCP Port Scanner

A beginner-friendly cybersecurity project that uses Python socket programming to identify commonly used TCP ports that are accessible on an authorized target.

## 🎯 Project Objective

The purpose of this project is to understand basic network reconnaissance and how exposed network services can be identified through TCP connections.

## 🛠️ Technologies

- Python 3
- Socket Programming
- TCP/IP
- Kali Linux / Linux

## 🔎 Features

- Accepts an IP address or hostname
- Resolves hostnames to IP addresses
- Scans commonly used TCP ports
- Identifies open ports
- Displays commonly associated services
- Includes basic error handling
- Records scan start and completion times

## 📋 Ports Tested

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 139 | NetBIOS |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-port-scanner.git
cd python-port-scanner
python3 port_scanner.py
```

Enter a target that you own or have explicit permission to test.

## 💻 Example

```text
==================================================
        PYTHON TCP PORT SCANNER
==================================================

Enter authorized target IP/hostname: 127.0.0.1

Target: 127.0.0.1
IP Address: 127.0.0.1
--------------------------------------------------
[OPEN] 22    SSH
[OPEN] 80    HTTP
[OPEN] 443   HTTPS
--------------------------------------------------
Open ports found: 3
```

## 🧠 What I Learned

Through this project, I practiced:

- Python socket programming
- TCP connections
- Network ports and services
- Basic network reconnaissance
- Error handling
- Security considerations around exposed services

## ⚠️ Ethical Use

This tool is intended for educational purposes and authorized security testing only.

Do not scan systems, networks, or devices without permission.

## 👩🏽‍💻 Author

**Onajite Joy Efeghaje**

Cybersecurity | Ethical Hacking | Python
