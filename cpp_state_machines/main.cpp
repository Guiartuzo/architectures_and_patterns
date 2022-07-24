/*
    This class is the "main" and starts the master's comunication with it's slave. 
*/

#include<stdio.h>
#include<master_protocol.h>

using namespace LAG

int main()
{
    Master_protocol master;
    master.communicate();
}
