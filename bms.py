from math import isnan
from numpy import arange
from bmsConstants import bms_param_thresholds 
from bmsConstants import bms_multilingual_logs
from bmsConstants import bms_multilingual_logs_status_heading
from bmsConstants import language_description
from bmsConstants import bms_sensor_temperature_unit
from bmsConstants import bms_sensor_temperature_log
def printglobalparamLog(log_string, mode):
    if mode == True:
        print(log_string+'\n')
        
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
       
def get_param_min_limit(param_name):
    return bms_param_thresholds[param_name]['min']

def get_param_max_limit(param_name):
    return bms_param_thresholds[param_name]['max']


def validate_bms_param_name(bms_parameter):
    for param_name in bms_parameter.keys():
        if param_name not in bms_param_thresholds:
            return 'ParamNameUnknown'
    return 'OK'

def check_temprature_unit(bms_param_name, bms_param_value):
    if bms_param_name == 'temperature':
        return convert_temprature_to_celsius(bms_param_name, bms_param_value)
    return bms_param_value

def convert_temprature_to_celsius(bms_param_name, bms_param_value):
    if temperature_unit == 'F':
        temp_in_celsius = (bms_param_value - 32)*(5/9)
    else:
        temp_in_celsius = bms_param_value
    return temp_in_celsius

def validate_bms_param_value(bms_parameter):
    for param_value in bms_parameter.values():
        if isnan(param_value):
            return 'NullValue'    
    return 'OK'

def get_multilingual_keys(language):
    return bms_multilingual_logs[language].keys()

def validate_bms_alert_limits(anomaly, bms_param_name, bms_param_value, language):
    log_key = list(get_multilingual_keys(language))[0]
    bms_param_value = check_temprature_unit(bms_param_name, bms_param_value)
    if bms_param_value < get_param_min_limit(bms_param_name):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][0]])
    elif bms_param_value > get_param_max_limit(bms_param_name):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][1]])

def warning_range(param_min_limit, param_max_limit, mode):
    warning_tolerance_percentage = 0.05
    warning_tolerance = warning_tolerance_percentage * param_max_limit
    if mode == 'min':
        return list(arange(param_min_limit, param_min_limit + warning_tolerance, 0.1))
    elif mode == 'max':
        return list(arange(param_max_limit - warning_tolerance, param_max_limit, 0.1))
    
def validate_bms_warning_limits(anomaly, bms_param_name, bms_param_value, language):
    param_min_limit = get_param_min_limit(bms_param_name)
    param_max_limit = get_param_max_limit(bms_param_name)
    log_key = list(get_multilingual_keys(language))[1]
    if bms_param_value in warning_range(param_min_limit, param_max_limit, mode='min'):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][0]])
    elif bms_param_value in warning_range(param_min_limit, param_max_limit, mode='max'):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][1]])
        
         
def validate_overall_bms_health(status_report):
    bms_error_report = {}
    for bms_param_name in status_report:
        validate_bms_warning_limits(bms_error_report, bms_param_name, status_report[bms_param_name], language)
        validate_bms_alert_limits(bms_error_report, bms_param_name, status_report[bms_param_name], language)  
    bms_log_report(bms_error_report)
    return bms_error_report

def bms_log_report(bms_error_report):
    if len(bms_error_report) == 0:
        print(bms_multilingual_logs_status_heading[language][0]+'\n')
    else:
        print('------------------------------------')
        print('        {}          '.format(bms_multilingual_logs_status_heading[language][1]))
        print('------------------------------------\n')        
        for param_name, param_value in zip(bms_error_report.keys(), bms_error_report.values()):
            printLog(param_name, param_value)
        print('\n')

def printLog(param_name,param_value):
    log_key = list(get_multilingual_keys(language))
    if param_value[0] == log_key[0]:
        print('\033[31m' + '{}'.format(param_value[0]) + '\033[m' + '   : {} -> {}'.format(param_name,param_value[1]))
    elif param_value[0] == log_key[1]:
        print('\033[32m' + '{}'.format(param_value[0]) + '\033[m' + ' : {} -> {}'.format(param_name,param_value[1]))                
