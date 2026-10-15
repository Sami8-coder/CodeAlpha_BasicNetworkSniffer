# CodeAlpha Basic Network Sniffer

This project is developed as a part of the **CodeAlpha Cybersecurity Internship**. It is a command-line network packet sniffing tool written in Python using the `Scapy` library. The script captures live network packets, extracts key header details (such as Source IP, Destination IP, and Protocol type), and displays packet summaries in real-time.

---

## Features
- Captures live network traffic packets.
- Identifies and classifies protocols (TCP, UDP, ICMP, etc.).
- Extracts and displays Source IP and Destination IP addresses.
- Displays payload/packet summaries for security analysis.

---

## Prerequisites & Requirements
- Operating System: Linux (Ubuntu/Debian recommended)
- Python 3.x installed
- Administrator/Root privileges (required for raw socket packet capturing)

---

## Installation & Setup Guide (Linux)

Follow these steps to set up and run the project locally on your Linux machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/Sami8-coder/CodeAlpha_BasicNetworkSniffer.git](https://github.com/Sami8-coder/CodeAlpha_BasicNetworkSniffer.git)
cd CodeAlpha_BasicNetworkSniffer
