import sys
import pandas as pd

def extractinfo_acl(path,source_ip,source_port,destination_ip,destination_port,i):
	i=i-1
	dataset = pd.read_excel(path,nrows=5)
	results=[]
	res = 0
	flag=1	
	if(str(dataset.iloc[i]["Source IP"])!="Any"):
		l1 = source_ip.split('.')
		l2 = str(dataset.iloc[i]["Source IP"]).split('.')
		for j in range(len(l1)):
			if(l2[j]!='*' and l2[j]!=l1[j]):
				flag=0
	if(str(dataset.iloc[i]["Destination IP"])!="Any"):
		l1 = destination_ip.split('.')
		l2 = str(dataset.iloc[i]["Destination IP"]).split('.')
		for j in range(len(l1)):
			if(l2[j]!='*' and l2[j]!=l1[j]):
				flag=0
	if(dataset.iloc[i]["Destination Port"]!="Any" and dataset.iloc[i]["Destination Port"]!=destination_port):
		flag=0
	if(dataset.iloc[i]["Source Port"]!="Any" and dataset.iloc[i]["Source Port"]!=source_port):
		flag=0
	if(flag==1 and dataset.iloc[i]["Action"]=="Allow"):
		res=1
	if(flag==0 and dataset.iloc[i]["Action"]=="Deny"):
		res=1


	if(res==1):
		return "Allow"
	else:
		return "Deny"


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
	print("source ip adress: "+source_ip)
	print("destination ip adress: "+dest_ip)
	print("source mac address: "+convert_to_addr(source_mac))
	print("destination mac adress: "+convert_to_addr(dest_mac))



def decode_packet(packet):
	a = packet.split(' ')
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
	
	print("\n Protocol "+p+"\n")
	print(" source mac address: "+addr(source_mac_adress))
	print(" destination mac address: "+addr(dest_mac_adress))
	print(" ethernet version: "+str(int(version_of_ethernet[0],16)) + " "+ str(int(version_of_ethernet[1],16)))
	print(" ip version: "+str(int(ip_version[0],16)))
	print(" length of datagram: "+str(int(str(length_of_the_datagram[0]+length_of_the_datagram[1]),16)))
	print(" total length: "+ str(int(str(total_length[0])+str(total_length[1]),16)))
	print(" time to live: "+str(int(time_to_live,16)))
	print(" protocol field: "+str(int(protocol_field,16)))
	print(" source ip address: "+source_ip_adress)
	print(" destination ip address: "+destination_ip_adress)
	print(" protocol number: "+str(protocol_number))
	print(" source port number :"+ str(int( str( str(source_port_number[0])+str(source_port_number[1])),16)))
	print(" destination port number :"+ str(int( str( str(destination_port_number[0])+str(destination_port_number[1])),16))+"\n")

	destination_port = int( str( str(destination_port_number[0])+str(destination_port_number[1])),16)
	source_port = int( str( str(source_port_number[0])+str(source_port_number[1])),16)




	return source_ip_adress,destination_ip_adress,protocol_number,source_port,destination_port










path=str(sys.argv[1])
# print(path[0])
k=int(path[0])
days_file = open(path,'r')
#print(days_file.read())
data_dump = days_file.read()
a = data_dump.split('\n')


for i in a:
	if(i!=''):
		source_ip_adress,destination_ip_adress,protocol_number,source_port,destination_port=decode_packet(i)
		a = extractinfo_acl('ACL-File.xlsx',source_ip_adress,source_port,destination_ip_adress,destination_port,k)
		print(" Access : "+a)