<img src="images/monty_hall_problem.png" alt="A description" width="600" height="200">


# Monty Hall Problem Simulation Interactive Dashboard

## Introduction
The Monty Hall problem is a famous probability puzzle based on a game show scenario: a contestant chooses one of three doors, one hiding a prize and two hiding goats. After the host reveals a goat behind one of the unchosen doors, the contestant can switch their choice or stay. This interactive dashboard lets you run customizable simulations to visualize how switching doors dramatically increases your winning probability from **33%** to **67%**, compared to staying with your original choice.

## Requirements
first add the folder to your PYTHONPATH:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

create a virtual enviroment using the code below:

```bash
conda create -n monty_hall python=3.12
```

run the code below in your command window:

```bash
pip install requirements.txt
```

## Usage
run the code below to run the interactive dashboard:

```bash
streamlit run src/app.py
```

## Project Structure
```
.
├─ README.md
├─ requirements.txt
└─ src
   ├─ monty_hall.py
   └─ app.py
```

## Results
The interactive dashboard clearly demonstrates the counterintuitive nature of the Monty Hall problem: switching doors after the host reveals a goat increases your winning probability to approximately **66.67%**, while staying with your initial choice yields only a **33.33%** success rate. This 2:1 advantage for switching holds consistently across thousands of simulations, proving that changing your decision is statistically the optimal strategy.