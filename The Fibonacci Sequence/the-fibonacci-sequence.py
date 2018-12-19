import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
from codebug_tether.sprites import StringSprite

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
  codebug.scroll_sprite(StringSprite('1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597-2584-4181-6765...', 'R'), 377/1000, 'L')
  codebug.scroll_sprite(StringSprite('1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597-2584-4181-6765...', 'R'), 233/1000, 'L')
  codebug.scroll_sprite(StringSprite('1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597-2584-4181-6765...', 'R'), 1/1000, 'L')
