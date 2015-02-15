class NodeDisconnectException(Exception):
    """
    This exception is thrown when a client is disconnected.
    """
    pass


class UnknownMessageException(Exception):
    """
    This exception is thrown when trying to (de)serialize an
    unknown message type
    """
    pass
