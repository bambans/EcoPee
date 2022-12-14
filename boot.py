print('Booting...')

from esp import osdebug
osdebug(None)

from gc import collect
collect()
