class PyFabricConnectError(Exception):
    """Base exception for PyFabricConnect."""


class AuthenticationError(PyFabricConnectError):
    """Authentication related errors."""


class ConnectionError(PyFabricConnectError):
    """Connection related errors."""


class QueryExecutionError(PyFabricConnectError):
    """Query execution related errors."""
