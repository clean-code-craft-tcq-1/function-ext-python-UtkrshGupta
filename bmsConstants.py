bms_param_thresholds = { 
                         'temperature': {'min': 0, 'max': 45},
                         'soc': {'min': 25 ,'max': 80},
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

controller_actions_heading = {
                                 'en': 'Controller is Triggered and performing below actions',
                                 'de': 'Der Controller wird ausgelöst und führt die folgenden Aktionen aus'
                             }
controller_actions = {
                        '00': {'en':'Increasing and Maintaining Battery {} quickly',
                               'de': 'Batterie erhöhen und warten {} schnell'},
                        '01': {'en':'Decreasing and Maintaining Battery {} quickly',
                               'de': 'Batterie verringern und warten {} schnell'},
                        '10': {'en':'Maintaining {} to avoid warnings for lower limits',
                               'de':'Aufrechterhaltung {} um Warnungen für untere Grenzwerte zu vermeiden'},
                        '11': {'en':'Maintaining {} to avoid warnings for upper limits',
                               'de':'Aufrechterhaltung {} um Warnungen für Obergrenzen zu vermeiden'}
                  }