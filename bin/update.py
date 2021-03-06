#!/usr/bin/python
import hashlib
import os,sys
 
def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash
 
def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash
         


os.system('rm -rf rpz.zone.new')
os.system('wget -O rpz.zone.new "https://raw.githubusercontent.com/zyqf/DNS/master-rpz/named/rpz.zone"')

old = CalcMD5("/usr/local/named/var/rpz.zone")
new = CalcMD5("rpz.zone.new")

if old == new:
	print('nothing can update')

else:
	os.system('')	
	os.system('mv /usr/local/named/var/rpz.zone /usr/local/named/var/rpz.zone.bak')
	os.system('mv rpz.zone.new /usr/local/named/var/rpz.zone')
	os.system('service named restart')	
	print('update have done,thanks!')

