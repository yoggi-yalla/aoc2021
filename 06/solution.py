with open('input.txt') as f:
    data = f.read()

population = {i:0 for i in range(9)}

for x in data.split(','):
    population[int(x)] += 1

for iteration in range(256):
    if iteration == 80:
        print("Part 1:", sum(population.values())) # 362666

    new = population[0]
    for i in range(8):
        population[i] = population[i+1]    
    population[8] = new
    population[6] += new

print("Part 2:", sum(population.values())) # 1640526601595
