bms_param_thresholds = { 
                         'temperature': {'min': 0, 'max': 45},
                         'soc': {'min': 25 ,'max': 75},
                         'charging_rate': {'min': 0, 'max': 0.8}
                       }
bms_param_descriptions = {
                           'temperature': 'Temperature ( in celsius )',
                           'soc': 'State of charge ( in % )',
                           'charging rate': 'Charging Rate ( in coulombs )'
                         }

bms_multilingual_logs = {
                            'en': {
                                    'ALERT': ['Under Limit', 'Exceed Limit'] ,
                                    'WARNING': ['Approaching Lower Limit', 'Approaching Peak limit'] 
                                  },
                            
                            'de': {
                                    'AUFMERKSAM': ['Unter Limit', 'Limit überschreiten'] ,
                                    'WARNUNG': ['Annäherung Untere Grenze', 'Annäherung Spitzengrenze'] 
                                  }
                        }

bms_multilingual_logs_status_heading = {
                                    'en': ['All Parameters are OK', 'BMS Log Report'],
                                    'de': ['Alle Parameter sind in Ordnung', 'BMS Protokollbericht']
                                }

language_description = {
                          'en': 'System Language set to English',
                          'de': 'Systemsprache auf Deutsch eingestellt'
                       }

bms_sensor_temperature_unit = {
                          'C': 'Celsius',
                          'F': 'Fahrenheit'
                       }
bms_sensor_temperature_log = {
                                 'en': 'Sensor Temperature is considered in',
                                 'de': 'Sensortemperatur wird in berücksichtigt'
                             }