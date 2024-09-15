
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
