#ifndef __SERVOS_H_
#define __SERVOS_H_

#include "stm32l0xx_hal.h"

#define ZERO_ANGLE_FRONT_LEFT    800
#define ZERO_ANGLE_BACK_LEFT     800
#define ZERO_ANGLE_FRONT_RIGHT   2500
#define ZERO_ANGLE_BACK_RIGHT    2400
#define ZERO_ANGLE_SECOND_LEFT   1700
#define ZERO_ANGLE_SECOND_RIGHT  1500

struct Servos_Position
{
	uint16_t back_left_feet_pos;
	uint16_t back_right_feet_pos;
	uint16_t front_left_feet_pos;
	uint16_t front_right_feet_pos;
	
	uint16_t second_left_feet_pos;
	uint16_t second_right_feet_pos;
};

// public
void Servos_Init(void);
void Servos_Handler(struct Servos_Position *pos);

// static
static void Set_Position(struct Servos_Position *pos);

#endif
