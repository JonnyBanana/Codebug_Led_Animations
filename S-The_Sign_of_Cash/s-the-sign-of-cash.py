import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
import time

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);


while True:
  # gamba sopra s ____
  codebug.set_pixel(4, 4, 1);
  codebug.set_pixel(3, 4, 1);
  codebug.set_pixel(2, 4, 1);
  codebug.set_pixel(1, 4, 1);
  codebug.set_pixel(0, 4, 1);
  # gamba verticale sx
  # I
  # I
  codebug.set_pixel(0, 3, 1);
  codebug.set_pixel(0, 2, 1);
  # blocco centrale
  codebug.set_pixel(1, 2, 1);
  codebug.set_pixel(2, 2, 1);
  codebug.set_pixel(3, 2, 1);
  codebug.set_pixel(4, 2, 1);
  # gamba verticale dx
  codebug.set_pixel(4, 1, 1);
  codebug.set_pixel(4, 0, 1);
  codebug.set_pixel(3, 0, 1);
  codebug.set_pixel(2, 0, 1);
  # gamba sotto s _____
  codebug.set_pixel(1, 0, 1);
  codebug.set_pixel(0, 0, 1);
  time.sleep(500/1000);
  codebug.clear();
  codebug.set_pixel(0, 0, 1);
  codebug.set_pixel(1, 0, 1);
  codebug.set_pixel(2, 0, 1);
  codebug.set_pixel(3, 0, 1);
  codebug.set_pixel(4, 0, 1);
  codebug.set_pixel(4, 1, 1);
  codebug.set_pixel(4, 2, 1);
  codebug.set_pixel(3, 2, 1);
  codebug.set_pixel(2, 2, 1);
  codebug.set_pixel(1, 2, 1);
  codebug.set_pixel(0, 2, 1);
  codebug.set_pixel(0, 3, 1);
  codebug.set_pixel(0, 4, 1);
  codebug.set_pixel(1, 4, 1);
  codebug.set_pixel(2, 4, 1);
  codebug.set_pixel(3, 4, 1);
  codebug.set_pixel(4, 4, 1);
  time.sleep(500/1000);
  codebug.clear();
