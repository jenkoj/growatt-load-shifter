def operation_health_check(data):
    """
    Check for faults and loadstatus

    returns True if all ok, else false
    """

    if data["faultBit"] !=0: return False

    if data["warningBit"] !=0: return False

    # Might not be the best to overload the inverter 
    if (float(data["loadpercent"]/10) > 60): return False

    return True