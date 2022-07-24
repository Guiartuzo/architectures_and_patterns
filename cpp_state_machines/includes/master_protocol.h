namespace LAG
{
    class Master_protocol : State_Machine
    {
    public:
        void communicate();
        bool Send_start();
        bool Send_configs();
        bool Send_keep_alive();
    };
}