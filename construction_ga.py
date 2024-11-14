from prettytable import PrettyTable
import random

# Global constants
POPULATION_SIZE = 20
NUM_ELITE_SCHEDULES = 2
TOURNAMENT_SELECTION_SIZE = 5
MUTATION_RATE = 0.1
MAX_GENERATIONS = 100

class Data:
    def __init__(self):
        self.machines = []
        self.labour_working_hours = []
        self.labour_names = []
        self.activities = []
        self.sites = []
        self._initialize_data()

    def _initialize_data(self):
        # Initialize construction sites with their specific activities
        self.sites = {
            "Site 1": ["Piling", "Pile Cap", "Pier"],
            "Site 2": ["Pier", "Pier Cap"],
            "Site 3": ["Pier Cap", "Girder Erection", "Pier"]
        }
        
        # Initialize machines with working times
        self.machines.append(Machine("Piling Rig", "8:00-17:00"))
        self.machines.append(Machine("Crane", "8:00-17:00"))
        self.machines.append(Machine("Excavator", "8:00-17:00"))
        
        # Initialize labour working hours (shifts)
        self.labour_working_hours.append(LabourWorkingHour("Morning", "8:00-13:00"))
        self.labour_working_hours.append(LabourWorkingHour("Evening", "13:00-17:00"))
        
        # Initialize labour names with specific skills
        self.labour_names.append(LabourName("Piling Crew"))
        self.labour_names.append(LabourName("Structure Crew"))
        self.labour_names.append(LabourName("General Workers"))
        
        # Initialize activities with durations and required labor
        self.activities.extend([
            Activity(1, "Piling", "Piling Crew", 5),
            Activity(2, "Pile Cap", "Structure Crew", 3),
            Activity(3, "Pier", "Structure Crew", 4),
            Activity(4, "Pier Cap", "Structure Crew", 3),
            Activity(5, "Girder Erection", "Structure Crew", 4)
        ])

class Schedule:
    def __init__(self):
        self.classes = []
        self.num_conflicts = 0
        self.fitness = -1
        self.class_num = 0
        self.data = Data()
    
    def initialize(self):
        # Create schedule ensuring activities are assigned to appropriate sites
        for site_name, site_activities in self.data.sites.items():
            for activity_name in site_activities:
                activity = next((a for a in self.data.activities if a.name == activity_name), None)
                if activity:
                    new_class = Class(self.class_num)
                    new_class.set_construction_site(site_name)
                    new_class.set_activity(activity)
                    
                    # Assign appropriate machine based on activity
                    if activity_name == "Piling":
                        machine = next(m for m in self.data.machines if m.name == "Piling Rig")
                    elif activity_name == "Girder Erection":
                        machine = next(m for m in self.data.machines if m.name == "Crane")
                    else:
                        machine = self.data.machines[random.randrange(0, len(self.data.machines))]
                    new_class.set_machine(machine)
                    
                    # Assign appropriate labor based on activity
                    labor = next(l for l in self.data.labour_names if l.name == activity.labour)
                    new_class.set_labour_name(labor)
                    
                    new_class.set_labour_working_hour(
                        self.data.labour_working_hours[random.randrange(0, len(self.data.labour_working_hours))]
                    )
                    
                    self.classes.append(new_class)
                    self.class_num += 1

    def calculate_fitness(self):
        self.num_conflicts = 0
        classes = self.get_classes()
        
        for i in range(len(classes)):
            for j in range(len(classes)):
                if i != j:
                    # Check machine conflicts
                    if (classes[i].get_machine() == classes[j].get_machine() and 
                        classes[i].get_labour_working_hour() == classes[j].get_labour_working_hour()):
                        self.num_conflicts += 1
                    
                    # Check labour conflicts
                    if (classes[i].get_labour_name() == classes[j].get_labour_name() and 
                        classes[i].get_labour_working_hour() == classes[j].get_labour_working_hour()):
                        self.num_conflicts += 1
                    
                    # Check site conflicts (same activity can't happen simultaneously at different sites)
                    if (classes[i].get_activity().name == classes[j].get_activity().name and 
                        classes[i].get_construction_site() != classes[j].get_construction_site() and
                        classes[i].get_labour_working_hour() == classes[j].get_labour_working_hour()):
                        self.num_conflicts += 1
        
        self.fitness = 1 / (1.0 * self.num_conflicts + 1)
        return self.fitness

    def get_classes(self):
        return self.classes

class Class:
    def __init__(self, class_num):
        self.class_num = class_num
        self.construction_site = None
        self.activity = None
        self.machine = None
        self.labour_name = None
        self.labour_working_hour = None
    
    def get_construction_site(self): return self.construction_site
    def get_activity(self): return self.activity
    def get_machine(self): return self.machine
    def get_labour_name(self): return self.labour_name
    def get_labour_working_hour(self): return self.labour_working_hour
    
    def set_construction_site(self, construction_site): self.construction_site = construction_site
    def set_activity(self, activity): self.activity = activity
    def set_machine(self, machine): self.machine = machine
    def set_labour_name(self, labour_name): self.labour_name = labour_name
    def set_labour_working_hour(self, labour_working_hour): self.labour_working_hour = labour_working_hour

class Machine:
    def __init__(self, name, working_time):
        self.name = name
        self.working_time = working_time

class LabourName:
    def __init__(self, name):
        self.name = name

class LabourWorkingHour:
    def __init__(self, shift, hours):
        self.shift = shift
        self.hours = hours

class Activity:
    def __init__(self, number, name, labour, duration):
        self.number = number
        self.name = name
        self.labour = labour
        self.duration = duration

def evolve_population(population):
    return mutate_population(crossover_population(population))

def crossover_population(population):
    crossover_pop = []
    
    # Keep elite schedules
    for i in range(NUM_ELITE_SCHEDULES):
        crossover_pop.append(population[i])
    
    # Create new schedules through crossover
    i = NUM_ELITE_SCHEDULES
    while i < POPULATION_SIZE:
        schedule1 = select_tournament_population(population)
        schedule2 = select_tournament_population(population)
        crossover_pop.append(crossover_schedule(schedule1, schedule2))
        i += 1
    
    return crossover_pop

def mutate_population(population):
    for i in range(NUM_ELITE_SCHEDULES, POPULATION_SIZE):
        mutate_schedule(population[i])
    return population

def crossover_schedule(schedule1, schedule2):
    crossover_schedule = Schedule()
    crossover_point = random.randint(0, len(schedule1.get_classes()) - 1)
    
    # First part from schedule1
    for i in range(crossover_point):
        crossover_schedule.classes.append(schedule1.get_classes()[i])
    
    # Second part from schedule2
    for i in range(crossover_point, len(schedule2.get_classes())):
        crossover_schedule.classes.append(schedule2.get_classes()[i])
    
    return crossover_schedule

def mutate_schedule(schedule):
    if random.random() < MUTATION_RATE:
        # Select two random classes and swap their working hours
        idx1, idx2 = random.sample(range(len(schedule.get_classes())), 2)
        temp_hour = schedule.get_classes()[idx1].get_labour_working_hour()
        schedule.get_classes()[idx1].set_labour_working_hour(schedule.get_classes()[idx2].get_labour_working_hour())
        schedule.get_classes()[idx2].set_labour_working_hour(temp_hour)
    return schedule

def select_tournament_population(pop):
    tournament_pop = []
    for i in range(TOURNAMENT_SELECTION_SIZE):
        tournament_pop.append(pop[random.randrange(0, POPULATION_SIZE)])
    tournament_pop = sorted(tournament_pop, key=lambda x: x.calculate_fitness(), reverse=True)
    return tournament_pop[0]

def print_schedule(schedule):
    table = PrettyTable()
    table.field_names = ["Class #", "Site", "Activity", "Duration", "Machine", "Labour", "Working Hours"]
    
    classes = schedule.get_classes()
    for i in range(0, len(classes)):
        table.add_row([
            classes[i].class_num,
            classes[i].get_construction_site(),
            classes[i].get_activity().name,
            classes[i].get_activity().duration,
            classes[i].get_machine().name,
            classes[i].get_labour_name().name,
            classes[i].get_labour_working_hour().hours
        ])
    
    print(table)

def main():
    generation_num = 0
    print("Generation # " + str(generation_num))
    
    # Initialize population
    population = []
    for i in range(POPULATION_SIZE):
        schedule = Schedule()
        schedule.initialize()
        population.append(schedule)
    
    # Sort population by fitness
    population = sorted(population, key=lambda x: x.calculate_fitness(), reverse=True)
    print_schedule(population[0])
    print("Fitness: " + str(population[0].calculate_fitness()))
    print("Conflicts: " + str(population[0].num_conflicts))
    
    # Evolution loop
    while population[0].num_conflicts > 0 and generation_num < MAX_GENERATIONS:
        generation_num += 1
        print("\nGeneration # " + str(generation_num))
        population = evolve_population(population)
        population = sorted(population, key=lambda x: x.calculate_fitness(), reverse=True)
        print_schedule(population[0])
        print("Fitness: " + str(population[0].calculate_fitness()))
        print("Conflicts: " + str(population[0].num_conflicts))

if __name__ == '__main__':
    main()