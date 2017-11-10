#encoding:utf-8
def PrintRed(Msg):
	print '\033[1;31;40m '+Msg;

def PrintGreen(Msg):
	print '\033[1;32;40m '+Msg;

def PrintYellow(Msg):
	print '\033[1;33;40m '+Msg;


Color = {0x000000:'30',0xff0000:'31',0x00ffff:'33',0x0000ff:'34',0x00ff00:'32'}
BColor ={};
for (key,value) in Color.items() :
	BColor[key] = str( int(value)+10  );


