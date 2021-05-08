import sys
from utility import extractinfo_acl

def convert_to_addr(hex_addr):
	ans=""
	for i in range(len(hex_addr)):
		a=int(hex_addr[i],16)
		if(i!=0):
			ans=ans+"."+str(a)
		else:
			ans+=str(a)
	return ans
def addr(hex_addr):
	ans=""
	for i in range(len(hex_addr)):
		if(i!=0):
			ans=ans+"."+str(hex_addr[i])
		else:
			ans+=str(hex_addr[i])
	return ans

def decode_arp(packet):
	a = packet.split(' ')
	source_mac=a[22:28]
	source_ip=convert_to_addr(a[28:32])
	dest_mac=a[32:38]
	dest_ip=convert_to_addr(a[38:42])
	print(" source ip adress: "+source_ip)
	print(" destination ip adress: "+dest_ip)
	print(" source mac address: "+convert_to_addr(source_mac))
	print(" destination mac adress: "+convert_to_addr(dest_mac))



def decode_packet(packet):
	a = packet
	dest_mac_adress = a[:6]
	source_mac_adress = a[6:12]
	version_of_ethernet = a[12:14]
	if(version_of_ethernet[1]=='06'):
		decode_arp(packet)
	ip_version_part = a[14:16]
	#print(ip_version_part)
	ip_version = ip_version_part[0][0]
	#print(ip_version)
	length_of_the_datagram = a[16:18]
	total_length = a[18:20]
	flag_fragment = a[20:22]
	time_to_live = a[22]
	protocol_field = a[23]
	header_checksum = a[24:26]
	source_ip_adress = convert_to_addr(a[26:30])
	destination_ip_adress = convert_to_addr(a[30:34])
	source_port_number = a[34:36]
	destination_port_number = a[36:38]
	protocol_number=int(protocol_field,16)
	p="UDP"
	if protocol_number==6:
		p="TCP"
	
	print(" Protocol : "+p+" ")
	print(" Source mac address: "+addr(source_mac_adress))
	print(" Destination mac address: "+addr(dest_mac_adress))
	print(" Ethernet version: "+str(int(version_of_ethernet[0],16)) + " "+ str(int(version_of_ethernet[1],16)))
	print(" Ip version: "+str(int(ip_version[0],16)))
	print(" Length of datagram: "+str(int(str(length_of_the_datagram[0]+length_of_the_datagram[1]),16)))
	print(" Total length: "+ str(int(str(total_length[0])+str(total_length[1]),16)))
	print(" Time to live: "+str(int(time_to_live,16)))
	print(" Protocol field: "+str(int(protocol_field,16)))
	print(" Source ip address: "+source_ip_adress)
	print(" Destination ip address: "+destination_ip_adress)
	print(" Protocol number: "+str(protocol_number))
	print(" Source port number :"+ str(int( str( str(source_port_number[0])+str(source_port_number[1])),16)))
	print(" Destination port number :"+ str(int( str( str(destination_port_number[0])+str(destination_port_number[1])),16))+" ")

	destination_port = int( str( str(destination_port_number[0])+str(destination_port_number[1])),16)
	source_port = int( str( str(source_port_number[0])+str(source_port_number[1])),16)




	return source_ip_adress,destination_ip_adress,protocol_number,source_port,destination_port









