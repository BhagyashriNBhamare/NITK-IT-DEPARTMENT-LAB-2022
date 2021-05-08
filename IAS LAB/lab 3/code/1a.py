from scapy.all import *

def main():

   

    pkt = IP(src='20.20.20.20', dst='100.100.100.100')/TCP(sport=11, dport = 80)
    unans, ans = sr(pkt)


if __name__ == '__main__':
    main()

