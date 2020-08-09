from p2pool.bitcoin import networks

PARENT = networks.nets['defcoin_testnet']

P2P_PORT = 62466
WORKER_PORT = 15555

SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 150 # shares
SPREAD = 7 # blocks
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1

VERSION_CHECK = lambda v: None
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['testdummy', 'bip65', 'csv', 'segwit', 'hive']) # must run with --allow-obsolete-bitcoind
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 4000000
BLOCK_MAX_WEIGHT = 4000000

BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#p2pool-dfc-alt'

IDENTIFIER = '17b751fd110a4637'.decode('hex')
PREFIX = 'fc962530dd5c11ef'.decode('hex')

PERSIST = False
