#!/usr/bin/python

import sqlite3 as lite


class Table():
    table_name = 'main_table'

    def __init__(self, database_name='temperature.db'):
        self.connection = lite.connect(database_name)

    def create_table(self, table_name=table_name):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS {}( \
                           Id INTEGER PRIMARY KEY, \
                           Date DATE, \
                           Time TIME, \
                           Sensor TEXT, \
                           Temperature FLOAT)".format(table_name))
            return table_name

    def add_data(self, sensor_place, temperature, table_name=table_name):
        cursor = self.connection.cursor()
        with self.connection:
            cursor.execute("INSERT INTO {0} \
                            VALUES(null, \
                            date(), \
                            time(), \
                            '{1}', {2})".format(table_name,
                                                sensor_place,
                                                temperature))

    def get_data(self, table_name=table_name, sensor_place=None):

        # cursor = self.connection.cursor()

        with self.connection:
            self.connection.row_factory = lite.Row
            cursor = self.connection.cursor()

            if sensor_place:
                cursor.execute("SELECT * FROM {} \
                               WHERE Sensor='{}'".format(table_name,
                                                         sensor_place))
            else:
                cursor.execute("SELECT * FROM {}".format(table_name))

            rows = cursor.fetchall()
            for row in rows:
                print row
            #    print row['Id'], \
            #          row['Date'], \
            #          row['Time'], \
            #          row['Sensor'], \
            #          row['Temperature']

            return rows


if __name__ == '__main__':
    table = Table()
    # table.create_table()
    # table.add_data(sensor_place='street', temperature=12.5)
    # table.add_data(sensor_place='kitchen', temperature=10)
    # table.add_data(sensor_place='room', temperature=8.2)
    # table.add_data(sensor_place='hall', temperature=11.7)
    # table.add_data(sensor_place='street', temperature=11)
    # table.add_data(sensor_place='kitchen', temperature=20)
    # table.add_data(sensor_place='room', temperature=18.2)
    # table.add_data(sensor_place='hall', temperature=9.4)

    dt = table.get_data()
    print ""
    table.get_data(sensor_place='street')
    print ""
    print dt
