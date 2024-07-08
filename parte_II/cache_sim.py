from optparse import OptionParser
import gzip
import sys
from cache2 import *

parser = OptionParser()
parser.add_option("--l1_s", dest="l1_s")
parser.add_option("--l1_a", dest="l1_a")
parser.add_option("--l2", action="store_true", dest="has_l2")
parser.add_option("--l2_s", dest="l2_s")
parser.add_option("--l2_a", dest="l2_a")
parser.add_option("--l3", action="store_true", dest="has_l3")
parser.add_option("--l3_s", dest="l3_s")
parser.add_option("--l3_a", dest="l3_a")
parser.add_option("-b", dest="block_size", default="64")
parser.add_option("-t", dest="TRACE_FILE")

(options, args) = parser.parse_args()

l1_cache = cache(options.l1_s, options.l1_a, options.block_size, 'l')
l2_cache = cache(options.l2_s, options.l2_a, options.block_size, 'l') if options.has_l2 else None
l3_cache = cache(options.l3_s, options.l3_a, options.block_size, 'l') if options.has_l3 else None

path = "../traces/{}.gz".format(options.TRACE_FILE)  

with gzip.open(path, 'rt') as trace_fh:
    for line in trace_fh:
        access_type, hex_str_address = line.split()
        address = int(hex_str_address, 16)
        is_l1_miss = l1_cache.access(access_type, address)
    
        if not is_l1_miss:
            if l2_cache:
                is_l2_miss = l2_cache.access(access_type, address)

                if not is_l2_miss:
                    if l3_cache:
                        l3_cache.access(access_type, address)
                

# Print statistics for each cache
print("L1:")
l1_cache.print_stats()
if l2_cache:
    print("L2:")
    l2_cache.print_stats()
if l3_cache:
    print("L3:")
    l3_cache.print_stats()