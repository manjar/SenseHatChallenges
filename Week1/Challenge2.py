from sense_hat import SenseHat
import time

"""

  Sense HAT Sensors Display
  
  Select Temperature, Pressure, or Humidity  with the Joystick
  to visualize the current sensor values on the LED.
  
  Note: Requires sense_hat 2.2.0 or later

"""

sense = SenseHat()

green  = (  0, 255,   0)
red    = (255,   0,   0)
blue   = (  0,   0, 255)
white  = (255, 255, 255)
black  = (  0,   0,   0)
orange = (255, 165,   0)

humidityColor = blue
tempColor     = green
pressureColor = orange


def show_t():
  sense.show_letter("T", back_colour = tempColor)
  time.sleep(.5)

def show_p():
  sense.show_letter("P", back_colour = pressureColor)
  time.sleep(.5)

def show_h():
  sense.show_letter("H", back_colour = humidityColor)
  time.sleep(.5)

def update_screen():
  temp = sense.temp
  temp_value = temp / 2.5 + 16
  pixels =  [tempColor if (i * 4) < temp_value else white for i in range(16)]
  pixels += [black for i in range(8)]
  pressure = sense.pressure
  pressure_value = pressure / 20
  pixels += [pressureColor if (i * 4) < pressure_value else white for i in range(16)]
  pixels += [black for i in range(8)]
  humidity = sense.humidity
  humidity_value = 64 * humidity / 100
  pixels += [humidityColor if (i * 4) < humidity_value else white for i in range(16)]
  sense.set_pixels(pixels)

####
# Intro Animation
####

show_t()
show_p()
show_h()

####
# Main game loop
####

while True:
    update_screen()
  
