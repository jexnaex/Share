costs = [1, 3 , 5, 7, 9]

def cost(items):
    total_cost = 0
    for x in items:
        total_cost += x
    return total_cost

a = cost(costs)
print a
