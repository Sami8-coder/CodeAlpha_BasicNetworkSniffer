from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        
        proto_name = "OTHER"
        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
        elif proto == 1:
            proto_name = "ICMP"
            
        print(f"[+] Packet: {src_ip} ---> {dst_ip} | Protocol: {proto_name}")
        if packet.payload:
            print(f"    Payload Summary: {packet.summary()}")

def main():
    print("[*] Starting Network Sniffer on Linux...")
    print("[*] Press Ctrl+C to stop sniffing.\n")
    sniff(prn=packet_callback, store=0, count=20)

if __name__ == "__main__":
    main()
