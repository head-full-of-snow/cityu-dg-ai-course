Search Problems
CS5491: Artificial Intelligence
Zhichao Lu
Content Credits:
Prof. Wei
's CS4486 Course
and
Prof. Boddeti
's AI Course

## Today

- Agents that Plan Ahead
- Search Problems
- Reading
  - Today's Lecture: RN Chapter 3.1-3.4
  - Next Lecture: RN Chapter 3.1-3.4

## Reminder: Rational Agents

- An agent is an entity that perceives
and acts.
- A rational agent selects actions that
maximize its (expected) utility.
- Characteristics of the percepts,
environment, and action space dictate techniques for selecting rational actions.

## Rational Agents

- Are rational agents omniscient
?
  - No - they are limited by what they can perceive
- Are rational agents clairvoyant
?
  - No - they lack knowledge of environment dynamics
- Do rational agents explore
and
learn
?
  - Yes - essential qualities required in unknown environments
- So, rational agents are not necessarily successful,
but they are autonomous
.

## Rational Agents

- Performance Measure
  - -1 per time step;+10 food; +500 win; -500 die;
+200 hit scared ghost
- Environment
  - Pacman dynamics + ghost behavior
- Actuators
  - North, West, East, South, Stop (idle)
- Sensors
  - entire state is visible

## Robotaxi - PEAS

- Performance Measure
  - income, happy customer, vehicle costs, fines, car, insurance
- Environment
  - streets, other drivers, customers, etc.
- Actuators
  - steering, brake, gas, display/speaker
- Sensors
  - cameras, lidar, radar, ultrasonic, accelerometer,
mechanical sensors, microphone, etc.

## Environment Categorization

|
Pacman
Robotaxi
|
Fully or Partially Observable
fully
| partial
|
Single or Multi Agent
multi
| multi
|
Deterministic or Stochastic
deterministic
| stochastic
|
Static or Dynamic
static
| dynamic
|
Discrete or Continuous
discrete
| continuous

## Environment Categorization

- Reflex agents:
  - Choose actions based on current observation (and maybe memory)
  - May have memory or a model of the world's current state.
  - Do not consider future consequences of actions
  - Consider how the world IS as opposed to how it would be.
- Can a reflex agent be rational?

## Agents that Plan Ahead

- Planning Agents:
  - Decision based on
predicted consequences
of actions
  - Must have a transition model
:
                            how the world evolves in responses to actions
  - Must formulate a goal
  - Consider how the world WOULD BE
as opposed to how it is
- Spectrum of Deliberativeness:
  - Generate complete, optimal plan offline, then execute
  - Generate simple, greedy plan, start executing, replan if necessary

## Search Problems

## What are Search Problems?

- A search problem
consists of:
  - A state space:
  - A successor function (actions, costs):
  - A start state and goal test
- A solution
is a sequence of actions (a plan) which transforms the start state to the goal test.

Search Problems Are Models

Example: Traveling in Romania
- State Space:
  - Cities
- Successor Function:
  - Roads: travel to adjacent city with cost=distance
- Start Space:
  - Arad
- Goal Test:
  - Is state == Bucharest?
- Solution?

## What is in a State Space?

World State: Includes every last detail of the environment
Search State: Keeps only details necessary for planning
- Problem: Pathing
  - States:
(x,y) position
  - Actions:
NEWS
  - Successor:
update location
  - Goal Test:
Is (x,y) == END
- Problem: Eat-All-Dots
  - States:
(x,y), boolean for each dot
  - Actions:
NEWS
  - Successor:
update location, boolean for dots
  - Goal Test:
All dot booleans are false

## Search Space Size

- World State
  - Agent Positions: 120
  - Food Count: 30
  - Ghost Positions: 12
  - Agent Orientation: NEWS
- Size
  - World States: 120 x 230 x 122 x 4
  - States for Pathing: 120
  - States for Eat-All-Dots: 120 x 230

Q & A
