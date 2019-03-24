#!/usr/bin/python

import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('.my.cnf')

def connect():
    return mysql.connector.connect(host = config['mysqlDB']['host'],
                                   user = config['mysqlDB']['user'],
                                   passwd = config['mysqlDB']['pass'],
                                   db = config['mysqlDB']['db'])
