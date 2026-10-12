import random
participants = ["Alice", "Bob", "Charlie", "David", "Emma"]
# Pick 2 unique winners for a prize
winners = random.sample(participants, k=2)
print(f"Winners: {winners}")  # Guaranteed to be two different people