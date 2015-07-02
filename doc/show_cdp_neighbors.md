#NX-API Learning Lab

##Example

###show cdp neighbors

```bash
$ python/example/show_cdp_neighbors.py
```
```
Demonstrate how to discover the network neighbors of one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh cdp ne
capability    device_id      ifindex  intf_id      platform_id           port_id                   ttl
------------  -----------  ---------  -----------  --------------------  ----------------------  -----
router        iosxrv-1     436731904  Ethernet2/1  cisco IOS XRv Series  GigabitEthernet0/0/0/0    179

Command Reference:

command    syntax
---------  -----------------------------------
sh cdp ne  show cdp neighbors [interface <if>]

Command Schema Fields:

name                           type      description
-----------------------------  --------  --------------------------------------
intf_id                        string    Interface Id
TABLE_cdp_neighbor_brief_info  keyword   output of show cdp neighbor - in breif
capability+
platform_id                    string    Platform Id
ttl                            uinteger  Hold Time
ifindex                        uinteger  Interface index
neigh_count                    uinteger  Neighbor Count
port_id                        string    Port Identifier
device_id                      string    System Name (or) Device Identifier
```
