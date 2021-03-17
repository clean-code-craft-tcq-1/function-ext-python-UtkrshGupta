import bmsGlobalParam as bgp
from bmsConstants import bms_multilingual_logs
from bmsConstants import controller_actions
from bmsConstants import controller_actions_heading

def call_controller(bms_error_report, controller_trigger_mode):
    if controller_trigger_mode == 'on':
        execute_controller_actions(bms_error_report)

def execute_controller_actions(bms_error_report):
    if len(bms_error_report) != 0:
        print(controller_actions_heading[bgp.language]+'\n')
        for param_name, param_value in zip(bms_error_report.keys(), bms_error_report.values()):
            log_controller_actions(param_name, param_value)    
        print('\n')    
        
def log_controller_actions(param_name, param_value):
    error_code = get_error_code(param_value)
    if error_code in controller_actions.keys():
        print('-> ' + controller_actions[error_code][bgp.language].format(param_name))
    
def get_error_code(error_values):
    error_types = list(bms_multilingual_logs[bgp.language].keys())  
    global_error_values = global_error_values=bms_multilingual_logs[bgp.language][error_values[0]]
    if error_values[0] == error_types[0]:
        error_type = '0'
        error_code = generate_error_code(error_type, error_value=error_values[1], global_error_values=global_error_values)
    elif error_values[0] == error_types[1]:
        error_type = '1'
        error_code = generate_error_code(error_type, error_value=error_values[1], global_error_values=global_error_values)
    return error_code

def generate_error_code(error_type, error_value, global_error_values):
    if error_type == '0':
        error_code = error_type + check_error_value(error_value, global_error_values)   
    elif error_type == '1':
        error_code = error_type + check_error_value(error_value, global_error_values)
    return error_code
    
def check_error_value(error_value, global_error_values):
    if error_value == global_error_values[0]:
        error_code = '0'
    elif error_value == global_error_values[1]:
        error_code = '1'
    return error_code

