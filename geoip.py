import pygeoip

_geoip = pygeoip.GeoIP('GeoIP.dat', pygeoip.MMAP_CACHE)

def _safe_geoip_query(method, ip, default=''):
    try:
        return method(ip)
    except:
        return default

def get_country_info(ip):
    country_code = _safe_geoip_query(_geoip.country_code_by_addr, ip)
    country_name = _safe_geoip_query(_geoip.country_name_by_addr, ip)
    return '\t'.join((ip, country_code, country_name))

if __name__ == '__main__':
    import sys

    for ip in sys.stdin:
        print get_country_info(ip.strip())
