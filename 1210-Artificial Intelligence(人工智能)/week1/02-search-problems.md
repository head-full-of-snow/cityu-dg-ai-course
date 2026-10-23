# Search Problems

CS5491: Artificial Intelligence

ZHICHAO LU

Content Credits: Prof. Wei's CS4486 Course and Prof. Boddeti's AI Course

# TODAY

Agents that Plan Ahead

Search Problems

Reading

• Today's Lecture: RN Chapter 3.1-3.4

• Next Lecture: RN Chapter 3.1-3.4

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F04efc607ef9445ae84d5577ba82622c5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089656&Signature=YySUVyBjSTL3Hc%2Bl%2BlX0c0lBfLw%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fb288c1f1ce5d4e19a41bc09f159cf57a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089656&Signature=5icfGxO%2BzO2v10nGHIizj8ZCx3E%3D)

# REMINDER: RATIONAL AGENTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F6ccd752c097f4b81acc823e554a6dfb1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089656&Signature=TwiOGP9Lv5o1Z8%2BvdubOLZYotaY%3D)

# REMINDER: RATIONAL AGENTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F33280c0902944c9abf88029dc530ed7a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089656&Signature=iQWo7OxNDrr4ukse87i1RWtUK8c%3D)

An agent is an entity that perceives and acts.

# REMINDER: RATIONAL AGENTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F64c0943c28744dab90656034ee4261c1.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089656&Signature=uCRETkX4dGDwPdVgH1BliIdldq0%3D)

An agent is an entity that perceives and acts.

A rational agent selects actions that maximize its (expected) utility.

# REMINDER: RATIONAL AGENTS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F8786fa461436461bbc2494007024e6e2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=PEsV5RAHAWHns6xbCauZUJnsl7g%3D)

New state  $ s_{t+1} $

Action  $ a_{t} $

Environment

An agent is an entity that perceives and acts.

A rational agent selects actions that maximize its (expected) utility.

Characteristics of the percepts, environment, and action space dictate techniques for selecting rational actions.

# RATIONAL AGENTS

# RATIONAL AGENTS

Are rational agents omniscient?

# RATIONAL AGENTS

# Are rational agents omniscient?

No - they are limited by what they can perceive

# RATIONAL AGENTS

Are rational agents omniscient?

• No - they are limited by what they can perceive

Are rational agents clairvoyant?

# RATIONAL AGENTS

Are rational agents omniscient?

• No - they are limited by what they can perceive

Are rational agents clairvoyant?

No - they lack knowledge of environment dynamics

# RATIONAL AGENTS

Are rational agents omniscient?

• No - they are limited by what they can perceive

Are rational agents clairvoyant?

• No - they lack knowledge of environment dynamics

Do rational agents explore and learn?

# RATIONAL AGENTS

Are rational agents omniscient?

• No - they are limited by what they can perceive

Are rational agents clairvoyant?

• No - they lack knowledge of environment dynamics

Do rational agents explore and learn?

• Yes - essential qualities required in unknown environments

# RATIONAL AGENTS

Are rational agents omniscient?

• No - they are limited by what they can perceive

Are rational agents clairvoyant?

• No - they lack knowledge of environment dynamics

Do rational agents explore and learn?

• Yes - essential qualities required in unknown environments

So, rational agents are not necessarily successful, but they are autonomous.

# RATIONAL AGENTS

Performance Measure

Environment

Actuators

Sensors

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F91f56137df9e4151814b780db04a4acd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=OI2GJtCucSUnJz0CZNOl1jhi1eE%3D)

# RATIONAL AGENTS

Performance Measure

- -1 per time step; +10 food; +500 win; -500 die; +200 hit scared ghost

Environment

Pacman dynamics + ghost behavior

Actuators

• North, West, East, South, Stop (idle)

Sensors

entire state is visible

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fb40deb193d4c4ece98c82f88f84d35b8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=5OlmgEO45gVM1IapyJPTN9kYf0s%3D)

# ROBOTAXI - PEAS

# Performance Measure

Environment

Actuators

Sensors

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F1ddeae1a28a44d6ca0618fb7fef00f7f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=0Tur5dSG50b6cK70SKRIaH59yQA%3D)

# ROBOTAXI - PEAS

Performance Measure

• income, happy customer, vehicle costs, fines, car, insurance

Environment

• streets, other drivers, customers, etc.

Actuators

• steering, brake, gas, display/speaker

Sensors

- cameras, lidar, radar, ultrasonic, accelerometer, mechanical sensors, microphone, etc.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F38bdd6dab43840b099debb45293f2d39.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=5zkS1TEkWwxrWXhjol6gA%2FJY%2BiA%3D)

# ENVIRONMENT CATEGORIZATION

# ENVIRONMENT CATEGORIZATION

<table><tr><td></td><td>Pacman</td><td>Robotaxi</td></tr><tr><td>Fully or Partially Observable</td><td>fully</td><td>partial</td></tr><tr><td>Single or Multi Agent</td><td>multi</td><td>multi</td></tr><tr><td>Deterministic or Stochastic</td><td>deterministic</td><td>stochastic</td></tr><tr><td>Static or Dynamic</td><td>static</td><td>dynamic</td></tr><tr><td>Discrete or Continuous</td><td>discrete</td><td>continuous</td></tr></table>

# ENVIRONMENT CATEGORIZATION

# Reflex agents:

• Choose actions based on current observation (and maybe memory)

• May have memory or a model of the world's current state.

• Do not consider future consequences of actions

Consider how the world IS as opposed to how it would be.

Can a reflex agent be rational?

# AGENTS THAT PLAN AHEAD

Planning Agents:

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

# AGENTS THAT PLAN AHEAD

# Planning Agents:

• Decision based on predicted consequences of actions

• Must have a transition model : how the world evolves in responses to actions

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

• Must have a transition model : how the world evolves in responses to actions

• Must formulate a goal

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

- Must have a transition model: how the world evolves in responses to actions

Must formulate a goal

• Consider how the world WOULD BE as opposed to how it is

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

- Must have a transition model : how the world evolves in responses to actions

Must formulate a goal

• Consider how the world WOULD BE as opposed to how it is Spectrum of Deliberativeness:

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

• Must have a transition model: how the world evolves in responses to actions

Must formulate a goal

• Consider how the world WOULD BE as opposed to how it is Spectrum of Deliberativeness:

• Generate complete, optimal plan offline, then execute

# AGENTS THAT PLAN AHEAD

# Planning Agents:

Decision based on predicted consequences of actions

- Must have a transition model : how the world evolves in responses to actions

Must formulate a goal

• Consider how the world WOULD BE as opposed to how it is Spectrum of Deliberativeness:

• Generate complete, optimal plan offline, then execute

• Generate simple, greedy plan, start executing, replan if necessary

# SEARCH PROBLEMS

# WHAT ARE SEARCH PROBLEMS?

A search problem consists of:

# WHAT ARE SEARCH PROBLEMS?

A search problem consists of:

• A state space:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F3690495db3684e94af8e463c6fed1c68.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=Cmf5i%2FCURL%2B%2FKLu%2F%2BaC%2Fr6Hvp0E%3D)

# WHAT ARE SEARCH PROBLEMS?

A search problem consists of:

• A state space:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fea43c555a8fd479bbf28d75757b14838.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=FQ%2FZWZ8H5WQWnX9pQvyls%2Bspx6Y%3D)

• A successor function (actions, costs):

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fe4c7f53ea59a4e6b9e1f224771caee4a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=GpKINjOHqlx38a4gdDiC27mVLrE%3D)

# WHAT ARE SEARCH PROBLEMS?

A search problem consists of:

• A state space:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Ff9317275f0164f828ca42634fbe734b5.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089657&Signature=cEzm99gkoaNW4t42zFUNzdpD0yg%3D)

• A successor function (actions, costs):

• A start state and goal test

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F2f7ddc342de4460a81f2544933f42bc7.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=caYHo%2FIwjrnoo%2BZGfC%2FF68TJJ%2FU%3D)

# WHAT ARE SEARCH PROBLEMS?

A search problem consists of:

• A state space:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F22e27e6fdad04585bddde19e52af9539.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=S59fe2axBlUS9p0eetBoaknIRdw%3D)

• A successor function (actions, costs):

• A start state and goal test

A solution is a sequence of actions (a plan) which transforms the start state to the goal test.

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F8141792d3bc8497eaa958297997662ba.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=ulEhAdMVpL1eWzUy4nmbLMo6nj0%3D)

# SEARCH PROBLEMS ARE MODELS

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fd2fb6234c6554dbf96a0d2151011fd87.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=70Liu9Zx92KZsd1ERhjB70jFnBI%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fef00687b3a054088946387c1503617b2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=PS2qylR5RoDYy6ADEz8h%2BEYXaZ8%3D)

# EXAMPLE: TRAVELING IN ROMANIA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Ff98ab21a022743f3a0fdf360d6994161.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=1A%2BAdUOa3vjn0SjD6OkeSd03Iuk%3D)

# EXAMPLE: TRAVELING IN ROMANIA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F0d57c2226517473aa41bdbc820292ba8.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=yCOHpqI06cIKyXOZX9OQbLzwFEs%3D)

State Space:

Successor Function:

Start Space:

Goal Test:

Solution?

# EXAMPLE: TRAVELING IN ROMANIA

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F1b16e5859f9944fa87bc31510558795a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=MjRqZhvzWqTuMPfICs5JDjYUnQo%3D)

# State Space:

• Cities

Successor Function:

- Roads: travel to adjacent city with cost=distance

# Start Space:

• Arad

Goal Test:

• Is state == Bucharest?

Solution?

# WHAT IS IN A STATE SPACE?

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F57cb8f1040824033b39dbf484d6eb1dd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=%2F%2FaxvONKPC2BRNJm3N3%2FmpzmB58%3D)

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fb4b567fd627a4f058bed6dc73f6ffbf2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089658&Signature=SN68HnxcMF0DcfmN02GphdHmVmA%3D)

Search State: Keeps only details necessary for planning

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fb1adaac4a2424f88ba67808a62b435a0.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=vbKxQZGBFj5YzUVIvgfCf565TQU%3D)

Search State: Keeps only details necessary for planning

# Problem: Pathing

States:

• Actions:

Successor:

• Goal Test:

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F059b621c2bdc4ffc8da9671b59e1556a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=89mjRyxetPjHgQlFl%2BsDHT7SVYM%3D)

Search State: Keeps only details necessary for planning

# Problem: Pathing

• States: (x,y) position

• Actions: NEWS

Successor: update location

• Goal Test: Is  $ (x,y) == END $

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F7dde92e03cea4f178a6ceb13be9fb207.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=iWxdOck3r%2BwvKyoktX3KwrHSVrw%3D)

Search State: Keeps only details necessary for planning

# Problem: Pathing

• States: (x,y) position

• Actions: NEWS

Successor: update location

• Goal Test: Is  $ (x,y) == END $

• States:

Actions:

Problem: Eat-All-Dots

Successor:

• Goal Test:

# WHAT IS IN A STATE SPACE?

World State: Includes every last detail of the environment

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F6be308387a2a4e06ae409ea27de9d5c2.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=MGkF1FhTDDbGHySQYHgAamqLuoA%3D)

Search State: Keeps only details necessary for planning

# Problem: Pathing

• States: (x,y) position

• Actions: NEWS

Successor: update location

• Goal Test: Is  $ (x,y) == END $

• States: (x,y), boolean for each dot

Problem: Eat-All-Dots

• Actions: NEWS

• Successor: update location, boolean for dots

• Goal Test: All dot booleans are false

# SEARCH SPACE SIZE

World State

• Agent Positions:

• Food Count:

• Ghost Positions:

Agent Orientation:

Size

• World States:

• States for Pathing:

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F1ca76653acb84dd4b39568c7a5d09ffd.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=QOhdKMkHgs5I62JmGSHTuIc35l8%3D)

• States for Eat-All-Dots:

# SEARCH SPACE SIZE

World State

• Agent Positions: 120

• Food Count: 30

• Ghost Positions: 12

Agent Orientation: NEWS

Size

• World States:  $ 120 \times 2^{30} \times 12^{2} \times 4 $

• States for Pathing: 120

• States for Eat-All-Dots: 120 x 230

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2Fe462824e811f49d0b3c6ee24f4298925.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=qV8t3GKIpQi2RJ8ENRDy8W%2F%2FRtw%3D)

# Q & A

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F64bd5ed382534eecbab9b218d5381743%2Fmedia%2F349b31722071413eb88afff4f4fc8121.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1800089659&Signature=h%2FeVwBLpRcwLEJyLysLorbM6Luk%3D)
