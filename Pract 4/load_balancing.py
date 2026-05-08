# Pract 4: Load Balancing Simulation using Round Robin and Random Selection
import random
from collections import defaultdict

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.rr_index = 0
        self.counts = defaultdict(int)

    def round_robin(self):
        server = self.servers[self.rr_index]
        self.rr_index = (self.rr_index + 1) % len(self.servers)
        self.counts[server] += 1
        return server

    def random_selection(self):
        server = random.choice(self.servers)
        self.counts[server] += 1
        return server

def simulate_requests():
    servers = ["Server A", "Server B", "Server C"]
    lb = LoadBalancer(servers)

    print("=== Round Robin ===")
    for i in range(10):
        server = lb.round_robin()
        print(f"Request {i+1:02d} -> {server}")

    print("\n=== Random Selection ===")
    for i in range(10):
        server = lb.random_selection()
        print(f"Request {i+1:02d} -> {server}")

    print("\nRequest distribution:")
    for server, count in lb.counts.items():
        print(f"{server}: {count}")

if __name__ == "__main__":
    simulate_requests()
