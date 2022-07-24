namespace GSM
{
    enum Event
    {
        SEND_START,
        SEND_CONFIGS,
        SEND_KEEP_ALIVE,
        ALERT_STATUS,
        HANDSHAKE_START
    };

    enum State
    {
        INTERFACE_OK,
        INTERFACE_NOTK,
        LINK_IS_DOWN,
        SEND_CONFIG,
        SEND_KEEP_ALIVE
    };

    class State_Machine
    {
    public:
        void NextEventHandler(State *state, Event *event);
    };
}