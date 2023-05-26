from datetime import datetime as dt
import socket as s
import sys

#Defining Target

def syntax():
    print("""[-] Argument Not Provided
[-] Syntax python portscanner.py <ip> -p <1-1000>
    -p : Mention the Range of ports to Scan
    """)

if len(sys.argv) == 4:
    target = s.gethostbyname(sys.argv[1])
    if '-' in sys.argv[3] and '-p' in sys.argv[2]:
        ports = sys.argv[3].split("-")
        if ports[0].isdigit() and ports[1].isdigit() and int(ports[0]) in range (1,65535) and int(ports[1]) in range(1,65535):
            pass
        else:
            print("[-] Mention Ports Correctly")
            syntax()
            sys.exit(1)

    else:
        ports = [int(sys.argv[3]),int(sys.argv[3])]

else:

    sys.exit()

print('-'*50)
print('[+] Scan started on '+target)
print('[+] Start Time: '+str(dt.now()))
print('-'*50)


try:
    for port in range(int(ports[0]),int(ports[1])):
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        s.setdefaulttimeout(1)
        result = soc.connect_ex((target,port))
        if result == 0:
            print(f'[+] Port {port} is open')
        soc.close()

except s.error:
    print("\n [-] Could not connect to the server")

except s.gaierror:
    print("\n[-] Hostname was not resloved. Provide a valid IP/Hostname")
    sys.exit()

except KeyboardInterrupt:
    print("\n[*] Existing Safely on Demand")
    sys.exit()

