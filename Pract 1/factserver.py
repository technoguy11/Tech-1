# factserver.py
# RPC Server for factorial calculation using XML-RPC

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class FactorialServer:
    """
    This class contains the remote method that the client can call.
    The server receives an integer and returns its factorial.
    """

    def calculate_factorial(self, n):
        """
        Calculate factorial of a non-negative integer.

        Parameters:
            n (int): input integer

        Returns:
            int: factorial of n
        """
        # Validate input
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")

        if n < 0:
            raise ValueError("Input must be a non-negative integer.")

        result = 1
        for i in range(1, n + 1):
            result *= i

        return result


class RequestHandler(SimpleXMLRPCRequestHandler):
    """
    Restrict XML-RPC requests to the /RPC2 path only.
    This is a common security and routing practice.
    """
    rpc_paths = ('/RPC2',)


def main():
    # Create the server on localhost and port 8000
    with SimpleXMLRPCServer(
        ("localhost", 8000),
        requestHandler=RequestHandler,
        allow_none=True,
        logRequests=True
    ) as server:

        # Register built-in system methods like listMethods
        server.register_introspection_functions()

        # Register our FactorialServer instance
        server.register_instance(FactorialServer())

        print("Factorial RPC Server is running on http://localhost:8000/RPC2")
        print("Waiting for client requests...")

        # Keep server alive
        server.serve_forever()


if __name__ == "__main__":
    main()