#!/usr/bin/python
# -*- coding:utf-8 -*-
# yum install libxml2-devel python-devel
# yum install python-setuptools&& easy_install pip
# sudo pip install ovirt-engine-sdk-python
import ovirtsdk4 as sdk
import sys,os,hashlib

# Create hosts file
HOST_FILE="/etc/dnsmasq.hosts"
#HOST_FILE="/root/python/hosts"
if os.path.exists(HOST_FILE):
	pass
else:	
	print("没有发现DNS FILE，将会创建！")
	os.system("touch /etc/dnsmasq.hosts")

# Create a connection to the server:
connection = sdk.Connection(
	url='https://',
	username='',
	password='',
	insecure=True,
	)
if connection =="":
	print("No content with ovirt")
	sys.exit(1)
	
system_service = connection.system_service()
vms_service = system_service.vms_service()
vms = vms_service.list()

SkipList = []
KvmList = []

dnshosts = {}
hosts = []
for vm in vms:
	VmName = vm.name
	if VmName in SkipList:
		continue
	try:
		VmHostName = VmName.split("-", 1)[1]
	except IndexError:
		print VmName+"不符合命名要求，要么填写SkipList，要么修改主机名"
		continue
	
	try:
		str = VmHostName.rindex('-')
	except ValueError:
		print VmName+"不符合命名要求，要么填写SkipList，要么修改主机名"
		continue

	VmIp = "10.1." + VmName.split("-", 1)[0]
	dnshosts[VmHostName]=VmIp

for hostname,ip in dnshosts.items():
	host=ip+" "+hostname+".ad.tuhu.cn"
	hosts.append(host)
for kvmlist in KvmList:
	hosts.append(kvmlist)

f = open(HOST_FILE,"r")
host_before = [line.strip() for line in f.readlines()]
f.close()

if hosts == host_before:
	print("没有发现新的Host，不做任何操作！")
else:
	print("发现新Host，将更新文件，并重启DNS server!")
	f = open(HOST_FILE,'w')
	for i in hosts:
		f.write(i+"\n")
	os.system("systemctl restart dnsmasq")
