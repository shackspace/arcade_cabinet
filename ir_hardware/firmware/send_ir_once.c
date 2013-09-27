/*
 * send_ir_once.c
 *
 *  Created on: 27.09.2013
 *      Author: alex
 *
 *      Sends the "Source" code of the Sony RM-833 remote control once on power on, then sleeps forever
 *      Connect IR LED to port B2 of Attiny 2313
 */

#include <avr/io.h>
#include <util/delay.h>
#include <avr/sleep.h>

#define LED_ON()		DDRB=1<<PB2
#define LED_OFF()		DDRB&=~(1<<PB2)

#define HEADER_PULSE	2369
#define SPACE			600
#define ONE_PULSE		1200
#define ZERO_PULSE		600
#define GAP				44596
#define CODE			0xA50

#define OCR_VALUE		104		//Value needed to generate 38khz (See atmega8 datasheet page 109)

#define WAIT_AFTER_POWERON 10000 //Wait 10 seconds after power on before sending signal

// Initiate the Timer in CTC mode, Set to generate about 38kHz
void initPWM(void) {
	TCCR0A = 1<< COM0A0 | 1<< WGM01;
	TCCR0B = 1<< CS00;
	OCR0A = OCR_VALUE;
}


//Send modulated signal by enabling and disabling PWM output
void sendIRcode(void) {
	uint16_t code = CODE;
	LED_ON();
	_delay_us(HEADER_PULSE);
	LED_OFF();
	_delay_us(SPACE);

	for (uint8_t i=0;i<12;i++) {
		LED_ON();
		if (code & 1<<11) {
			_delay_us(ONE_PULSE);
		} else {
			_delay_us(ZERO_PULSE);
		}
		LED_OFF();
		_delay_us(SPACE);
		code=code<<1;
	}
}

int main(void) {
	initPWM();
	_delay_ms(WAIT_AFTER_POWERON);
	sendIRcode();
	_delay_us(GAP);
	sendIRcode();
	set_sleep_mode(SLEEP_MODE_PWR_DOWN);
	sleep_mode();
	while (1) {
		//hang here, never wake up
	}
}
