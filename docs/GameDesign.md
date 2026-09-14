# VendiStep Game Design

## Overview

VendiStep is a gamified pedometer and collectible game where
real-world walking earns tokens that can be spent on virtual
vending machines.

Players collect items of different rarities from themed vending
machines. The game is designed around everyday activity rather
than requiring dedicated workouts.

## Target Audience

Primary target:
- Adults roughly 18–40
- Casual mobile gamers
- People who enjoy collecting items
- Smartwatch users
- People looking for additional motivation to walk

The collectible themes should appeal to both men and women.

## Core Gameplay Loop

1. Player walks throughout the day.
2. Steps are tracked through the Android health system.
3. Every 5,000 steps awards a roll token.
4. Players can also receive tokens from login rewards.
5. Player selects a vending machine.
6. Player spends one token to roll.
7. The vending machine performs its animation.
8. An item is randomly selected based on rarity.
9. The item is added to the player's collection.
10. Player continues walking, collecting, and completing machines.

## Vending Machine Selection

Players have access to multiple themed vending machines.

The main vending-machine screen should visually place the machines
around the player.

The player can pan or rotate left and right to move between machines.

The visual effect should feel somewhat like looking through a
fisheye lens, giving the impression that the vending machines
surround the user.

## Initial Machine Themes

Two vending machines should be used initially to test the system.

Possible themes include:

- Designer monsters and robots
- Plastic / claw-machine-style toys
- Tiny food and everyday objects

Additional machine themes can be added later without changing the
core gameplay system.

## Collection

Each vending machine has its own collection.

Items that have not yet been obtained appear as grey silhouettes.

Obtained items display their full artwork and rarity.

Players can select an obtained item to inspect it.

## Duplicate Items

Duplicate items are allowed.

A duplicate should influence the player's next roll by increasing
the chance of receiving a non-duplicate item by 5%.

The exact stacking rules and maximum bonus still need to be defined.

## Future Expansion

Potential future systems:

- Additional vending machines
- Seasonal machines
- Limited collections
- Achievements
- Additional reward types
- Expanded smartwatch interactions