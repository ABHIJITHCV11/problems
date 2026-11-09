# 138. Copy List with Random Pointer

sol1 : my own
sol2 : neetcode

## Core idea

When you deep-copy a structure, the copy's pointers must point to the **new** nodes, not the old ones.
Use a hashmap **old node → new copy**. Same pattern as Clone Graph (Graphs section).

## Why two passes

- `random` can point to a node further ahead that hasn't been copied yet, so you can't set `copy.random` in a single pass.
- Pass 1: create every copy and fill the map.
- Pass 2: set `next` / `random` by looking up `map[old.next]` and `map[old.random]`.
- `random = None` in the original must be `None` in the copy.

## sol1 (mine)

- Pass 1 builds the copied `next` chain and `d1[old] = new`.
- Pass 2 sets `x.random = d1[curr_real.random]`, with an explicit `None` check.
- First attempt had a bug that I found myself: the fix was **the dict key** (key the map on the old node itself).

## sol2 (NeetCode)

- `oldToCopy = {None: None}`. Seeding `None` removes all the `None` checks, because `oldToCopy[cur.next]` and `oldToCopy[cur.random]` just work.
- Pass 2 sets both `next` and `random` from the map.

O(n) time, O(n) extra space for the map.

## Revision

Parked for revision: rewrite from memory.
