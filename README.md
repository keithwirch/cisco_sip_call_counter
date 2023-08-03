# cisco_sip_call_counter
No Frills SIP Call Counter for Cisco Routers made in pure python with limited requirements.  Currently only supports SNMPv2 on the standard port of UDP/161.  All output is within the terminal.  No GUI.

Requires Python3.7+ to be installed.

## Setup
```
git clone https://github.com/keithwirch/cisco_sip_call_counter.git
cd cisco_sip_call_counter
! Reccommended to create a python virtual environment
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage
```! Help
$ python cisco_sip_call_counter.py -h
usage: cisco_sip_call_counter.py [-h] -c C -a A [-r R] [-o O] [-t T]

options:
  -h, --help  show this help message and exit
  -c C        SNMPv2 Community String (Required)
  -a A        Address/Domain of router being polled (Required)
  -r R        Graph refresh interval (Default: 3)
  -o O        OID used to grab calls (Default: 1.3.6.1.4.1.9.9.63.1.3.8.1.1.2.2)
  -t T        Set Graph Title (Default: SIP Calls)
  
! Example
python cisco_sip_call_counter.py -c '<community string>' -a '<address/domain of router>'
  ```
![Example Outout](example.png "Title")