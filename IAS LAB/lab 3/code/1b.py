from decoder import decode_packet
from utility import extractinfo_acl

from scapy.all import *
a = sniff( filter="host 100.100.100.100",count = 1)



hex_dump = chexdump(a[0], dump=True)

li = hex_dump.split(',')

for i in range(len(li)):
	li[i] = li[i].strip(' ')
	li[i] = li[i][2:]
print(" Packet received   ")
print("     ",a[0],"")
a[0].display()
print(" Decoded Packet...........................................")


source_ip,destination_ip,protocol_number,source_port,destination_port  = decode_packet(li)


f = extractinfo_acl('ACL-File-Lab-Program-3.xlsx',source_ip,source_port,destination_ip,destination_port,1)

print("--------------------------------")
print(f)
print("---------------------------------")


