#!/usr/bin/python

__author__ = ['[Gerald Sim](https://github.com/meappy)']
__date__ = '2019.03.24'

"""
Set and print MySQL wait_timeout setting
"""

import argparse
import sys
import mysqlstore

sys.dont_write_bytecode = True

db = mysqlstore.connect()

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--timeout', type=int,
                    action="store", dest="timeout",
                    help="set wait_timeout in seconds")

parser.add_argument('-p', '--print',
                    action="store_true", dest='print_',
                    help="print wait_timeout in seconds")

parser.add_argument('-q', '--quiet',
                    action="store_true", dest='quiet',
                    help="suppress output")

def set_wait_timeout(fset_wait_timeout):
    cursor = db.cursor(prepared=True)
    sql_query = """set global wait_timeout=%s"""
    cursor.execute(sql_query, (fset_wait_timeout,))

def return_wait_timeout():
    cursor = db.cursor()
    cursor.execute("select @@global.wait_timeout")
    for row in cursor.fetchall():
        return row[0]

# Print -h if no args supplied, needs to be before parser.parse_args()
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

args = parser.parse_args()

if args.quiet and args.timeout:
    set_wait_timeout(args.timeout)
elif args.timeout:
    set_wait_timeout(args.timeout)
    print 'New wait_timeout:', return_wait_timeout()
elif args.print_:
    print 'Current wait_timeout:', return_wait_timeout()
