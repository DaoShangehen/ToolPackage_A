"""import ftplib;
from ColorPrint import *;
import re;
#exit(0);
class FTPToolBox:
	Parameters=None;#Parameters for call class method use 
	@classmethod
	def Init_Parameter(cls,Pars,Regex):
		try:
			cls.Parameters=[];
			MatchObj= re.match(Regex,Pars);
			for i in range(1,len(MatchObj.regs)+1):
				cls.Parameters.append( MathchObj.group(i));
		except:
			return False;
		#MatchObj.group
		return True;
	FTPTB_Variable = {};# this list is for IO data;
	@classmethod
	def NewVar(cls):
		#...
		return True;
	@classmethod
	def Connect(cls):

		if(len(Parameters) <1):
			PrintRed("[-] Connect expected at least 1 arguments ,got 0");
			return False;
		IP= Parameters[0];			
		if(len(Parameters)>=3):
			User = Parameters[1];
			Password = Parameters[2];
		ftpObj = ftplib.FTP(IP);


		#FtpObj = ftplib.FTP(Parameters[]

Re_Cmds={"set[ ]+(.+)":FTPToolBox.NewVar,'connect[ ]+(.+)':FTPToolBox.Connect};
def ftpTB(parameters=None):
	global Re_Cmds;
	import ftpTB;# load module  to this
	
	PrintGreen("=================================");
	PrintGreen("=	fff		 tt		   pp  		=");
	PrintGreen("=	f	   tttttt	   p p		=");
	PrintGreen("= fffff      tt  tt    pp       =");
	PrintGreen("=	f		 tttttt	   p		=");
	PrintGreen("=================================");
	if(parameters != None):
		IP = parameters[0];
		#Need extpand
	while(True):
		Command= raw_input(">");
		#re.match(,Command);
		for k,v in Re_Cmd:
			if(re.match(v,Command)):
				
		#PrintGreen("[+] Cmd:"+Command);
	return False;


if( __name__ == '__main__'):
	ftpTB();
"""

