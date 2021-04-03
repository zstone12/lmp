from influxdb import InfluxDBClient
from config import cfg

DBNAME = cfg["influxdb"]["dbname"]
USER = cfg["influxdb"]["user"]
PASSWORD = cfg["influxdb"]["password"]

influx_client = InfluxDBClient(database=DBNAME,host='localhost',username=USER,password=PASSWORD)
influx_client.get_list_database()
influx_client.create_database('lmp')
influx_client.get_list_database()
tmp = [{"measurement": None, "tags": {}, "fields": {}, }]
influx_client.write_points(tmp)

# TODO: 接入其他数据库
# mysql_client
# es_client
# prometheus_client
# test
