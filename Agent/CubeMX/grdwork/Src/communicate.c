#include "communicate.h"
#include "servos.h"
#include "usart.h"

char buffer[EXPECTED_LEN] = {0};

void Comm_Init()
{
	MX_USART2_UART_Init();
	HAL_UART_Receive_IT(&huart2,(uint8_t*) buffer, EXPECTED_LEN);
}


struct Servos_Position Receive_and_Parse_Packet()
{
	struct Servos_Position pos = {0};
	if(huart2.RxXferCount == 0)
	{
		HAL_UART_Receive_IT(&huart2,(uint8_t*) buffer, EXPECTED_LEN);
	}
		
	uint8_t *buf = (uint8_t*) &buffer[1];
	
	pos.back_left_feet_pos    =   *buf++ << 8;
	pos.back_left_feet_pos    +=  *buf++;
	
	pos.back_right_feet_pos   =   *buf++ << 8;
	pos.back_right_feet_pos   +=  *buf++;
	
	pos.front_left_feet_pos   =   *buf++ << 8;
	pos.front_left_feet_pos   +=  *buf++;
	
	pos.front_right_feet_pos  =   *buf++ << 8;
	pos.front_right_feet_pos  +=  *buf++;
	
	pos.second_left_feet_pos  =   *buf++ << 8; 
	pos.second_left_feet_pos  +=  *buf++;
	
	pos.second_right_feet_pos =   *buf++ << 8;
	pos.second_right_feet_pos +=  *buf++;
	return pos;
}