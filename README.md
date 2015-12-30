# pysvr_framework
a network service framwork in python based on eventlet

svrfmw.py         #framwork main file,its an entrance of the framework

Module_Table.py   #module list file,used by svrfmw.py,json format,number is the trade code

Print.py          #Print service file

SqlSvr.py         #SQL service file,sqlite database

client.py         #single-process test client

tt.py             #multi-process test client

test.db           #sqlite database file used by SqlSvr.py


###################################################################

Before start the framework,eventlet module should be installed,use "pip install eventlet" to install the module.

Print service and SQL service are the example,you could develop your own service in the framework.

type "python svrfmw.py" to start the framework.

