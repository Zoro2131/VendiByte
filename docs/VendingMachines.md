# VendiStep Vending Machines

## Machine Selection

The main game screen presents the player's available vending
machines.

Players pan or scroll left and right to change machines.

The presentation should create the impression that the machines
are positioned around the player.

A fisheye-style perspective may be used while moving between
machines.

## Machine Screen

Selecting a vending machine opens its individual machine interface.

The machine contains:

- Item display area
- Roll button
- Drop box
- Collection progress
- Machine artwork/theme

## Item Display

The machine visually displays the items that can be collected.

Uncollected items appear as grey silhouettes.

Collected items display normally.

## Roll Interaction

Pressing the Roll button:

1. Checks that the player has a Roll Token.
2. Consumes one token.
3. Starts a coin-insertion animation.
4. Plays the vending-machine animation.
5. Determines the player's reward.
6. Sends the item into the machine's drop box.

## Drop Box

After the vending animation finishes, the player selects the
drop box to reveal the item they received.

The reveal should emphasize the item's rarity.

## Machine Idle Animation

Items displayed inside the machine should not remain completely
static.

Possible behavior:

- Items illuminate randomly.
- Illumination begins slowly.
- The sequence gradually becomes faster.
- It then slows again.
- The pattern repeats.

This gives the vending machine life while the player is viewing it.

## Scalability

Vending machines should be data-driven so additional machines can
be added without rebuilding the core game system.

Each machine should define its own:

- Name
- Theme
- Artwork
- Item collection
- Rarity configuration
- Animations
- Availability