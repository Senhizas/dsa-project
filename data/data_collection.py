import vectorbt as vbt
import sys

#symbol = 'BTCUSDT'
interval = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
coins_list = ['1INCHUSDT', 'AAVEUSDT', 'ACAUSDT', 'ACHUSDT', 'ACMUSDT', 'ADAUSDT', 'ADXUSDT', 'AGLDUSDT', 'AIONUSDT', 'AKROUSDT', 'ALCXUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPACAUSDT', 'ALPHAUSDT', 'ALPINEUSDT', 'AMPUSDT', 'ANCUSDT', 'ANKRUSDT', 'ANTUSDT', 'APEUSDT', 'API3USDT', 'ARUSDT', 'ARDRUSDT', 'ARPAUSDT', 'ASRUSDT', 'ASTRUSDT', 'ATAUSDT', 'ATMUSDT', 'ATOMUSDT', 'AUCTIONUSDT', 'AUDUSDT', 'AUDIOUSDT', 'AUTOUSDT', 'AVAUSDT', 'AVAXUSDT', 'AXSUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANDUSDT', 'BARUSDT', 'BATUSDT', 'BCHUSDT', 'BEAMUSDT', 'BELUSDT', 'BETAUSDT', 'BICOUSDT', 'BIFIUSDT', 'BLZUSDT', 'BNBUSDT', 'BNTUSDT', 'BNXUSDT', 'BONDUSDT', 'BSWUSDT', 'BTCUSDT', 'BTCSTUSDT', 'BTGUSDT', 'BTSUSDT', 'BURGERUSDT', 'C98USDT', 'CAKEUSDT', 'CELOUSDT', 'CELRUSDT', 'CFXUSDT', 'CHESSUSDT', 'CHRUSDT', 'CHZUSDT', 'CITYUSDT', 'CKBUSDT', 'CLVUSDT', 'COCOSUSDT', 'COMPUSDT', 'COSUSDT', 'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CTXCUSDT', 'CVCUSDT', 'CVPUSDT', 'CVXUSDT', 'DARUSDT', 'DASHUSDT', 'DATAUSDT', 'DCRUSDT', 'DEGOUSDT', 'DENTUSDT', 'DEXEUSDT', 'DFUSDT', 'DGBUSDT', 'DIAUSDT', 'DNTUSDT', 'DOCKUSDT', 'DODOUSDT', 'DOGEUSDT', 'DOTUSDT', 'DREPUSDT', 'DUSKUSDT', 'DYDXUSDT', 'EGLDUSDT', 'ELFUSDT', 'ENJUSDT', 'ENSUSDT', 'EOSUSDT', 'EPXUSDT', 'ERNUSDT', 'ETCUSDT', 'ETHUSDT', 'FARMUSDT', 'FETUSDT', 'FIDAUSDT', 'FILUSDT', 'FIOUSDT', 'FIROUSDT', 'FISUSDT', 'FLMUSDT', 'FLOWUSDT', 'FLUXUSDT', 'FORUSDT', 'FORTHUSDT', 'FRONTUSDT', 'FTMUSDT', 'FTTUSDT', 'FUNUSDT', 'FXSUSDT', 'GALUSDT', 'GALAUSDT', 'GBPUSDT', 'GHSTUSDT', 'GLMRUSDT', 'GMTUSDT', 'GNOUSDT', 'GRTUSDT', 'GTCUSDT', 'GTOUSDT', 'HARDUSDT', 'HBARUSDT', 'HIGHUSDT', 'HIVEUSDT', 'HNTUSDT', 'HOTUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'ILVUSDT', 'IMXUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IRISUSDT', 'JASMYUSDT', 'JOEUSDT', 'JSTUSDT', 'JUVUSDT', 'KAVAUSDT', 'KDAUSDT', 'KEYUSDT', 'KLAYUSDT', 'KMDUSDT', 'KNCUSDT', 'KP3RUSDT', 'KSMUSDT', 'LAZIOUSDT', 'LDOUSDT', 'LEVERUSDT', 'LINAUSDT', 'LINKUSDT', 'LITUSDT', 'LOKAUSDT', 'LPTUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCUSDT', 'LTOUSDT', 'LUNAUSDT', 'MANAUSDT', 'MASKUSDT', 'MATICUSDT', 'MBLUSDT', 'MBOXUSDT', 'MCUSDT', 'MDTUSDT', 'MDXUSDT', 'MFTUSDT', 'MINAUSDT', 'MIRUSDT', 'MITHUSDT', 'MKRUSDT', 'MLNUSDT', 'MOBUSDT', 'MOVRUSDT', 'MTLUSDT', 'MULTIUSDT', 'NBSUSDT', 'NBTUSDT', 'NEARUSDT', 'NEOUSDT', 'NEXOUSDT', 'NKNUSDT', 'NMRUSDT', 'NULSUSDT', 'OCEANUSDT', 'OGUSDT', 'OGNUSDT', 'OMUSDT', 'OMGUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'OOKIUSDT', 'OPUSDT', 'ORNUSDT', 'OXTUSDT', 'PAXGUSDT', 'PEOPLEUSDT', 'PERLUSDT', 'PERPUSDT', 'PHAUSDT', 'PLAUSDT', 'PNTUSDT', 'POLSUSDT', 'POLYUSDT', 'PONDUSDT', 'PORTOUSDT', 'POWRUSDT', 'PSGUSDT', 'PUNDIXUSDT', 'PYRUSDT', 'QIUSDT', 'QNTUSDT', 'QTUMUSDT', 'QUICKUSDT', 'RADUSDT', 'RAREUSDT', 'RAYUSDT', 'REEFUSDT', 'REIUSDT', 'RENUSDT', 'REPUSDT', 'REQUSDT', 'RIFUSDT', 'RLCUSDT', 'RNDRUSDT', 'ROSEUSDT', 'RSRUSDT', 'RUNEUSDT', 'RVNUSDT', 'SANDUSDT', 'SANTOSUSDT', 'SCUSDT', 'SCRTUSDT', 'SFPUSDT', 'SHIBUSDT', 'SKLUSDT', 'SLPUSDT', 'SNXUSDT', 'SOLUSDT', 'SPELLUSDT', 'SRMUSDT', 'STEEMUSDT', 'STMXUSDT', 'STORJUSDT', 'STPTUSDT', 'STRAXUSDT', 'STXUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSHIUSDT', 'SXPUSDT', 'SYSUSDT', 'TCTUSDT', 'TFUELUSDT', 'THETAUSDT', 'TKOUSDT', 'TLMUSDT', 'TOMOUSDT', 'TORNUSDT', 'TRBUSDT', 'TRIBEUSDT', 'TROYUSDT', 'TRUUSDT', 'TRXUSDT', 'TVKUSDT', 'TWTUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIUSDT', 'UTKUSDT', 'VETUSDT', 'VGXUSDT', 'VIDTUSDT', 'VITEUSDT', 'VOXELUSDT', 'VTHOUSDT', 'WANUSDT', 'WAVESUSDT', 'WAXPUSDT', 'WINUSDT', 'WINGUSDT', 'WNXMUSDT', 'WOOUSDT', 'WRXUSDT', 'WTCUSDT', 'XECUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XNOUSDT', 'XRPUSDT', 'XTZUSDT', 'XVGUSDT', 'XVSUSDT', 'YFIUSDT', 'YFIIUSDT', 'YGGUSDT', 'ZECUSDT', 'ZENUSDT', 'ZILUSDT', 'ZRXUSDT']
original_stdout = sys.stdout
_edict = {}
_xdata = {}
for x in coins_list:
    for y in interval:
        if y == '1m':
            _start = str(540 * 1)+" minutes ago"
        elif y == '3m':
            _start = str(540 * 3)+" minutes ago"
        elif y == '5m':
            _start = str(540 * 5)+" minutes ago"
        elif y == '15m':
            _start = str(540 * 15)+" minutes ago"
        elif y == '30m':
            _start = str(540 * 30)+" minutes ago"
        elif y == '1h':
            _start = str(540 * 60)+" minutes ago"
        elif y == '2h':
            _start = str(540 * 120)+" minutes ago"
        elif y == '4h':
            _start = str(540 * 240)+" minutes ago"
        elif y == '6h':
            _start = str(540 * 360)+" minutes ago"
        elif y == '8h':
            _start = str(540 * 480)+" minutes ago"
        elif y == '12h':
            _start = str(540 * 720)+" minutes ago"
        elif y == '1d':
            _start = str(540 * 1440)+" minutes ago"
        elif y == '3d':
            _start = str(540 * 4320)+" minutes ago"
        elif y == '1w':
            _start = str(540 * 10080)+" minutes ago"
        elif y == '1M':
            _start = str(540 * 43800)+" minutes ago"

        data_downloaded = vbt.BinanceData.download(x, interval=y, start=_start, end="Now").get()
        _edited = data_downloaded.drop(['Close time', 'Quote volume', 'Number of trades', 'Taker base volume', 'Taker quote volume'], axis=1)
        df = _edited.reset_index(drop=True)
        _open = list(df['Open'])
        _high = list(df['High'])
        _low = list(df['Low'])
        _close = list(df['Close'])
        _volume = list(df['Volume'])
        _data = [_open, _high, _low, _close, _volume]
        fdata = {y: _data}
        _edict.update(fdata)

    xdata = {x: _edict}
    _xdata.update(xdata)

with open(f"data\coins_data.py", "a+") as f:
    sys.stdout = f
    print(f'coins_data = {xdata}')
    sys.stdout = original_stdout

