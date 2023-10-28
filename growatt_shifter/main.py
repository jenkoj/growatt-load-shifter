import time
import sys

from influxdb_handling import connect_to_influxdb, query_influxdb
from decision_logic import decide
from load_handling import handle_load
from health_check import operation_health_check
from config import INFLUX_HOST, INFLUX_PORT, INFLUX_DATABASE, LOAD_ON_SCRIPT, LOAD_OFF_SCRIPT, VERBOSE

client = connect_to_influxdb(INFLUX_HOST,
                            INFLUX_PORT,
                            INFLUX_DATABASE)

load_state = False
data = 0

while True:
    
    try:
        green_flag = False  # Just in case

        old_data = data
        data, sec_since_update_query, current_date_time = query_influxdb(client)

        green_flag = decide(data, old_data, sec_since_update_query, current_date_time, VERBOSE)
        # Execute if true
        #green_flag = True # override
        print("Turn on boiler? ", green_flag)

        if green_flag:
            if VERBOSE: print("Turning on boiler!")
            handle_load(LOAD_ON_SCRIPT)
            load_state = True


        if operation_health_check(data) & (load_state): 
            handle_load(LOAD_OFF_SCRIPT)
            if VERBOSE: print("WARNING, health check not passed")
            if VERBOSE: print(f"-> warningbit{data['warningBit']}")
            if VERBOSE: print(f"-> faultbit{data['faultBit']}")
            if VERBOSE: print(f"-> loadperc{data['loadpercent']/10}")
            load_state = False

        _, sec_since_update, _ = query_influxdb(client)

    except KeyboardInterrupt:
        print("Script execution stopped by the user.")
        break  # Re-raise the exception to break the main loop
    
    except ValueError as e:
        print("Value error occurred, :", e)
        sys.exit(1)

    except Exception as e:
        sec_since_update = 404
        print(f"An error occurred: {e}")
        print("exiting")
        sys.exit(1)
    
    print("time since update at calculation, ", sec_since_update)
    sleep_time = (84 - sec_since_update)   # Calculate sleep time

    #In cases where something goes wrong long wait times
    if sleep_time < -40:
        if load_state:
            handle_load(LOAD_OFF_SCRIPT)
            load_state = False

        sleep_time = 80 # Datalogger refresh period

    if sleep_time < 0:
        sleep_time = 4

    # in case when data gets updated while cruinching
    if sec_since_update < sec_since_update_query:
        sleep_time = 0

    print("Sleeping for", sleep_time, "seconds")
    time.sleep(sleep_time)  # Wait for the specified sleep time

