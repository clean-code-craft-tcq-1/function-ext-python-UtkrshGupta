from bmsConstants import language_description
from bmsConstants import bms_sensor_temperature_unit
from bmsConstants import bms_sensor_temperature_log
        
def set_system_language(lang = 'en', mode = True):
    global language
    if lang in language_description:
        language = lang 
        printglobalparamLog(language_description[language], mode=mode)
        return True
    else:
        return False
    
def set_sensor_temperatue_unit(temp_unit='C', mode=True):
    global temperature_unit
    if temp_unit in bms_sensor_temperature_unit:
        temperature_unit = temp_unit
        printglobalparamLog( log_string=bms_sensor_temperature_log[language]+' {}\n'.format(bms_sensor_temperature_unit[temp_unit]), mode=mode)
        return True
    else:
        return False

def printglobalparamLog(log_string, mode):
    if mode == True:
        print(log_string+'\n')        