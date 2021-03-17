from math import isnan
from bmsConstants import bms_param_thresholds 
from bmsConstants import bms_multilingual_logs
from bmsConstants import bms_multilingual_logs_status_heading
from bmsAccumulator import accumulateLogs
from bmsController import call_controller
import bmsGlobalParam as bgp

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
    if bgp.temperature_unit == 'F':
        temp_in_celsius = (bms_param_value - 32)*(5/9)
    else:
        temp_in_celsius = bms_param_value
    return round(temp_in_celsius,2)

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

def generate_warning_range(param_lower_limit, param_higher_limit):
    warning_range = []
    counter = param_lower_limit
    while counter < param_higher_limit:
        warning_range.append(round(counter , 2))
        counter+=0.01
    return warning_range

def warning_range(param_min_limit, param_max_limit, mode):
    warning_tolerance_percentage = 0.05
    warning_tolerance = warning_tolerance_percentage * param_max_limit
    if mode == 'min':
        return generate_warning_range(param_min_limit, param_min_limit + warning_tolerance)
    elif mode == 'max':
        return generate_warning_range(param_max_limit - warning_tolerance, param_max_limit)
    
def validate_bms_warning_limits(anomaly, bms_param_name, bms_param_value, language):
    param_min_limit = get_param_min_limit(bms_param_name)
    param_max_limit = get_param_max_limit(bms_param_name)
    log_key = list(get_multilingual_keys(language))[1]
    bms_param_value = check_temprature_unit(bms_param_name, bms_param_value)
    if bms_param_value in warning_range(param_min_limit, param_max_limit, mode='min'):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][0]])
    elif bms_param_value in warning_range(param_min_limit, param_max_limit, mode='max'):
        anomaly[bms_param_name] = list([log_key, bms_multilingual_logs[language][log_key][1]])
        
         
def validate_overall_bms_health(status_report, log_mode='off', controller_mode='off'):
    bms_error_report = {}
    for bms_param_name in status_report:
        validate_bms_warning_limits(bms_error_report, bms_param_name, status_report[bms_param_name], bgp.language)
        validate_bms_alert_limits(bms_error_report, bms_param_name, status_report[bms_param_name], bgp.language)  
    bms_overall_output_heading(bms_error_report)
    accumulateLogs(bms_error_report, log_mode)
    call_controller(bms_error_report, controller_mode)
    return bms_error_report

def bms_overall_output_heading(bms_error_report):
    if len(bms_error_report) != 0:
        print('------------------------------------')
        print('        {}          '.format(bms_multilingual_logs_status_heading[bgp.language][1]))
        print('------------------------------------\n')    