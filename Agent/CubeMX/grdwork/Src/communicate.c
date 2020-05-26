#include "communicate.h"
#include "servos.h"
#include "usart.h"

char buffer[15] = {0};

void Comm_Init()
{
	MX_USART2_UART_Init();
	HAL_UART_Receive_IT(&huart2,(uint8_t*) buffer, 15);
}


struct Servos_Position Receive_and_Parse_Packet()
{
	struct Servos_Position pos = {0};
	if(huart2.RxXferCount == 0)
	{
		HAL_UART_Receive_IT(&huart2,(uint8_t*) buffer, 15);
	}
		
	pos.back_left_feet_pos = buffer[2] << 8 & buffer[1];

//	pos.back_right_feet_pos =;
//	pos.front_left_feet_pos = ;
//	pos.front_right_feet_pos = ;
//	
//	pos.second_left_feet_pos = ;
//	pos.second_right_feet_pos = ;
	return pos;
}