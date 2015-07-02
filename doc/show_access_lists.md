#NX-API Learning Lab

##Example

###show access lists

```bash
$ python/example/show_access_lists.py
```
```
Demonstrate how to obtain the access-control-lists (ACLs) of one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh access
acl-name                                  seqno  dest_any      dest_port1_num  dest_port1_str    dest_port_op    permitdeny    proto_str    src_any      src_port1_num  src_port_op    src_port1_str    dest_ip_prefix    dest_ipv6_prefix    icmp_str          icmpv6_str            mac_dest        mac_dest_wild    eth_proto    mac_src         mac_src_wild      proto  ip      src_port2_num    dest_port2_num  ipv6
--------------------------------------  -------  ----------  ----------------  ----------------  --------------  ------------  -----------  ---------  ---------------  -------------  ---------------  ----------------  ------------------  ----------------  --------------------  --------------  ---------------  -----------  --------------  --------------  -------  ----  ---------------  ----------------  ------
copp-system-p-acl-bgp                        10  any                      179  bgp               eq              permit        tcp          any                   1024  gt
copp-system-p-acl-bgp                        20  any                     1024                    gt              permit        tcp          any                    179  eq             bgp
copp-system-p-acl-bgp6                       10  any                      179  bgp               eq              permit        tcp          any                   1024  gt
copp-system-p-acl-bgp6                       20  any                     1024                    gt              permit        tcp          any                    179  eq             bgp
copp-system-p-acl-cts                        10  any                    64999                    eq              permit        tcp          any
copp-system-p-acl-cts                        20  any                                                             permit        tcp          any                  64999  eq
copp-system-p-acl-dhcp                       10  any                                                             permit        udp          any                     68  eq             bootpc
copp-system-p-acl-dhcp                       20  any                       67  bootps            eq              permit        udp          any                     67  neq            bootps
copp-system-p-acl-dhcp-relay-response        10  any                                                             permit        udp          any                     67  eq             bootps
copp-system-p-acl-dhcp-relay-response        20  any                       68  bootpc            eq              permit        udp          any
copp-system-p-acl-dhcp6                      10  any                                                             permit        udp          any                    546  eq
copp-system-p-acl-dhcp6                      20  any                      547                    eq              permit        udp          any                    547  neq
copp-system-p-acl-dhcp6-relay-response       10  any                                                             permit        udp          any                    547  eq
copp-system-p-acl-dhcp6-relay-response       20  any                      546                    eq              permit        udp          any
copp-system-p-acl-eigrp                      10  any                                                             permit        eigrp        any
copp-system-p-acl-eigrp6                     10  any                                                             permit        eigrp        any
copp-system-p-acl-ftp                        10  any                       20  ftp-data          eq              permit        tcp          any
copp-system-p-acl-ftp                        20  any                       21  ftp               eq              permit        tcp          any
copp-system-p-acl-ftp                        30  any                                                             permit        tcp          any                     20  eq             ftp-data
copp-system-p-acl-ftp                        40  any                                                             permit        tcp          any                     21  eq             ftp
copp-system-p-acl-glbp                       10                          3222                    eq              permit        udp          any                   3222  eq                              224.0.0.0/24
copp-system-p-acl-hsrp                       10                          1985                    eq              permit        udp          any                                                         224.0.0.2/32
copp-system-p-acl-hsrp                       20                          1985                    eq              permit        udp          any                                                         224.0.0.102/32
copp-system-p-acl-hsrp6                      10                          2029                    eq              permit        udp          any                                                                           ff02::66/128
copp-system-p-acl-http-response              10  any                     1024                    gt              permit        tcp          any                     80  eq             www
copp-system-p-acl-http-response              20  any                     1024                    gt              permit        tcp          any                    443  eq
copp-system-p-acl-http6-response             10  any                     1024                    gt              permit        tcp          any                     80  eq             www
copp-system-p-acl-http6-response             20  any                     1024                    gt              permit        tcp          any                    443  eq
copp-system-p-acl-icmp                       10  any                                                             permit        icmp         any                                                                                               echo
copp-system-p-acl-icmp                       20  any                                                             permit        icmp         any                                                                                               echo-reply
copp-system-p-acl-icmp6                      10  any                                                             permit        icmp         any                                                                                                                 echo-request
copp-system-p-acl-icmp6                      20  any                                                             permit        icmp         any                                                                                                                 echo-reply
copp-system-p-acl-igmp                       10                                                                  permit        igmp         any                                                         224.0.0.0/3
copp-system-p-acl-lisp                       10  any                     4342                    eq              permit        udp          any
copp-system-p-acl-lisp                       20  any                                                             permit        udp          any                   4342  eq
copp-system-p-acl-lisp6                      10  any                     4342                    eq              permit        udp          any
copp-system-p-acl-lisp6                      20  any                                                             permit        udp          any                   4342  eq
copp-system-p-acl-mac-cdp-udld-vtp           10                                                                  permit                     any                                                                                                                                       0100.0ccc.cccc  0000.0000.0000
copp-system-p-acl-mac-cfsoe                  10                                                                  permit                     any                                                                                                                                       0180.c200.000e  0000.0000.0000   0x8843
copp-system-p-acl-mac-cfsoe                  20                                                                  permit                     any                                                                                                                                       0180.c200.000e  0000.0000.0000
copp-system-p-acl-mac-dot1x                  10                                                                  permit                     any                                                                                                                                       0180.c200.0003  0000.0000.0000   0x888e
copp-system-p-acl-mac-ecp-ack                10                                                                  permit                     any                                                                                                                                       0180.c200.0000  0000.0000.0000   0x8940
copp-system-p-acl-mac-ecp-ack                20  any                                                             permit                                                                                                                                                                                                0x8940       0180.c200.0000  0000.0000.0000
copp-system-p-acl-mac-ecp-ack                30  any                                                             permit                     any                                                                                                                                                                        0x8940
copp-system-p-acl-mac-ecp-req                10                                                                  permit                     any                                                                                                                                       0180.c200.0000  0000.0000.0000   0x8940
copp-system-p-acl-mac-ecp-req                20  any                                                             permit                                                                                                                                                                                                0x8940       0180.c200.0000  0000.0000.0000
copp-system-p-acl-mac-ecp-req                30  any                                                             permit                     any                                                                                                                                                                        0x8940
copp-system-p-acl-mac-fabricpath-isis        10                                                                  permit                     any                                                                                                                                       0180.c200.0041  0000.0000.0000
copp-system-p-acl-mac-fcoe                   10  any                                                             permit                     any                                                                                                                                                                        0x8906
copp-system-p-acl-mac-fcoe                   20  any                                                             permit                     any                                                                                                                                                                        0x8914
copp-system-p-acl-mac-flow-control           10                                                                  permit                     any                                                                                                                                       0180.c200.0001  0000.0000.0000   0x8808
copp-system-p-acl-mac-l2-tunnel              10  any                                                             permit                     any                                                                                                                                                                        0x8840
copp-system-p-acl-mac-l2pt                   10                                                                  permit                     any                                                                                                                                       0100.0ccd.cdd0  0000.0000.0000
copp-system-p-acl-mac-l3-isis                10                                                                  permit                     any                                                                                                                                       0180.c200.0015  0000.0000.0000
copp-system-p-acl-mac-l3-isis                20                                                                  permit                     any                                                                                                                                       0180.c200.0014  0000.0000.0000
copp-system-p-acl-mac-l3-isis                30                                                                  permit                     any                                                                                                                                       0900.2b00.0005  0000.0000.0000
copp-system-p-acl-mac-lacp                   10                                                                  permit                     any                                                                                                                                       0180.c200.0002  0000.0000.0000   0x8809
copp-system-p-acl-mac-lldp                   10                                                                  permit                     any                                                                                                                                       0180.c200.000e  0000.0000.0000   0x88cc
copp-system-p-acl-mac-mvrp                   10                                                                  permit                     any                                                                                                                                       0180.c200.0021  0000.0000.0000   0x88f5
copp-system-p-acl-mac-otv-isis               10                                                                  permit                     any                                                                                                                                       0100.0cdf.dfdf  0000.0000.0000
copp-system-p-acl-mac-sdp-srp                10                                                                  permit                     any                                                                                                                                       0180.c200.000e  0000.0000.0000   0x3401
copp-system-p-acl-mac-stp                    10                                                                  permit                     any                                                                                                                                       0100.0ccc.cccd  0000.0000.0000
copp-system-p-acl-mac-stp                    20                                                                  permit                     any                                                                                                                                       0180.c200.0000  0000.0000.0000
copp-system-p-acl-mac-undesirable            10  any                                                             permit                     any
copp-system-p-acl-mld                        10  any                                                             permit        icmp         any                                                                                                                 mld-query
copp-system-p-acl-mld                        20  any                                                             permit        icmp         any                                                                                                                 mld-report
copp-system-p-acl-mld                        30  any                                                             permit        icmp         any                                                                                                                 mld-reduction
copp-system-p-acl-mld                        40  any                                                             permit        icmp         any                                                                                                                 mldv2
copp-system-p-acl-mpls-ldp                   10  any                      646                    eq              permit        udp          any                    646  eq
copp-system-p-acl-mpls-ldp                   20  any                      646                    eq              permit        tcp          any
copp-system-p-acl-mpls-ldp                   30  any                                                             permit        tcp          any                    646  eq
copp-system-p-acl-mpls-oam                   10  any                     3503                    eq              permit        udp          any
copp-system-p-acl-mpls-rsvp                  10  any                                                             permit                     any                                                                                                                                                                                                                          46
copp-system-p-acl-msdp                       10  any                      639                    eq              permit        tcp          any                   1024  gt
copp-system-p-acl-msdp                       20  any                     1024                    gt              permit        tcp          any                    639  eq
copp-system-p-acl-ndp                        10  any                                                             permit        icmp         any                                                                                                                 router-solicitation
copp-system-p-acl-ndp                        20  any                                                             permit        icmp         any                                                                                                                 router-advertisement
copp-system-p-acl-ndp                        30  any                                                             permit        icmp         any                                                                                                                 redirect
copp-system-p-acl-ndp                        40  any                                                             permit        icmp         any                                                                                                                 nd-ns
copp-system-p-acl-ndp                        50  any                                                             permit        icmp         any                                                                                                                 nd-na
copp-system-p-acl-ntp                        10  any                      123  ntp               eq              permit        udp          any
copp-system-p-acl-ntp                        20  any                                                             permit        udp          any                    123  eq             ntp
copp-system-p-acl-ntp6                       10  any                      123  ntp               eq              permit        udp          any
copp-system-p-acl-ntp6                       20  any                                                             permit        udp          any                    123  eq             ntp
copp-system-p-acl-ospf                       10  any                                                             permit        ospf         any
copp-system-p-acl-ospf6                      10  any                                                             permit                     any                                                                                                                                                                                                                          89
copp-system-p-acl-otv-as                     10  any                     8472                    eq              permit        udp          any
copp-system-p-acl-pim                        10                                                                  permit        pim          any                                                         224.0.0.0/24
copp-system-p-acl-pim                        20  any                      496  pim-auto-rp       eq              permit        udp          any
copp-system-p-acl-pim                        30                                                                  permit                     any                                                         224.0.0.13/32                                                                                                                                                        ip
copp-system-p-acl-pim-mdt-join               10                                                                  permit        udp          any                                                         224.0.0.13/32
copp-system-p-acl-pim-reg                    10  any                                                             permit        pim          any
copp-system-p-acl-pim6                       10                                                                  permit        pim          any                                                                           ff02::d/128
copp-system-p-acl-pim6                       20  any                      496  pim-auto-rp       eq              permit        udp          any
copp-system-p-acl-pim6-reg                   10  any                                                             permit        pim          any
copp-system-p-acl-radius                     10  any                     1812                    eq              permit        udp          any
copp-system-p-acl-radius                     20  any                     1813                    eq              permit        udp          any
copp-system-p-acl-radius                     30  any                     1645                    eq              permit        udp          any
copp-system-p-acl-radius                     40  any                     1646                    eq              permit        udp          any
copp-system-p-acl-radius                     50  any                                                             permit        udp          any                   1812  eq
copp-system-p-acl-radius                     60  any                                                             permit        udp          any                   1813  eq
copp-system-p-acl-radius                     70  any                                                             permit        udp          any                   1645  eq
copp-system-p-acl-radius                     80  any                                                             permit        udp          any                   1646  eq
copp-system-p-acl-radius6                    10  any                     1812                    eq              permit        udp          any
copp-system-p-acl-radius6                    20  any                     1813                    eq              permit        udp          any
copp-system-p-acl-radius6                    30  any                     1645                    eq              permit        udp          any
copp-system-p-acl-radius6                    40  any                     1646                    eq              permit        udp          any
copp-system-p-acl-radius6                    50  any                                                             permit        udp          any                   1812  eq
copp-system-p-acl-radius6                    60  any                                                             permit        udp          any                   1813  eq
copp-system-p-acl-radius6                    70  any                                                             permit        udp          any                   1645  eq
copp-system-p-acl-radius6                    80  any                                                             permit        udp          any                   1646  eq
copp-system-p-acl-rip                        10                           520  rip               eq              permit        udp          any                                                         224.0.0.0/24
copp-system-p-acl-rip6                       10                           521                    eq              permit        udp          any                                                                           ff02::9/64
copp-system-p-acl-rise                       10  any                                                             permit        tcp          any                   8000  range                                                                                                                                                                                                                 8001
copp-system-p-acl-rise-nam-response          10  any                     1024                    gt              permit        tcp          any                  63934  eq
copp-system-p-acl-rise-nam-response          20  any                     1024                    gt              permit        tcp          any                  63936  eq
copp-system-p-acl-rise6                      10  any                                                             permit        tcp          any                   8000  range                                                                                                                                                                                                                 8001
copp-system-p-acl-rise6-nam-response         10  any                     1024                    gt              permit        tcp          any                  63934  eq
copp-system-p-acl-rise6-nam-response         20  any                     1024                    gt              permit        tcp          any                  63936  eq
copp-system-p-acl-sftp                       10  any                      115                    eq              permit        tcp          any
copp-system-p-acl-sftp                       20  any                                                             permit        tcp          any                    115  eq
copp-system-p-acl-smtp-response              10  any                     1024                    gt              permit        tcp          any                     25  eq             smtp
copp-system-p-acl-smtp6-response             10  any                     1024                    gt              permit        tcp          any                     25  eq             smtp
copp-system-p-acl-snmp                       10  any                      161  snmp              eq              permit        udp          any
copp-system-p-acl-snmp                       20  any                      162  snmptrap          eq              permit        udp          any
copp-system-p-acl-snmp                       30  any                      161                    eq              permit        tcp          any
copp-system-p-acl-snmp                       40  any                      162                    eq              permit        tcp          any
copp-system-p-acl-snmp6                      10  any                      161  snmp              eq              permit        udp          any
copp-system-p-acl-snmp6                      20  any                      162  snmptrap          eq              permit        udp          any
copp-system-p-acl-snmp6                      30  any                      161                    eq              permit        tcp          any
copp-system-p-acl-snmp6                      40  any                      162                    eq              permit        tcp          any
copp-system-p-acl-ssh                        10  any                       22                    eq              permit        tcp          any
copp-system-p-acl-ssh                        20  any                                                             permit        tcp          any                     22  eq
copp-system-p-acl-ssh6                       10  any                       22                    eq              permit        tcp          any
copp-system-p-acl-ssh6                       20  any                                                             permit        tcp          any                     22  eq
copp-system-p-acl-tacacs                     10  any                       49  tacacs            eq              permit        tcp          any
copp-system-p-acl-tacacs                     20  any                                                             permit        tcp          any                     49  eq             tacacs
copp-system-p-acl-tacacs6                    10  any                       49  tacacs            eq              permit        tcp          any
copp-system-p-acl-tacacs6                    20  any                                                             permit        tcp          any                     49  eq             tacacs
copp-system-p-acl-telnet                     10  any                       23  telnet            eq              permit        tcp          any
copp-system-p-acl-telnet                     20  any                      107                    eq              permit        tcp          any
copp-system-p-acl-telnet                     30  any                                                             permit        tcp          any                     23  eq             telnet
copp-system-p-acl-telnet                     40  any                                                             permit        tcp          any                    107  eq
copp-system-p-acl-telnet6                    10  any                       23  telnet            eq              permit        tcp          any
copp-system-p-acl-telnet6                    20  any                      107                    eq              permit        tcp          any
copp-system-p-acl-telnet6                    30  any                                                             permit        tcp          any                     23  eq             telnet
copp-system-p-acl-telnet6                    40  any                                                             permit        tcp          any                    107  eq
copp-system-p-acl-tftp                       10  any                       69  tftp              eq              permit        udp          any
copp-system-p-acl-tftp                       20  any                     1758                    eq              permit        udp          any
copp-system-p-acl-tftp                       30  any                                                             permit        udp          any                     69  eq             tftp
copp-system-p-acl-tftp                       40  any                                                             permit        udp          any                   1758  eq
copp-system-p-acl-tftp6                      10  any                       69  tftp              eq              permit        udp          any
copp-system-p-acl-tftp6                      20  any                     1758                    eq              permit        udp          any
copp-system-p-acl-tftp6                      30  any                                                             permit        udp          any                     69  eq             tftp
copp-system-p-acl-tftp6                      40  any                                                             permit        udp          any                   1758  eq
copp-system-p-acl-traceroute                 10  any                                                             permit        icmp         any                                                                                               ttl-exceeded
copp-system-p-acl-traceroute                 20  any                                                             permit        icmp         any                                                                                               port-unreachable
copp-system-p-acl-traceroute                 30  any                    33434                    range           permit        udp          any                                                                                                                                                                                                                                                                33534
copp-system-p-acl-undesirable                10  any                     1434                    eq              permit        udp          any
copp-system-p-acl-vpc                        10  any                     3200                    eq              permit        udp          any
copp-system-p-acl-vrrp                       10                                                                  permit                     any                                                         224.0.0.18/32                                                                                                                                                        ip
copp-system-p-acl-vrrp6                      10                                                                  permit                     any                                                                           ff02::12/128                                                                                                                                                                                ipv6
copp-system-p-acl-wccp                       10  any                     2048                    eq              permit        udp          any                   2048  eq
```
```
Command Reference:

command    syntax
---------  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sh access  show { access-lists [<acl-ip-ipv6-mac-name>] | ip access-lists [<acl-ip-name>] |  mac access-lists [<acl-mac-name>] |  ipv6 access-lists [<acl-ipv6-name>] } [capture session <capture_session>] [<expanded> | <summary> | <private> |<brief>]

Command Schema Fields:

name                    type        description
----------------------  ----------  -----------------------------------
dest_ipv6_mask          ipv6addr    Destination IP mask;
dest_any                enum        DESTAny
dest_port1_num          uinteger    Destination port number;
precedence              uinteger    precedence;
dest_addrgrp            string      Destination address group;
ip                      enum        IP
frag_opt_permit_deny    enum        frag_op_type
timerange               string      Time-range;
actioninfo              string      Action information;
capture_session         uinteger    session id
icmpv6_type             uinteger    ICMP type;
dest_port_op            enum        Destination Port operator
global_capture_session  uinteger    capture session
dest_port2_num          uinteger    Destination port number;
src_ip_mask             ipaddr      Source IP mask;
op_ip_ipv6_mac          enum        IP/IPv6/MAC
icmpv6_code             uinteger    ICMP code;
eth_proto               hex         MAC protocol number
established             enum        ESTABLISHED
icmp_type               uinteger    ICMP type;
dest_ipv6_prefix        ipv6prefix  Destination IPv6 prefix;
log                     enum        Log
TABLE_seqno             keyword     ;
proto                   uinteger    A protocol number
tos                     uinteger    tos;
dest_ip_addr            ipaddr      Destination IP address;
dest_portgrp            string      Destination port group;
dest_ip_prefix          ipprefix    Destination IP prefix;
dest_ip_mask            ipaddr      Destination IP mask;
src_ipv6_mask           ipv6addr    Source IP mask;
tos_str                 string      tos string;
ipv6                    enum        IPV6
TABLE_ip_ipv6_mac       keyword     ;
;
fin                     enum        FIN
mac_src_wild            ethernet    Source MAC mask;
icmp_code               uinteger    ICMP code;
src_port_op             enum        Source Port operator
psh                     enum        PSH
dest_port1_str          string      Destination port name;
acl_name                string      List name
icmp_str                string      ICMP message;
mac_dest                ethernet    Destination MAC address;
seqno                   uinteger    Sequence number
vlan                    integer     VLAN number
cos                     integer     CoS value
dscp                    uinteger    dscp;
igmp_type_str           string      IGMP type String;
action                  enum        Action
mac_dest_wild           ethernet    Destination MAC mask;
statistics              enum        STATISTICS
dest_ipv6_addr          ipv6addr    Destination IP address;
plen2                   uinteger    packet length maximum;
dscp_str                string      dscp string;
src_port2_str           string      Source port name;
rst                     enum        RST
src_ipv6_addr           ipv6addr    Source IP address;
src_port2_num           uinteger    Source port number;
proto_str               string      Protocol name;
fragments               enum        Fragments
plen1                   uinteger    Packet length minimum;
match_count             longlong    Number of packets matching the ACL;
mac_src                 ethernet    Source MAC address;
remark                  string      Remark String;
urg                     enum        URG
icmpv6_str              string      ICMP message;
ack                     enum        ACK
src_portgrp             string      Source port group;
igmp_type               uinteger    IGMP type;
src_addrgrp             string      Source address group;
plen_op                 enum        Source Port operator
src_any                 enum        SRCAny
src_ipv6_prefix         ipv6prefix  Source IPv6 prefix;
syn                     enum        SYN
src_ip_prefix           ipprefix    Source IP prefix;
flow_label              uinteger    IPv6 flow label;
dest_port2_str          string      Destination port name;
eth_proto_str           string      MAC protocol name;
src_port1_str           string      Source port name;
permitdeny              enum        Permit/deny
src_ip_addr             ipaddr      Source IP address;
precedence_str          string      precedence string;
src_port1_num           uinteger    Source port number;
```
