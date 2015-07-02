#NX-API Learning Lab

##Example

###show ip interface brief

```bash
$ python/example/show_ip_interface_brief.py
```
```
Demonstrate how to obtain a brief description of the network interfaces of one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh ip int br
link-state    proto-state    ip-disabled    intf-name    prefix       admin-state      iod
------------  -------------  -------------  -----------  -----------  -------------  -----
up            up             FALSE          Lo0          192.168.0.1  up                36
up            up             FALSE          Eth2/1       10.0.0.6     up                37

vrf-name-out
--------------
default
default

Command Reference:

command       syntax
------------  ---------------------------------------------------------------------------------------------------------------------------------------------------
sh ip int br  show ip interface { {{brief [include-secondary]} | [<interface>] | [<ip-addr>]} [operational] [vaddr] [vrf {<vrf-name> | <vrf-known-name> | all}] }

Command Schema Fields:

name                     type        description
-----------------------  --------  -------------
lbyte-recv               uinteger
subnet1                  ipaddr
pbr-in                   string
num-maddr                uinteger
ubyte-orig               uinteger
mpkt-consumed            uinteger
proxy-arp                string
prefix1                  ipaddr
stats-last-reset         string
TABLE_intf               keyword
proto-state              string
upkt-consumed            uinteger
bpkt-recv                uinteger
prefix                   ipaddr
tag                      uinteger
mpkt-fwd                 uinteger
num-addr                 uinteger
bbyte-consumed           uinteger
bpkt-consumed            uinteger
admin-state              string
upkt-fwd                 uinteger
lpkt-sent                uinteger
bpkt-fwd                 uinteger
bbyte-fwd                uinteger
mbyte-sent               uinteger
TABLE_vrf                keyword
pref                     uinteger
vrf-name-out             string
ip-disabled              string
intf-name                string
ubyte-fwd                uinteger
lbyte-sent               uinteger
upkt-sent                uinteger
mpkt-recv                uinteger
mbyte-orig               uinteger
ubyte-consumed           uinteger
num-vaddr                uinteger
bbyte-sent               uinteger
bbyte-recv               uinteger
port-unreach             string
unnum-intf               string
link-state               string
lcl-proxy-arp            string
mbyte-consumed           uinteger
maddr                    ipaddr
subnet                   ipaddr
bbyte-orig               uinteger
urpf-mode                enum
masklen                  uinteger
ip-ls-type               enum
lbyte-consumed           uinteger
ubyte-sent               uinteger
bpkt-orig                uinteger
lbyte-fwd                uinteger
upkt-orig                uinteger
upkt-recv                uinteger
masklen1                 uinteger
mbyte-recv               uinteger
iod                      uinteger
lpkt-consumed            uinteger
acl-in                   string
vaddr-client             string
pbr-out                  string
dir-bcast                string
ubyte-recv               uinteger
lpkt-orig                uinteger
lpkt-recv                uinteger
acl-out                  string
vaddr-subnet             ipaddr
mpkt-sent                uinteger
mrouting                 string
urpf-acl                 string
bpkt-sent                uinteger
icmp-redirect            string
lbyte-orig               uinteger
mpkt-orig                uinteger
ip-unreach               string
vaddr-masklen            uinteger
mbyte-fwd                uinteger
bcast-addr               ipaddr
vaddr-prefix             ipaddr
mtu                      uinteger
lpkt-fwd                 uinteger
TABLE_secondary_address  keyword
```
