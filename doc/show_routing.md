#NX-API Learning Lab

##Example

###show routing

```bash
$ python/example/show_routing.py
```
```
Demonstrate how to obtain routing information of one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh routing
vrf-name-out    addrf    attached    ipprefix          mcast-nhops    ucast-nhops  clientname    hidden    ifname    ipnexthop      metric    pref  stale    stale-label    ubest    unres    uptime        type
--------------  -------  ----------  --------------  -------------  -------------  ------------  --------  --------  -----------  --------  ------  -------  -------------  -------  -------  ------------  ------
default         ipv4     true        10.0.0.4/30                 0              1  direct        false     Eth2/1    10.0.0.6            0       0  false    false          true     false    P3DT9H43M27S
default         ipv4     true        10.0.0.6/32                 0              1  local         false     Eth2/1    10.0.0.6            0       0  false    false          true     false    P3DT9H43M27S
default         ipv4     true        192.168.0.1/32              0              2  local         false     Lo0       192.168.0.1         0       0  false    false          true     false    P3DT9H43M53S
default         ipv4     true        192.168.0.1/32              0              2  direct        false     Lo0       192.168.0.1         0       0  false    false          true     false    P3DT9H43M53S
default         ipv4     false       192.168.0.2/32              0              1  ospf-1        false     Eth2/1    10.0.0.5           41     110  false    false          true     false    P1DT8H21M1S   intra
```
```
Command Reference:

command     syntax
----------  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sh routing  show {routing | ip route} [vrf {<vrf-name> | <vrf-known-name> | <vrf-all>}] [ip | ipv4] [unicast] [topology <topology-name>] [l3vm-info] [rpf] [ <ip-addr> | <hostname> | { <ip-prefix> [{longer-prefixes|shorter-prefixes}] } ] [ { <protocol> [all] } | { next-hop <next-hop> | next-hop-v6 <next-hop-v6> } | { interface <interface> } | { updated { [since <stime> ] [until <utime>] } } ]+ [ summary | detail ] [vrf {<vrf-name> | <vrf-known-name> | <vrf-all>}]

Command Schema Fields:

name               type         description
-----------------  ---------  -------------
addrf              string
pref               integer
TABLE_path         keyword
mcast-nhops        integer
attached           bool
metric             integer
stale-label        bool
tag                integer
clientname         string
TABLE_multicast    keyword
paths              integer
uptime             duration
mpls-vpn           bool
TABLE_vrf          keyword
TABLE_prefix       keyword
mask_len           integer
vrf-name-out       vrf
multicast_paths    integer
ifname             interface
type               string
backup-paths       integer
ubest              bool
TABLE_unicast      keyword
ipnexthop          string
ipprefix           string
best-paths         integer
hidden             bool
count              integer
unres              bool
mcast_clientname   string
TABLE_summary      keyword
ucast_clientname   string
mpls               bool
TABLE_addrf        keyword
mbest              bool
routes             integer
stale              bool
TABLE_route_count  keyword
ucast-nhops        integer
```
