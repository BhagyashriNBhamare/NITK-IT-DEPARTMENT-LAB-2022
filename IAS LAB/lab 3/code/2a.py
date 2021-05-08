from scapy.all import *

def main():

   

    pkt = IP(src='200.200.200.200', dst='100.100.110.100')/TCP(sport=81, dport = 400)
    sr1(pkt)


if __name__ == '__main__':
    main()

