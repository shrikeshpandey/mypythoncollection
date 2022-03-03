#!/usr/bin/env python
'''
    File name: connect_db_query.py
    Author: Rui Monteiro
    Date created: 16/01/2019
    Date last modified: 16/01/2019
    Python Version: 3.6
'''

import os
import cx_Oracle
import json
import sys
import time
import csv
from datetime import datetime

class ConnectDB(object):
    """docstring for ConnectDB"""

    def __init__(self, poolDB):
        super(ConnectDB, self).__init__()
        self.poolDB = poolDB

    def extractQuery(self, query, o_csv):
        while True:
            try:
                con = self.poolDB.acquire()
                break
            except:
                print("Error acquiring connection!")
                print(self.poolDB.opened)
                time.sleep(4)
        if con is None:
            print('Error! No connections in the pool.')
            sys.exit(0)
        cur = con.cursor()
        cur.execute(query)

        # Write to csv.
        with open(o_csv, mode='w') as csv_file:
            skulist_writer = csv.writer(csv_file, delimiter=',')
            for result in cur:
                skulist_writer.writerow(result)

        # Close connection.
        cur.close()
        self.poolDB.release(con)

def main():

    start = time.time()

    # Configure session credentials.
    crd = json.load( open('access.json') )['TST']['BD']
    dsn = cx_Oracle.makedsn(crd['HOST'], crd['PORT'], crd['SID'])
    mypool = cx_Oracle.SessionPool(user=crd['USER'], password=crd['PASS'], dsn=dsn, min=4, max=20, increment=2, threaded = True)
    os.environ["NLS_LANG"] = ".WE8ISO8859P1"

    # Example query.
    query = "select * from skulist_detail a where a.skulist = 13012"
    queryTime = datetime.now().strftime("%Y%m%d_%H%M%S")

    sess = ConnectDB(mypool)
    sess.extractQuery(query, 'query_result_' + format(queryTime) + '.csv')

    end = time.time()
    elapsed_time = end - start
    print("Finished in " + str(round(elapsed_time, 3)) + " seconds.")

if __name__ == "__main__":
    main()

