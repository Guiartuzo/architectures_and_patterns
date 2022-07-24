/*
    Implementation of generic state machine, it should take decisions based on link status
    and current event.
    returns next event, and sets current link status.
*/

#include "switch_state_machine.h"
#include<stdio.h>
#include<iostream>

using namespace GSM;

class State_Machine
{
public:

    void NextEventHandler(State *state, Event *event)
    {

    }
};