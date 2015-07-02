#NX-API Learning Lab

##Example

###show version

```bash
$ python/example/show_version.py
```
```
Demonstrate how to obtain the version of one network device.

1. Select a configured device from the inventory.
2. Execute the command and print the output.
3. Print the command syntax and output field descriptions.

Select an appropriate device from those available.
username    password    scheme    hostname       port
----------  ----------  --------  -----------  ------
cisco       cisco       http      172.16.1.73      80

Connected to http://172.16.1.73

Output for command: sh ver
name               value
-----------------  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
kern_uptm_secs     18
kick_file_name     bootflash:///titanium-d1-kickstart.7.2.0.ZD.0.120.bin
loader_ver_str     N/A
module_id          NX-OSv Supervisor Module
kick_tmstmp        03/08/2015 11:04:12
isan_file_name     bootflash:///titanium-d1.7.2.0.ZD.0.120.bin
sys_ver_str        7.2(0)D1(1) [build 7.2(0)ZD(0.120)]
bootflash_size     1582402
kickstart_ver_str  7.2(0)D1(1) [build 7.2(0)ZD(0.120)]
kick_cmpl_time     3/8/2015 1:00:00
chassis_id         NX-OSv Chassis
proc_board_id      TM3E1E2C55B
memory             3064940
kern_uptm_mins     50
cpu_name           QEMU Virtual CPU version 2.0
kern_uptm_hrs      8
isan_tmstmp        03/08/2015 15:34:48
manufacturer       Cisco Systems, Inc.
header_str         Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2015, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained herein are owned by
other third parties and are used and distributed under license.
Some parts of this software are covered under the GNU Public
License. A copy of the license is available at
http://www.gnu.org/licenses/gpl.html.

NX-OSv is a demo version of the Nexus Operating System
isan_cmpl_time     3/8/2015 1:00:00
host_name          nx-osv-1
mem_type           kB
kern_uptm_days     3

Command Reference:

command    syntax
---------  ------------
sh ver     show version

Command Schema Fields:

name                   type      description
---------------------  --------  ------------------------------
kern_uptm_secs         integer   Kernel up time(secs)
kick_file_name         string    Kickstart image file name
num_pnic               integer
install_smu_id+
rr_service             string    Service name causing the reset
TABLE_module_smu_list  keyword   SMUs on module
module_id              string    Module ID
loader_ver_str         string    Loader version
slot0_size             longlong  Slot0 size
kick_tmstmp            string    Kickstart image file timestamp
isan_file_name         string    System image file name
bios_cmpl_time         string    BIOS compile time
bootflash_size         integer   Bootflash size
kickstart_ver_str      string    Kickstart image version
header_str             string    Version header
chassis_id             string    Chassis ID
proc_board_id          string    Processor Board ID
memory                 integer   Memory size
cpu_core_str           string
kern_uptm_mins         integer   Kernel up time(mins)
hdd_size               integer
bios_ver_str           string    BIOS version
kern_uptm_days         integer   Kernel up time(days)
cpu_name               string    CPU name
sys_ver_str            string    System image version
kern_uptm_hrs          integer   Kernel up time(hours)
rr_usecs               integer   Last reset time(secs)
isan_tmstmp            string    System image file timestamp
rr_sys_ver             string    System version on last reset
ucontroller_ver_str    string
rr_reason              string    Last reset reason
manufacturer           string    Manufacturer
rr_ctime               date      Last reset time(date)
install_module_smu_id  string    SMU id
TABLE_module_list      keyword   Modules
num_cores              integer
install_modno          uinteger  Module number
kick_cmpl_time         string    Kickstart image compile time
isan_cmpl_time         string    System image compile time
host_name              string    Device name
mem_type               string    Memory type
TABLE_smu_list         keyword   Active SMU(s)
power_seq_ver_str      string
```
