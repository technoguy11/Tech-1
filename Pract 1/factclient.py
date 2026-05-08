# factclient.py
# RPC Client for calling the factorial server

import xmlrpc.client


def main():
    try:
        # Connect to the RPC server
        proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2", allow_none=True)

        # Take input from user
        user_input = input("Enter a non-negative integer: ").strip()

        # Convert input to integer
        n = int(user_input)

        # Call remote method on server
        result = proxy.calculate_factorial(n)

        # Display result
        print(f"Factorial of {n} is: {result}")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"RPC Error: {e}")


if __name__ == "__main__":
    main()