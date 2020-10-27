from p2pool.bitcoin import networks

PARENT = networks.nets['defcoin']
P2P_PORT = 1337
WORKER_PORT = 9355
SHARE_PERIOD = 45 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 15 # shares
SPREAD = 42 # blocks
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
VERSION_CHECK = lambda v: None if 160002 <= v else 'Litecoin Cash version out of date. Upgrade to 0.16.0.2 or newer!'
VERSION_WARNING = lambda v: None
BLOCK_MAX_SIZE = 4000000
BLOCK_MAX_WEIGHT = 4000000
BOOTSTRAP_ADDRS = []
BOOTSTRAP_ADDRS = '157.245.252.251 104.37.196.26'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-dfc'
IDENTIFIER = 'b032d5a8c6923410'.decode('hex')
PREFIX = '1389c1ad3ef0b9b5'.decode('hex')
PERSIST = True # SET THIS TO FALSE UNTIL THE SHARE CHAIN IS BOOTSTRAPPED
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 15
NEW_MINIMUM_PROTOCOL_VERSION = 3301