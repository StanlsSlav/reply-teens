# %%
with open("output.txt", "w") as f:
    f.write("")

# %%
i = 0
current_budget = 0
final_budget = 0

slot_machines = []
slot_machines_used = 0

def reset_variables():
    global current_budget, final_budget, slot_machines, slot_machines_used
    
    current_budget = 0
    final_budget = 0

    slot_machines = []
    slot_machines_used = 0

# %%
class SlotMachine:
    def __init__(self, cost: int, reward: int):
        self.reward = reward
        self.cost = cost
        
    def play(self):
        global current_budget, slot_machines_used
        
        if not self.can_buy():
            raise Exception(f"Not enough money to buy {self.cost}")

        current_budget += self.reward - self.cost
        slot_machines_used += 1
        
    def can_buy(self):
        return current_budget >= self.cost
    
def parse_first_line(line):
    global total_slot_machines, final_budget, current_budget
    
    total_slot_machines = int(line[0])
    final_budget = int(line[1])
    current_budget = int(line[2])

def is_target_reached():
    global current_budget, final_budget
    return current_budget >= final_budget

def available_slots():
    global slot_machines
    return [x for x in slot_machines if x.can_buy()]

def minimum_used_slots():
    global slot_machines, current_budget, final_budget, slot_machines_used, i
    
    while not is_target_reached():
        # Get the highest rewarding available slot machines sorted by reward
        highest_rewarding = sorted(available_slots(), key=lambda x:x.reward - x.cost, reverse=True)[0]
        highest_rewarding.play()
        
    with open('output.txt', 'a') as f:
        i += 1
        output = f"Case #{i}: {slot_machines_used}\n"
        print(output)
        f.write(output)
        
    reset_variables()
    

# %%
with open('input.txt', 'r') as f:
    lines = f.readlines()
    test_cases = int(lines[0])
    
    for line in lines[1:]:
        line = line.strip().split(' ')
        if len(line) == 3:
            parse_first_line(line)
            continue

        cost = int(line[0])
        reward = int(line[1])

        slot_machines.append(SlotMachine(cost, reward))
        if total_slot_machines == len(slot_machines):
            minimum_used_slots()


