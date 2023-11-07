import random
from Calculate_pump import CalculatePump

class GeneticPumpOptimizer:
    def __init__(self, target_vpm, population_size=100, mutation_rate=0.05, generations=1000):
        self.target_vpm = target_vpm
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def fitness(self, pump):
        return 1 / (1 + abs(pump.vpm() - self.target_vpm)**2)

    def crossover(self, parent1, parent2):
        child_radius = random.choice([parent1.radius, parent2.radius])
        child_teethDiameterRatio = random.choice([parent1.teethDiameterRatio, parent2.teethDiameterRatio])
        child_teethDiameterRatio = max(3, min(10, child_teethDiameterRatio))  # Ensure it's within the desired range
        child_angleSpeed = random.choice([parent1.angleSpeed, parent2.angleSpeed])
        child_angleSpeed = max(1, min(10, child_angleSpeed))  # Ensure it's within the range of 1 to 10
        child_pump = CalculatePump(child_radius, child_teethDiameterRatio, child_angleSpeed)
        return self.validate_pump(child_pump)
    
    def mutate(self, pump):
        if random.random() < self.mutation_rate:
            pump.radius += random.uniform(-0.01, 0.01)
        if random.random() < self.mutation_rate:
            pump.teethDiameterRatio += random.uniform(-2, 2)
            pump.teethDiameterRatio = max(3, min(10, pump.teethDiameterRatio))  # Ensure it's within the desired range
        if random.random() < self.mutation_rate:
            pump.angleSpeed += random.uniform(-1, 1)
            pump.angleSpeed = max(1, min(10, pump.angleSpeed))  # Ensure it's within the range of 1 to 10
        return self.validate_pump(pump)
    
    def validate_pump(self, pump):
        if pump.teethDiameter >= pump.radius:
            pump.teethDiameter = pump.radius * 0.8  # or some other adjustment logic
            pump.teethDiameterRatio = pump.radius / pump.teethDiameter
        
        pump.teethDiameterRatio = max(3, min(10, pump.teethDiameterRatio))
        pump.angleSpeed = max(1, min(10, pump.angleSpeed))  # Ensure it's within the range of 1 to 10
        return pump

    def run(self):
        population = [CalculatePump(random.uniform(0.01, 0.5), random.randint(3, 10), random.uniform(1, 10)) for _ in range(self.population_size)]
        
        for _ in range(self.generations):
            population.sort(key=self.fitness, reverse=True)
            
            # Introduce more variety into the population
            if _ % 100 == 0 and _ != 0:  # Every 100 generations
                population[-10:] = [CalculatePump(random.uniform(0.01, 0.5), random.uniform(3, 10), random.uniform(1, 10)) for _ in range(10)]
            
            new_population = []

            while len(new_population) < self.population_size:
                parents = random.choices(population[:50], k=2)  # Select two parents from top 50 solutions
                child = self.crossover(parents[0], parents[1])
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

        best_pump = population[0]
        return best_pump

# Example usage:
if __name__ == "__main__":
    target_vpm = 2  # Adjust this value as needed
    optimizer = GeneticPumpOptimizer(target_vpm)
    best_pump = optimizer.run()
    
    print(f"Optimized parameters to achieve close to {target_vpm} VPM are:")
    print(f"Radius: {round(best_pump.radius*1000, 4)} mm")
    print(f"Teeth Diameter Ratio: {round(best_pump.teethDiameterRatio, 2)}")
    print(f"Teeth Diameter: {round(best_pump.teethDiameter*1000, 4)} mm")
    print(f"Angle Speed: {round(best_pump.angleSpeed, 2)} rad/s")
    print(f"Depth: {round(best_pump.depth*1000, 4)} mm")
    print(f"Number of Teeth: {best_pump.numberOfTeeth()}")
    print(f"Calculated VPM: {round(best_pump.vpm(), 2)}")
    

