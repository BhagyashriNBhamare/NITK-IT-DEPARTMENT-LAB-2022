from scapy.all import *

def main():

   

    pkt = IP(src='20.20.20.20', dst='200.200.200.200')/TCP(sport=81, dport = 80)
    sr(pkt)


if __name__ == '__main__':
    main()

