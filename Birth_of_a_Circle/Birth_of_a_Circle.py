import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
from codebug_tether.sprites import Sprite
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

def build_sprite(rows):
  s = Sprite(5, 5)
  for i in range(5):
    s.set_row(i, rows[i])
  return s


while True:
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00100,0b00000,0b00000]));
  time.sleep(500/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b01110,0b10001,0b01110,0b00000]));
  time.sleep(500/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00100,0b01010,0b10001,0b01010,0b00100]));
  time.sleep(500/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b10001,0b10001,0b01110]));
  time.sleep(500/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00100,0b00000,0b00000]));
  time.sleep(400/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b01110,0b10001,0b01110,0b00000]));
  time.sleep(400/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00100,0b01010,0b10001,0b01010,0b00100]));
  time.sleep(400/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b10001,0b10001,0b01110]));
  time.sleep(400/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00100,0b00000,0b00000]));
  time.sleep(300/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b01110,0b10001,0b01110,0b00000]));
  time.sleep(300/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00100,0b01010,0b10001,0b01010,0b00100]));
  time.sleep(300/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b10001,0b10001,0b01110]));
  time.sleep(300/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00100,0b00000,0b00000]));
  time.sleep(200/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b01110,0b10001,0b01110,0b00000]));
  time.sleep(200/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00100,0b01010,0b10001,0b01010,0b00100]));
  time.sleep(200/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b10001,0b10001,0b01110]));
  time.sleep(200/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00100,0b00000,0b00000]));
  time.sleep(100/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00000,0b01110,0b10001,0b01110,0b00000]));
  time.sleep(100/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b00100,0b01010,0b10001,0b01010,0b00100]));
  time.sleep(100/1000);
  codebug.draw_sprite(0, 0, build_sprite([0b01110,0b10001,0b10001,0b10001,0b01110]));
  time.sleep(100/1000);
