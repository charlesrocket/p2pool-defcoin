import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

SYMBOL = 'TDFC'
POW_FUNC = data.hash256
BLOCK_PERIOD = 150 # s
ADDRESS_VERSION = 127
SEGWIT_ADDRESS_VERSION = 58
HUMAN_READABLE_PART = 'tdfc'

CONF_FILE_FUNC = lambda: os.path.join(
	os.path.join(os.environ['APPDATA'], 'Defcoin') if platform.system() == 'Windows' else
	os.path.expanduser('~/Library/Application Support/Defcoin/') if platform.system() == 'Darwin' else
	os.path.expanduser('~/.defcoin'),
'defcoin.conf')

P2P_PORT = 62456
P2P_PREFIX = 'b6f5d3cf'.decode('hex')
RPC_PORT = 62455
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
	(yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
))

BLOCK_EXPLORER_URL_PREFIX = 'http://127.0.0.1/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://127.0.0.1/address/'
TX_EXPLORER_URL_PREFIX = 'https://127.0.0.1/tx/'

SUBSIDY_FUNC = lambda height: (
	0 if height <= 101 or height >= 6215968 or height / 840000 >= 64 else
	50*100000000 >> height//840000 if height-101 > 40 else
	(height-100) * ((50*100000000)/40) >> height//840000
)
SUBSIDY_DECIMAL = 1e-7

DUST_THRESHOLD = 0.001e7
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
