/*
    This class emulates a master equipment trying to comunicate with it's respective slave.
    It should start the comunication and access the state machine in order to get the next event.
*/

#include "switch_state_machine.h"
#include "master_protocol.h"

using namespace GSM;
using namespace LAG;

class Master_protocol : State_Machine
{
public:

    void communicate()
    {
        State state = INTERFACE_OK;
        Event event = SEND_START;

        NextEventHandler(&state, &event);

        while(1)
        {
            NextEventHandler(&state, &event);
        }
    }

    bool Send_start()
    {

    }

    bool Send_configs()
    {

    }

    bool Send_keep_alive()
    {

    }
};