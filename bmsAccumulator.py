
from bmsConstants import bms_multilingual_logs_status_heading
from bmsConstants import bms_multilingual_logs
import bmsGlobalParam as bgp

def accumulateLogs(bms_error_report, log_mode):
    if log_mode == 'on':
        bms_log_report(bms_error_report)
        
def bms_log_report(bms_error_report):
    if len(bms_error_report) == 0:
        print(bms_multilingual_logs_status_heading[bgp.language][0]+'\n')
    else:    
        for param_name, param_value in zip(bms_error_report.keys(), bms_error_report.values()):
            printLog(param_name, param_value)
        print('\n')

def printLog(param_name,param_value):
    log_key = list(bms_multilingual_logs[bgp.language].keys())
    if param_value[0] == log_key[0]:
        print('\033[31m' + '{}'.format(param_value[0]) + '\033[m' + '   : {} -> {}'.format(param_name,param_value[1]))
    elif param_value[0] == log_key[1]:
        print('\033[32m' + '{}'.format(param_value[0]) + '\033[m' + ' : {} -> {}'.format(param_name,param_value[1]))                
