import pandas as pd

def extractinfo_acl(path,source_ip,source_port,destination_ip,destination_port,i):
	dataset = pd.read_excel(path)
	results=[]
	i=i-1
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
		return "Action : Allow"
	else:
		return "Action : Deny"





