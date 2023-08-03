import argparse
import plotext as plt
from pysnmp.hlapi import *
from datetime import datetime
from time import sleep

def get_snmpv2_call_legs(community, host, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community, mpModel=1),  # SNMPv2c
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print("Error: %s" % errorIndication)
    elif errorStatus:
        print("Error: %s at %s" % (errorStatus.prettyPrint(),
                                   errorIndex and varBinds[int(errorIndex) - 1][0] or "?"))
    else:
        for varBind in varBinds:
            # Each call has two legs.  Divide by 2 to get the actual calls.
            return (int(varBind[1]) / 2 )



if __name__ == "__main__":
    # Build Arg Parsing
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', help='SNMPv2 Community String (Required)', required=True, type=str)
    parser.add_argument('-a', help='Address/Domain of router being polled (Required)', required=True, type=str)
    parser.add_argument('-r', help='Graph refresh interval (Default: 3)', default=3, required=False, type=int)
    parser.add_argument('-o', help='OID used to grab calls (Default: 1.3.6.1.4.1.9.9.63.1.3.8.1.1.2.2)', default='1.3.6.1.4.1.9.9.63.1.3.8.1.1.2.2', required=False, type=str)
    parser.add_argument('-t', help='Set Graph Title (Default: SIP Calls)', default='SIP Calls', required=False)

    args = parser.parse_args()

    data = []  # Holds data returned from SNMP Get
    times = []  # Hold timestamps for fetching

    while True:
        try:
            data.append(get_snmpv2_call_legs(args.c, args.a, args.o))  # Get the SNMP value
            times.append(datetime.now().strftime("%H:%M:%S"))  # Collect a list of strings for time format
            end = plt.today_datetime()

            # Build the graph
            plt.clf()
            plt.date_form("H:M:S")
            plt.title(args.t)
            plt.plot(times, data)
            plt.show()

            # Refresh the graph an interval
            sleep(args.r)
        except KeyboardInterrupt:
            print('Exiting, Keyboard Interrupt')
            exit()