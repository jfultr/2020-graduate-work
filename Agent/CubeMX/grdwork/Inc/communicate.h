#ifndef __COMMUNICATE_H_
#define __COMMUNICATE_H_

#define EXPECTED_LEN          15

void Comm_Init(void);
struct Servos_Position Receive_and_Parse_Packet(void);

#endif
