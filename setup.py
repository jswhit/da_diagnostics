from distutils.core import setup
short_desc = "utilities for validating cyclde DA with UFS"
setup(
  name = 'ufsda_diagnostics',
  version = '0.1',
  description = short_desc,
  author = 'Jeff Whitaker',
  author_email = 'jeffrey dot s dot whitaker at noaa dot gov',
  url = 'https://github.com/jswhit/da_diagnostics',
  packages = ['ufsda_diagnostics'],
  requires = ['numpy','netCDF4','pygrib']
)








