#NX-API Learning Lab

##Example

###show ip interface mgmt 0

```bash
$ python/example/show_ip_interface_mgmt_0.py
```
```
Demonstrate how to obtain the details of a network 'management' interface, on one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh ip int mgmt 0
  upkt-orig    num-maddr    lbyte-recv    mpkt-consumed  proxy-arp    stats-last-reset      upkt-recv    bbyte-sent    upkt-consumed    bpkt-recv  prefix         tag    lbyte-fwd    mpkt-fwd    num-addr    bbyte-consumed    bpkt-consumed    mbyte-recv    upkt-fwd  subnet        bpkt-fwd    bbyte-fwd    mbyte-sent    pref  proto-state    ip-disabled    intf-name      ubyte-fwd    lbyte-sent    upkt-sent    mpkt-recv    mbyte-orig    ubyte-consumed  mrouting      bbyte-recv  port-unreach      ubyte-orig  link-state    lcl-proxy-arp      mbyte-consumed    lpkt-sent    bbyte-orig    ubyte-sent  urpf-mode      ubyte-recv  ip-ls-type      lbyte-consumed  dir-bcast      bpkt-orig    lpkt-recv  admin-state      iod    lpkt-consumed    masklen    lpkt-orig    lpkt-fwd    mpkt-orig    mpkt-sent    mtu    bpkt-sent  icmp-redirect      lbyte-orig    ip-unreach    mbyte-fwd  bcast-addr
-----------  -----------  ------------  ---------------  -----------  ------------------  -----------  ------------  ---------------  -----------  -----------  -----  -----------  ----------  ----------  ----------------  ---------------  ------------  ----------  ----------  ----------  -----------  ------------  ------  -------------  -------------  -----------  -----------  ------------  -----------  -----------  ------------  ----------------  ----------  ------------  --------------  ------------  ------------  ---------------  ----------------  -----------  ------------  ------------  -----------  ------------  ------------  ----------------  -----------  -----------  -----------  -------------  -----  ---------------  ---------  -----------  ----------  -----------  -----------  -----  -----------  ---------------  ------------  ------------  -----------  ---------------
      45804            0             0                0  disabled     never                     31137             0            62274          394  172.16.1.73      0            0           0           1                 0                0        937215           0  172.16.1.0           0            0             0       0  up             FALSE          mgmt0                  0             0        45804         3585             0           4202884  disabled           36248  enabled             58795974  up            disabled                        0            0             0      58795974  none              2101502  none                         0  disabled               0            0  up                 2                0         24            0           0            0            0   1500            0  enabled                     0             0            0  255.255.255.255

Command Reference:
No schema available for command(s): sh ip int mgmt 0
WARNING:root:Swallow error retrieving schema(s) for sh ip int mgmt 0 500 Server Error: Internal Server Error
```
