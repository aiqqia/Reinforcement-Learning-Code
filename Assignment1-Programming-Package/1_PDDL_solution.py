"""
Assignment 1 - Problem 1 PDDL testing script.

* Group Member 1:
    - Name: Ayush Goyal
    - Student ID: A0274831B

* Group Member 2:
    - Name: Poornima Sridhara
    - Student ID: A0274976H
    
* Collaborators: None

* Sources:
    - https://fai.cs.uni-saarland.de/teaching/winter18-19/planning-material/planning03-pddl-post-handout.pdf
"""

import numpy as np

### AFTER YOU COMPLETE THE 1_PDDL.ipynb, COPY YOUR CODES HERE FOR OUR EVALUATION ###

# COPY-FLAG-1-START

pddl_domain = """
(define (domain elevator)
  (:types 
    level person ; Define types for levels and persons
  )
  
  (:predicates
    (elevator_at ?l - level) ; The elevator is at a specific level
    (person_at ?p - person ?l - level) ; A person is at a specific level
    (person_in_elevator ?p - person) ; A person is in the elevator
    (elevator_empty) ; The elevator is empty
    (door_open ?l - level) ; The door is open at a specific level
    (adjacent_up ?from ?to - level) ; Defines that ?to is the level above ?from
    (adjacent_down ?from ?to - level) ; Defines that ?to is the level below ?from
  )
  
  ; move_up: The elevator can only move up one level
  (:action move_up
    :parameters (?from ?to - level)
    :precondition (and (elevator_at ?from) ;
                      (adjacent_up ?from ?to) ;
                      (elevator_empty) ;
                      (not (door_open ?from))) ; FILL IN the precondition for move_up
    :effect (and (not(elevator_at ?from)) ;
                (elevator_at ?to)) ; FILL IN the effect for move_up
  )

  ; move_down: The elevator can only move down one level
  (:action move_down
    :parameters (?from ?to - level)
    :precondition (and (elevator_at ?from) ;
                      (adjacent_down ?from ?to) ;
                      (not (door_open ?from))) ; FILL IN the precondition for move_down
    :effect (and (not(elevator_at ?from)) ;
                (elevator_at ?to)) ; FILL IN the effect for move_down
  )

  ; open_door: Open the door without considering picking up people
  (:action open_door
    :parameters (?l - level)
    :precondition (and (elevator_at ?l) ;
                      (not (door_open ?l))) ; FILL IN the precondition for open_door
    :effect (and (door_open ?l)) ; FILL IN the effect for open_door
  )

  ; close_door: Close the door
  (:action close_door
    :parameters (?l - level)
    :precondition (and (elevator_at ?l) ;
                      (door_open ?l)) ; FILL IN the precondition for close_door
    :effect (and (not (door_open ?l))) ; FILL IN the effect for close_door
  )

  ; load: Pick up a person, requires the door to be open and the elevator to be empty
  (:action load
    :parameters (?p - person ?l - level)
    :precondition (and (elevator_at ?l) ;
                      (door_open ?l) ;
                      (elevator_empty) ;
                      (person_at ?p ?l)) ; FILL IN the precondition for load
    :effect (and (not(elevator_empty)) ;
                  (not(person_at ?p ?l)) ;
                  (person_in_elevator ?p)) ; FILL IN the effect for load
  )

  ; unload: Drop off a person, requires the door to be open and the person to be in the elevator
  (:action unload
    :parameters (?p - person ?l - level)
    :precondition (and (elevator_at ?l) ;
                      (door_open ?l) ;
                      (not(elevator_empty)) ;
                      (person_in_elevator ?p)) ; FILL IN the precondition for unload
    :effect (and (not(person_in_elevator ?p));
                  (elevator_empty) ;
                  (person_at ?p ?l)) ; FILL IN the effect for unload
  )
)
"""


# COPY-FLAG-1-END

def generate_pddl_domain():
    with open("elevator_domain.pddl", "w") as file:
        file.write(pddl_domain)


# COPY-FLAG-2-START


def generate_pddl_from_config(config_map, output_file):
    num_levels = len(config_map)
    persons = [f"person{i + 1}" for i in range(np.sum(config_map))]

    # PDDL header
    pddl = "(define (problem elevator_problem)\n"
    pddl += "  (:domain elevator)\n"

    # Objects
    levels = " ".join([f"level{i}" for i in range(num_levels)])
    persons_str = " ".join(persons)
    pddl += f"  (:objects\n    {levels} - level\n    {persons_str} - person\n  )\n\n"

    # Initial state
    pddl += "  (:init\n"
    pddl += "    (elevator_at level0)\n"  # Assuming elevator starts at level 0

    person_idx = 0
    for level, has_person in enumerate(config_map):
        if has_person:
            person = persons[person_idx]
            pddl += f"    (person_at {person} level{level})\n"
            person_idx += 1

    # Add elevator states and adjacencies
    pddl += "    (elevator_empty)\n"
    for i in range(num_levels - 1):
        pddl += f"    (adjacent_up level{i} level{i+1})\n"  # Fill in this line to define adjacency up
        pddl += f"    (adjacent_down level{i+1} level{i})\n"  # Fill in this line to define adjacency down

    pddl += "  )\n\n"

    # Goal state
    pddl += "  (:goal\n"
    pddl += "    (and\n"
    for person in persons:
        pddl += f"      (person_at {person} level0)\n"  # Fill in this line to define the goal for each person
    pddl += "    )\n"
    pddl += "  )\n"
    pddl += ")"

    # Save PDDL to file
    with open(output_file, 'w') as file:
        file.write(pddl)

    return pddl

# COPY-FLAG-2-END
