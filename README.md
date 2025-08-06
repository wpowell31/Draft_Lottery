# Fantasy Football Draft Lottery System

## Overview

This draft lottery system provides a **completely fair and randomized** method for determining fantasy football draft order. Unlike traditional systems that favor teams with poor previous season records, this lottery gives **every team equal odds** for every draft position, ensuring maximum fairness and excitement. This draft lottery process is based on the NBA Draft Lottery Process, conducted by EY.

## How the Draft Lottery Works

### 1. Equal Odds System

Every team in your fantasy league receives **exactly the same number of lottery combinations**, meaning each team has an identical chance of receiving any draft pick position.

- **Total Combinations**: 1,000 combinations are distributed equally among all teams
- **Fair Distribution**: Each team receives `1000 ÷ number_of_teams` combinations
- **Remainder Handling**: Any leftover combinations are distributed evenly (one per team) to maintain perfect fairness

**Example for 10-team league:**
- Each team gets 100 combinations (10.0% chance for each pick)
- No team has better odds than any other team

### 2. Complete Lottery Selection

**All draft positions** are determined through the lottery process - there are no "consolation picks" based on previous season records.

#### The Selection Process:

1. **Random Pool Creation**: All team combinations are shuffled into a random pool
2. **Sequential Drawing**: Teams are drawn one by one for each draft position
3. **Elimination System**: Once a team is selected, they're removed from subsequent drawings
4. **Complete Randomization**: This continues until all draft positions are filled

### 3. Step-by-Step Lottery Process

#### Phase 1: Setup
- Teams are listed (order doesn't matter since all have equal odds)
- Lottery combinations are assigned equally to all teams
- Random seed is set for reproducible results (if desired)

#### Phase 2: The Drawing
For each draft pick (1st overall, 2nd overall, etc.):

1. **Create Drawing Pool**: Combine all remaining teams' lottery combinations
2. **Random Selection**: One combination is randomly selected from the pool
3. **Determine Winner**: The team owning that combination gets the current draft pick
4. **Remove from Pool**: That team is eliminated from future drawings
5. **Repeat**: Process continues for the next draft position

#### Phase 3: Final Results
- Complete draft order is displayed
- All positions are marked as "LOTTERY" picks
- No picks are based on previous season performance

## Key Features

### 🎲 **Complete Fairness**
- Every team has identical odds for every available draft position
- No advantages based on previous season performance
- True random selection process

### 🔄 **Dynamic Odds**
- As teams are selected, remaining teams maintain equal odds
- Example: In a 10-team league, each team starts with 10% chance for pick #1
- After pick #1, remaining 9 teams each have 11.11% chance for pick #2

### 📊 **Transparent Process**
- All lottery odds are displayed before the drawing
- Each pick selection is shown in real-time
- Final draft order clearly indicates all picks were lottery-determined

### 🎯 **Reproducible Results**
- Optional random seed setting allows for consistent results
- Useful for testing or re-running the same lottery scenario

## Usage Examples

### Basic 10-Team League
```python
run_fantasy_draft_lottery(num_teams=10, seed_value=42)
```

### Custom Team Names
```python
team_names = ["Team Alpha", "Team Beta", "Team Gamma", ...]
run_fantasy_draft_lottery(num_teams=10, team_names=team_names, seed_value=42)
```

### Different League Sizes
- **8-team league**: Each team gets 125 combinations (12.5% each)
- **12-team league**: Each team gets 83-84 combinations (~8.33% each)
- **14-team league**: Each team gets 71-72 combinations (~7.14% each)

## Sample Output

```
LOTTERY ODDS (based on previous season finish):
---------------------------------------------
 1. Team 1        - 100 combinations ( 10.0%)
 2. Team 2        - 100 combinations ( 10.0%)
 3. Team 3        - 100 combinations ( 10.0%)
 ... (all teams have identical odds)

DRAWING LOTTERY PICKS...
------------------------------
Pick # 1: Team 7
Pick # 2: Team 3
Pick # 3: Team 1
... (continues for all positions)

FINAL DRAFT ORDER
==================================================
Pick # 1: Team 7         (LOTTERY)
Pick # 2: Team 3         (LOTTERY)
Pick # 3: Team 1         (LOTTERY)
... (all picks marked as LOTTERY)

* All 10 picks determined by lottery with equal odds
```

## Why This System?

### Traditional Problems Solved
- **No "Tanking"**: Teams can't benefit from poor performance
- **Equal Opportunity**: Every team has the same chance at top picks
- **Maximum Excitement**: Any team could get the #1 pick
- **Fair Competition**: Skill in drafting matters more than draft position luck

### League Benefits
- **Increased Engagement**: All teams stay involved in lottery results
- **Balanced Competition**: No systematic advantages for any team
- **Simple to Understand**: Clear, transparent process
- **Customizable**: Works for any league size (4-20 teams)

## Technical Implementation

The lottery system uses Python's `random` module with the following key components:

- **Equal Distribution Algorithm**: Ensures fair combination allocation
- **Weighted Random Selection**: Uses combination counts for proper probability
- **Sequential Elimination**: Removes selected teams from subsequent draws
- **Seed Support**: Allows reproducible results for testing

## Running the Lottery

Execute the Python script to run your draft lottery:

```bash
python run_lottery.py
```

The script will display:
1. Team listings with equal lottery odds
2. Real-time drawing of each draft position
3. Final complete draft order
4. Confirmation that all picks were lottery-determined

---

*This system ensures every fantasy football season starts with maximum fairness and excitement for all league members!*
