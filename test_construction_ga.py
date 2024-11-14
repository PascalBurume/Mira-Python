# test_construction_ga.py

def test_data_initialization():
    """Test if the data is initialized correctly"""
    data = Data()
    
    print("\nTesting Data Initialization:")
    print("Number of machines:", len(data.machines))
    print("Machines:", [m.name for m in data.machines])
    print("\nNumber of labour types:", len(data.labour_names))
    print("Labour types:", [l.name for l in data.labour_names])
    print("\nConstruction sites and their activities:")
    for site, activities in data.sites.items():
        print(f"{site}: {activities}")

def test_schedule_generation():
    """Test if a schedule can be generated without errors"""
    print("\nTesting Schedule Generation:")
    schedule = Schedule()
    schedule.initialize()
    print("Initial schedule generated:")
    print_schedule(schedule)
    print("Number of conflicts:", schedule.num_conflicts)
    print("Fitness score:", schedule.calculate_fitness())

def test_genetic_operations():
    """Test genetic operations (crossover and mutation)"""
    print("\nTesting Genetic Operations:")
    
    # Create two parent schedules
    parent1 = Schedule()
    parent2 = Schedule()
    parent1.initialize()
    parent2.initialize()
    
    print("\nParent 1:")
    print_schedule(parent1)
    
    print("\nParent 2:")
    print_schedule(parent2)
    
    # Test crossover
    child = crossover_schedule(parent1, parent2)
    print("\nChild after crossover:")
    print_schedule(child)
    
    # Test mutation
    mutated = mutate_schedule(child)
    print("\nSchedule after mutation:")
    print_schedule(mutated)

def run_optimization_test(max_generations=10):
    """Run a short optimization test"""
    print("\nRunning Optimization Test:")
    generation_num = 0
    
    # Initialize population
    population = []
    for i in range(POPULATION_SIZE):
        schedule = Schedule()
        schedule.initialize()
        population.append(schedule)
    
    # Evolution loop
    while generation_num < max_generations:
        generation_num += 1
        print(f"\nGeneration #{generation_num}")
        
        population = sorted(population, key=lambda x: x.calculate_fitness(), reverse=True)
        best_schedule = population[0]
        
        print(f"Best fitness: {best_schedule.calculate_fitness()}")
        print(f"Number of conflicts: {best_schedule.num_conflicts}")
        
        if best_schedule.num_conflicts == 0:
            print("\nOptimal solution found!")
            print_schedule(best_schedule)
            break
            
        population = evolve_population(population)

def main_test():
    """Run all tests"""
    print("Starting Construction Schedule GA Tests")
    print("=======================================")
    
    test_data_initialization()
    test_schedule_generation()
    test_genetic_operations()
    run_optimization_test()

if __name__ == "__main__":
    from construction_ga import *  # Import all classes and functions from main file
    main_test()