# Lab rat

Simulate a rat moving around on a table.

## Requirements

Python version 3.6 or higher is required.

## Usage

Set table size and starting position for the rat with 4 integers, followed by any number of integers as commands:

```
[table-width,table-height,rat-position-x,rat-position-y,commands...] | python main.py
```

The rat is facing upwards initially, and the output will be the final rat position as 2 integers:

```
[rat-position-x,rat-position-y]
```

If the rat falled off the table, then the final position will be:

```
[-1,-1]
```

> Integers are assumed to be 32-bit.

### Commands

0. Quit simulation and print results to stdout.
1. Move rat forward one step.
2. Move rat backwards one step.
3. Rotate rat right (clockwise) 90 degrees.
4. Rotate rat left (counterclockwise) 90 degrees.
