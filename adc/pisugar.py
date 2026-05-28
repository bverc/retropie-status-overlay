# ADC Plugin for retropie-status-overlay
# github.com/bverc/retropie-status-overlay
#
# ADC module for PiSugar3
# https://github.com/PiSugar/PiSugar/wiki/PiSugar-3-Series
#
# Author: bverc
#
# I2C must be enabled via raspi-config

# Import smbus for I2C interface
import smbus

#  PiSugar register is at address 0x57
address = 0x57

# Initialize I2C (SMBus) on I2C Channel 1
bus = smbus.SMBus(1)

# ADC read function, return voltage
def read(channel):
  raw = bus.read_word_data(address, 0x22)
  raw_swapped = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)
  voltage = raw_swapped / 1000.0
  return voltage
