import math

print("this is to calculate resource block based on the bandwidth")
Tech=input("FR1 or FR2 >").upper()

scs=int(input("enter the subcarrier spacing in kHz >"))
if (scs==15 or scs==30 or scs==60 or scs==120):
	resource_block_width= 12* scs
	print(" resource block width is > %r" % resource_block_width)
else:
	print("invalid input")
	exit()


def calc_guardbw_FR1(scs,channel_bw):
	scsDict = {15:0, 30:1, 60: 2}
	bwdict = {
	5:[242.5, 505, -1],
	10:[312.5, 665, 1010],
	15:[382.5, 645, 990],
	20:[452.5,805,1330],
	25:[522.5,785,1310],
	30:[592.5,945,1290],
	40:[552.5,905,1610],
	50:[692.5,1045,1570],
	60:[-1,825,1530],
	80:[-1,925,1450],
	90:[-1,885,1410],
	100:[-1,845,1370],
	}
	return bwdict[channel_bw][scsDict[scs]]

def calc_guardbw_FR2(scs,channel_bw):
	scsDict = {60:0, 120:1}
	bwdict = {
	50:[1210,1900],
	100:[2450,2420],
	200:[4390,4900],
	400:[-1,9860],
	
	}
	return bwdict[channel_bw][scsDict[scs]]

channel_BW= int(input ("Enter the BW in MHz >"))
if (Tech=="FR1"):
	Guard_BW= calc_guardbw_FR1(scs,channel_BW)
else:
	Guard_BW= calc_guardbw_FR2(scs,channel_BW)

print("the Guard BW is > %r" %Guard_BW)
if Guard_BW== -1:
	print("since the calculated Guard bandwidth is -1 this configuration in not valid please select the correct channel bandwidth ")
	exit()
else :
	Number_Resource_block= ((channel_BW*10**3)-2*Guard_BW)/resource_block_width
	print("The total number of resource block %r" % math.floor(Number_Resource_block))

