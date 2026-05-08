# server.py
# RMI Server using Pyro4 (Corrected Version)

import Pyro4

@Pyro4.expose
class StringServer:
    """
    Remote class exposed to client
    """

    def concatenate_strings(self, str1, str2):
        """
        Concatenate two strings
        """
        return str1 + str2


def main():
    # Create daemon
    daemon = Pyro4.Daemon(host="localhost")

    try:
        # Try connecting to Name Server
        ns = Pyro4.locateNS(host="localhost")
    except:
        print("❌ ERROR: Pyro Name Server is not running!")
        print("👉 Run this first in another terminal: pyro4-ns")
        return

    # Create object
    obj = StringServer()

    # Register object
    uri = daemon.register(obj)

    # Register name
    ns.register("string.server", uri)

    print("✅ Server is running...")
    print("URI:", uri)

    daemon.requestLoop()


if __name__ == "__main__":
    main()