class MCPMessage:
    def __init__(self,sender,receiver,msg_type,trace_id,payload):
        self.message={
            "sender":sender,
            "receiver":receiver,
            "type":msg_type,
            "trace_id":trace_id,
            "payload":payload}

    def get(self):
        return self.message
