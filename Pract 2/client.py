# client.py
# RMI Client using Pyro4 (Corrected Version)

import Pyro4


def main():
    try:
        # Connect to server using name
        server = Pyro4.Proxy("PYRONAME:string.server")

        # Input from user
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")

        # Remote call
        result = server.concatenate_strings(str1, str2)

        print("Concatenated Result:", result)

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    main()