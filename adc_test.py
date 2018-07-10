#!/usr/bin/python3
import Adafruit_ADS1x15

GAIN = 2/3

def convert_adc_to_voltage(adc_reading,gain):
  return (val/0x7ff)*4.096/GAIN

#Create devices
adcs = [None]*4
for i in range(4):
  adcs[i] = Adafruit_ADS1x15.ADS1015(0x48+i)

#Read all channels from all devices
for i in range(4):
  try:
    for j in range(4):
      val=adcs[i].read_adc(j,gain=GAIN)
      volt = convert_adc_to_voltage(adc_reading=val,gain=GAIN)
      msg = 'ADC '+str(i)+', Pin '+str(j)+' reading is: ' + \
              str(val)+' '*(4-len(str(val))) + \
              ' which corresponds to %1.4f Volts.' % volt
      print(msg)
  except OSError:
    print('ADC '+str(i)+' could not be communicated with successfully')


