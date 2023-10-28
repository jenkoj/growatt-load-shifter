from influxdb import InfluxDBClient
from datetime import datetime
import pytz

def connect_to_influxdb(host, port, database):
    client = InfluxDBClient(host=host, port=port)
    client.switch_database(database)
    return client

def query_influxdb(client):
    storage_id = "ZRK0CK80FU"
    query = "SELECT * FROM {} ORDER BY time DESC LIMIT 1".format(storage_id)
    result = client.query(query)
    point = list(result.get_points())[0]
    current_date_time_utc = datetime.strptime(point['time'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.UTC)
    local_tz = pytz.timezone('Europe/Ljubljana')
    current_date_time = current_date_time_utc.astimezone(local_tz)

    sec_since_update = (datetime.now(tz=local_tz) - current_date_time).total_seconds()

    return point, sec_since_update, current_date_time
