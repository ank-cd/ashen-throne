# Ashen Throne

A small text-based RPG written in Python.

## Features
- turn-based combat
- random exploration events
- multiple player classes
- boss encounters

## Tech
- Python
- console-based prototype

## How to Run
From the project root, run:

```bash
py game/main.py
```

## Project Structure
- `game/` - core game logic and text modules
- `game/main.py` - game entry point
- `game/battle.py` - combat system
- `game/exploration.py` - exploration and random events
- `game/entity_sheet.py` - player and enemy data
- `game/attack_sets.py` - attack definitions
- `game/text_*.py` - game texts and descriptions
- `UI/` - future interface-related development

## Status
Current focus:
- stabilizing the core gameplay loop
- improving structure for future development

## Planned Improvements
- add more event variety
- expand boss encounters
- add a loot system
- improve console presentation
- connect future UI layer