
Total No. of Questions - [06]                Total No. of Printed Pages: 2
G.R. No.
DECEMBER 2021 - ENDSEM EXAM
T. Y. B. TECH. (ELECTRONICS AND TELECOMMUNICATION)
(SEMESTER - I)
COURSE NAME: MICROCONTROLLER AND APPLICATIONS
COURSE CODE: ETUA31182
(PATTERN 2018)

Time: [1 Hour]                                      [Max. Marks: 30]

(*) Instructions to candidates:

AnSWer Q.1 OR Q.2, Q.3 OR Q.4, Q.5 OR Q.6.

Figures to the right indicate full marks.

Use of scientific calculator is allowed

Use suitable data where ever required

# Q.1)

a) Compare, how I2C is advantageous over SPI?                                [4]

b) Interface system with 8051 microcontroller using RS 232 in null           [6]

modem configuration. Illustrate the pins of RS232 used for null modem.

# OR

# Q.2)

a) Compare Rs232 with RS485.                                                 [4]

b) Interface I2C based ADC chip PCF8591 with 8051 microcontroller for           [6]

ADC address 90H. With the help of timing diagram draw the start and

stop signal generation to initiate start and stop conditions.

# Q.3)

a) Illustrate the features of USART serial interface available with AVR      [4]

ATmega32 microcontroller.

b) Construct the internal architecture of AVR CPU core and discuss the       [6]

functions of each block in brief.

# OR

# Q.4)

a) With respect to timing diagram, analyze the various actions performed    [4]

during instruction execution in pipeline architecture of AVR.

b) Illustrate any three addressing modes used in AVR                     [6]

microcontrollers with example.


---



#include "avr/io.h"
int main()
{
DDRB = 0b11111111;
OCR0 = 191;
TCCR0 = 0x61;
while (1);
return 0;
}

b) It is decided to design a temperature measurement system which displays an ambient temperature microcontroller laboratory using AVR ATmega32 microcontroller. The temperature is displayed on two digit seven segment display. Draw the interface diagram which uses serial peripheral interface for seven segment display, use suitable seven segment driver. Write algorithm for temperature reading and displaying process.

OR

Q.6)a In a certain DC motor speed control application using AVR, the required duty cycle to maintain a constant speed is 50%. It is decided to use Timer0 of AVR using output compare approach to generate PWM output in non-inverting mode with no-prescaler, calculate the count to be loaded in OCR0 register.

b) Interface two seven segment LED displays using MAX7221 display driver with AVR for making interfacing minimum use serial peripheral interface of microcontroller. Write different steps to send any number from microcontroller to seven segment display.

