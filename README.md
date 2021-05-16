Requirements:
=========================
To use P2Pool, you must be running your own local defcoind. It takes a while to sync so get that started first.


Generic:
* defcoind >=1.0.0
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

NOTE: IF USING UBUNTU, USE 16 OR 18. Starting with 20 they removed some of the libs from global, and i was seeing instability with 20 (but that could have just been me). Just a note to make your life easier.

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web python-dev
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install [Python 2.7](http://www.python.org/getit/)
* Install [Twisted](http://twistedmatrix.com/trac/wiki/Downloads)
* Install [Zope.Interface](http://pypi.python.org/pypi/zope.interface/3.8.0)
* Install [python win32 api](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/)
* Install [python win32 api wmi wrapper](https://pypi.python.org/pypi/WMI/#downloads)
* Unzip the files into C:\Python27\Lib\site-packages


Running P2Pool:
=========================

You can run a "private" node to connect your miner(s) to or a public pool.


All
-------------------------
Configuration:
Edit p2pool/networks/defcoin.py by uncommenting WORKER_PORT and BOOTSTRAP_ADDRS for the type of node you want to run. The 3 pool types are as follows. Take note that these hash ranges are an early division and may be modified (feedback welcome).
* pool 0, CPU, <1mh, port 13370 --> CPU miners
* pool 1, USB, 1mh to 50mh, port 13371 --> USB ASIC miners like moonlanders and gridseed
* pool 2, ASIC, >50mh, port 13372 --> big ASIC miners like antminer L3


Now that it is configured, a few definitions for clarity:
* YOURADDR - the address of the wallet of the local defcoind running the pool
* USERNAME - as a miner, your defcoin payout address
* MININGPORT - port to mine to as defined when you chose your configuration
* YOUR_LOCAL_IP - IPv4 of pool computer such as 192.168.1.46
* YOUR_PUBLIC_IP - IPv4 of pool computer such as 135.148.43.187


Run for additional options.

    python run_p2pool.py --help


Example commands for running your miners:
* CPU: ./minerd -a scrypt -o stratum+tcp://IP:MININGPORT -O USERNAME:x
* USB: bfgminer.exe --scrypt -o stratum+tcp://IP:MININGPORT -u USERNAME -p 1,d=128 -S MLD:all --set MLD:clock=600


Private - needs testing so might have errors
-------------------------
For standard configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net defcoin -a YOURADDR -n YOUR_LOCAL_IP --bitcoind-p2p-port 10332

If mining from the pool computer, run your miner program, connecting to 127.0.0.1 on port MININGPORT with USERNAME and any password (x is used commonly).

If mining from another local source, run your miner program, connecting YOUR_LOCAL_IP on port MININGPORT with USERNAME and any password (x is used commonly). Probably need to open firewall on pool computer to MININGPORT.


Public
-------------------------
For standard configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net defcoin -a YOURADDR -n YOUR_PUBLIC_IP --bitcoind-p2p-port 10332

Connecting your miners to YOUR_PUBLIC_IP on port MININGPORT with USERNAME and any password (x is used commonly).

Probably need to open firewall on pool computer to MININGPORT.

If you are behind a NAT, you should enable TCP port forwarding on your router. Forward port MININGPORT to the host running P2Pool.


NOTE: Past experience showed need of opening of ports MININGPORT, 1335, 1337, 10332. All 4 might not need to be open thus this note instead of a firewall rules/port forwarding section, and being listed in todo.



Official wiki:
=========================
https://en.bitcoin.it/wiki/P2Pool


Alternate web frontend:
=========================

    cd ..
    mv web-static web-static.old
    git clone https://github.com/justino/p2pool-ui-punchy web-static
    mv web-static.old web-static/legacy
    cd web-static
    git clone https://github.com/hardcpp/P2PoolExtendedFrontEnd ext

There are multiple alt frontends out there to choose from.


Notes for Defcoin:
=========================
Requirements:
-------------------------
Prepare Defcoin core and edit the config file:

    connect=129.2.164.234:1337
    connect=107.191.119.170:1337
    connect=199.204.211.87:1337
    connect=104.37.196.137:1337
    connect=137.117.89.23:1337
    rpcuser=xxx
    rpcpassword=xxx
    rpcallowip=127.0.0.1
    daemon=1
    server=1
    listen=1
    maxconnections=64
    port=10332
    rpcport=1335

In order to run P2Pool with the Defcoin network, you would need to build and install the
dfc_scrypt module that includes the scrypt proof of work code that Defcoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd defcoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (Microsoft Visual C++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%        # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%        # For visual c++ 2010
    cd defcoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

_Tested on Ubuntu 16 and 18_


License:
=========================
[Available here](COPYING)


TODO:
=========================
* migrate to python 3 (this fork or base p2pool)
* link to whoever's defcoin repo is the main one now
* alt frontends options investigation
* firewall rules - were all 4 needed?
* fix complaint about version being dirty when modifying p2pool/networks/defcoin.py to choose node type. After that is fixed, make sure it doesn't complain if you change the web frontend. Lastly make sure it wont complain by creating a run.sh script.
