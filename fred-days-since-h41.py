import fred_days_since_larger_or_smaller

series_names = [
    'WLFN',
    'WLRRAL',
    'TERMT',
    'WLODLL',
    'WDTGAL',
    'WDFOL',
    'WLODL',
    'H41RESH4ENWW',
    'WLDACLC',
    'WLAD',
    'WSHOBL',
    'WSHONBNL',
    'WSHONBIIL',
    'WSHOICL',
    'WSHOFADSL',
    'WSHOMCB',
    'WUPSHO',
    'WUDSHO',
    'WORAL',
    'SWPT',
    'WFCDA',
    'WAOAL',
    'WLCFLPCL',
    'WLCFLSCL',
    'WLCFLSECL',
    'H41RESPPALDJNWW',
    'WLCFOCEL',
    'H41RESPPALDKNWW'
]

df = fred_days_since_larger_or_smaller.update(series_names)

df

# df[['series', 'date', 'value', 'days_since']]

# df[['series', 'realtime_start', 'realtime_end', 'date', 'value', 'value_diff', 'days_since']]