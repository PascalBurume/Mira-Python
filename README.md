# Mira Python

This project demonstrates the use of a Genetic Algorithm (GA) to optimize construction schedules. The algorithm assigns activities to construction sites, schedules machines, and allocates labor efficiently while minimizing conflicts.

## Features
- **Genetic Algorithm**: Utilizes crossover and mutation operations to evolve schedules.
- **Conflict Management**: Ensures that machines and labor are not double-booked.
- **Fitness Calculation**: Measures the effectiveness of a schedule based on conflicts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PascalBurume/Mira-Python.git
   cd Mira-Python
   ```
## Result
    Starting Construction Schedule GA Tests
=======================================

Testing Data Initialization:

Number of machines: 3  
Machines: `['Piling Rig', 'Crane', 'Excavator']`

Number of labour types: 3  
Labour types: `['Piling Crew', 'Structure Crew', 'General Workers']`

Construction sites and their activities:

- **Site 1**: `['Piling', 'Pile Cap', 'Pier']`
- **Site 2**: `['Pier', 'Pier Cap']`
- **Site 3**: `['Pier Cap', 'Girder Erection', 'Pier']`

Testing Schedule Generation:

**Initial schedule generated:**

| Class # |  Site  |     Activity    | Duration |   Machine   |     Labour     | Working Hours |
|:-------:|:------:|:---------------:|:--------:|:-----------:|:--------------:|:-------------:|
|    0    | Site 1 |     Piling      |     5    | Piling Rig  |  Piling Crew   |  8:00-13:00   |
|    1    | Site 1 |    Pile Cap     |     3    |  Excavator  | Structure Crew | 13:00-17:00   |
|    2    | Site 1 |      Pier       |     4    | Piling Rig  | Structure Crew | 13:00-17:00   |
|    3    | Site 2 |      Pier       |     4    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    4    | Site 2 |    Pier Cap     |     3    |  Excavator  | Structure Crew |  8:00-13:00   |
|    5    | Site 3 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    6    | Site 3 | Girder Erection |     4    |    Crane    | Structure Crew |  8:00-13:00   |
|    7    | Site 3 |      Pier       |     4    |    Crane    | Structure Crew | 13:00-17:00   |

Number of conflicts: 0  
Fitness score: 0.034482758620689655

Testing Genetic Operations:

**Parent 1:**

| Class # |  Site  |     Activity    | Duration |   Machine   |     Labour     | Working Hours |
|:-------:|:------:|:---------------:|:--------:|:-----------:|:--------------:|:-------------:|
|    0    | Site 1 |     Piling      |     5    | Piling Rig  |  Piling Crew   | 13:00-17:00   |
|    1    | Site 1 |    Pile Cap     |     3    |  Excavator  | Structure Crew |  8:00-13:00   |
|    2    | Site 1 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    3    | Site 2 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    4    | Site 2 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    5    | Site 3 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    6    | Site 3 | Girder Erection |     4    |    Crane    | Structure Crew | 13:00-17:00   |
|    7    | Site 3 |      Pier       |     4    | Piling Rig  | Structure Crew | 13:00-17:00   |

**Parent 2:**

| Class # |  Site  |     Activity    | Duration |  Machine  |     Labour     | Working Hours |
|:-------:|:------:|:---------------:|:--------:|:---------:|:--------------:|:-------------:|
|    0    | Site 1 |     Piling      |     5    | Piling Rig|  Piling Crew   |  8:00-13:00   |
|    1    | Site 1 |    Pile Cap     |     3    |   Crane   | Structure Crew | 13:00-17:00   |
|    2    | Site 1 |      Pier       |     4    | Piling Rig| Structure Crew | 13:00-17:00   |
|    3    | Site 2 |      Pier       |     4    | Excavator | Structure Crew |  8:00-13:00   |
|    4    | Site 2 |    Pier Cap     |     3    | Piling Rig| Structure Crew |  8:00-13:00   |
|    5    | Site 3 |    Pier Cap     |     3    |   Crane   | Structure Crew | 13:00-17:00   |
|    6    | Site 3 | Girder Erection |     4    |   Crane   | Structure Crew |  8:00-13:00   |
|    7    | Site 3 |      Pier       |     4    | Excavator | Structure Crew | 13:00-17:00   |

**Child after crossover:**

| Class # |  Site  |     Activity    | Duration |   Machine   |     Labour     | Working Hours |
|:-------:|:------:|:---------------:|:--------:|:-----------:|:--------------:|:-------------:|
|    0    | Site 1 |     Piling      |     5    | Piling Rig  |  Piling Crew   | 13:00-17:00   |
|    1    | Site 1 |    Pile Cap     |     3    |  Excavator  | Structure Crew |  8:00-13:00   |
|    2    | Site 1 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    3    | Site 2 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    4    | Site 2 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    5    | Site 3 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    6    | Site 3 | Girder Erection |     4    |    Crane    | Structure Crew |  8:00-13:00   |
|    7    | Site 3 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |

**Schedule after mutation:**

| Class # |  Site  |     Activity    | Duration |   Machine   |     Labour     | Working Hours |
|:-------:|:------:|:---------------:|:--------:|:-----------:|:--------------:|:-------------:|
|    0    | Site 1 |     Piling      |     5    | Piling Rig  |  Piling Crew   | 13:00-17:00   |
|    1    | Site 1 |    Pile Cap     |     3    |  Excavator  | Structure Crew |  8:00-13:00   |
|    2    | Site 1 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    3    | Site 2 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
|    4    | Site 2 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    5    | Site 3 |    Pier Cap     |     3    | Piling Rig  | Structure Crew |  8:00-13:00   |
|    6    | Site 3 | Girder Erection |     4    |    Crane    | Structure Crew |  8:00-13:00   |
|    7    | Site 3 |      Pier       |     4    |  Excavator  | Structure Crew | 13:00-17:00   |
