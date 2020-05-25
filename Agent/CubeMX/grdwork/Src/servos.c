#include "servos.h"
#include "tim.h"


extern TIM_HandleTypeDef htim2;
extern TIM_HandleTypeDef htim21;
extern TIM_HandleTypeDef htim22;



void Servos_Init(void)
{
	MX_TIM2_Init();
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_3);
	HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_4);
	HAL_TIM_PWM_Start(&htim21, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim21, TIM_CHANNEL_2);
	HAL_TIM_PWM_Start(&htim22, TIM_CHANNEL_1);
	HAL_TIM_PWM_Start(&htim22, TIM_CHANNEL_2);
	struct Servos_Position pos = {0};
	pos.second_left_feet_pos = 200;
	pos.second_right_feet_pos = 200;
	Set_Position(&pos);
}

void Servos_Handler(struct Servos_Position pos)
{
	
}

static void Set_Position(struct Servos_Position *pos)
{
	// TIM2
	htim2.Instance->CCR1 = ZERO_ANGLE_FRONT_RIGHT   - pos->front_right_feet_pos;     // front right
	htim2.Instance->CCR2 = ZERO_ANGLE_BACK_LEFT     + pos->back_left_feet_pos;       // back left
	htim2.Instance->CCR3 = ZERO_ANGLE_BACK_RIGHT    - pos->back_right_feet_pos;      // back right
	htim2.Instance->CCR4 = ZERO_ANGLE_FRONT_LEFT    + pos->front_left_feet_pos;      // front left
	// TIM21
	htim21.Instance->CCR1 = ZERO_ANGLE_SECOND_LEFT  - pos->second_left_feet_pos;     // left
	htim21.Instance->CCR2 = ZERO_ANGLE_SECOND_RIGHT + pos->second_right_feet_pos;    // right
	// TIM22
	htim22.Instance->CCR1 = ZERO_ANGLE_SECOND_LEFT  - pos->second_left_feet_pos;     // left
	htim22.Instance->CCR2 = ZERO_ANGLE_SECOND_RIGHT + pos->second_right_feet_pos;    // right
}




