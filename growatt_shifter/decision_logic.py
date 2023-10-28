def decide(data, old_data, sec_since_update, current_date_time, verbose):
    # Rules 
    green_flag = True
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    if data == old_data: green_flag = False
    if verbose: print("is data new? :", data != old_data)

    if sec_since_update > 100: green_flag = False
    if verbose: print("sec_since_update:", sec_since_update)

    if (float(data["loadpercent"]/10) > 60): green_flag = False
    if verbose: print("load percent:", data["loadpercent"]/10)

    if (float(data["bat_Volt"]/100) <= 54): green_flag = False
    if verbose: print("battery voltage:", float(data["bat_Volt"]/100))
    
    if (current_date_time.hour >= 15): green_flag = False
    if verbose: print("hour:", current_date_time.hour)

    discharge_status = data["pvstatus"]
    #if (discharge_status == "Bypass"): green_flag = False
    if (discharge_status != 9): green_flag = False
    if verbose: print("discharge status (9 is ok):", discharge_status)

    # with open("/home/pi/sonoff/shifter/run.log", "w") as file:
    #     file.write("Last execution time: " + formatted_date_time + " STATE:" + str(green_flag)+"\n")
    #     file.write("sec_since_update:"+str(sec_since_update)+"\n")
    #     file.write("load percent:"+str(data["loadpercent"]/10)+"\n")
    #     file.write("battery voltage:"+str(data["bat_Volt"]/100)+"\n")
    #     file.write("discharge status:"+str(discharge_status)+"\n")
    #     file.write("hour:"+str(current_date_time.hour)+"\n")


    # if green_flag:
    #     with open("/home/pi/sonoff/shifter/run_true.log", "w") as file:
    #         file.write("Last true execution time: " + formatted_date_time + " STATE:" + str(green_flag)+"\n")
    #         file.write("sec_since_update:"+str(sec_since_update)+"\n")
    #         file.write("load percent:"+str(data["loadpercent"])+"\n")
    #         file.write("battery voltage:"+str(data["bat_Volt"])+"\n")
    #         file.write("discharge status:"+str(discharge_status)+"\n")
    #         file.write("hour:"+str(current_date_time.hour)+"\n")
    
    return green_flag