class LED:
  def __init__(self, line, bank, chip=1):
    from maix import gpio
    self.led = gpio.gpio(line, bank, chip)
  def on(self):
    self.led.set_value(1)
  def off(self):
    self.led.set_value(0)
  def value(self):
    return self.led.get_value()
  def __del__(self):
    self.led.release()