first_string = input()
second_string = input()

first_list = first_string.split()
second_list = second_string.split()
N = len(first_list)

alice = []
bob = []
alice_number = 0
bob_number = 0
for item1 in first_list:
    alice.append(int(item1))

for item2 in second_list:
    bob.append(int(item2))

for item in range(0,N):
    if alice[item]>bob[item]:
        alice_number = alice_number + 1
    if alice[item]<bob[item]:
        bob_number = bob_number + 1
print(f"{alice_number} {bob_number}")
