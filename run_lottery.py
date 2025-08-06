import random

def set_seed(seed_value=31):
    """Set the random seed for reproducible results"""
    random.seed(seed_value)
    print(f"Random seed set to: {seed_value}")

def assign_lottery_odds(num_teams):
    """
    Assign equal lottery odds to all teams.
    Every team has the same chance at higher picks.
    """
    # Create a system where all teams get equal odds
    base_combinations = 1000  # Total combinations available
    
    # Calculate equal combinations for each team
    combinations_per_team = base_combinations // num_teams
    team_combinations = [combinations_per_team] * num_teams
    
    # Distribute any remaining combinations evenly
    remaining = base_combinations % num_teams
    for i in range(remaining):
        team_combinations[i] += 1
    
    return team_combinations

def simulate_lottery_drawing(teams, team_combinations):
    """
    Simulate the lottery drawing process.
    Returns the order of teams for draft picks.
    """
    print("\n" + "="*50)
    print("FANTASY FOOTBALL DRAFT LOTTERY SIMULATION")
    print("="*50)
    
    # Display lottery odds
    print("\nLOTTERY ODDS (based on previous season finish):")
    print("-" * 45)
    total_combinations = sum(team_combinations)
    
    for i, (team, combinations) in enumerate(zip(teams, team_combinations)):
        percentage = (combinations / total_combinations) * 100
        print(f"{i+1:2}. {team:15} - {combinations:3} combinations ({percentage:5.1f}%)")
    
    # Create the lottery pool
    lottery_pool = []
    for i, combinations in enumerate(team_combinations):
        lottery_pool.extend([i] * combinations)
    
    # Shuffle the pool
    random.shuffle(lottery_pool)
    
    # Simulate the lottery drawing
    draft_order = []
    remaining_teams = list(range(len(teams)))
    
    print(f"\nDRAWING LOTTERY PICKS...")
    print("-" * 30)
    
    # All picks are now determined by lottery (not just top picks)
    lottery_picks = len(teams)
    
    for pick in range(lottery_picks):
        # Draw from remaining teams
        available_combinations = []
        for team_idx in remaining_teams:
            available_combinations.extend([team_idx] * team_combinations[team_idx])
        
        if not available_combinations:
            break
            
        # Draw the winning team
        winning_team_idx = random.choice(available_combinations)
        draft_order.append(winning_team_idx)
        remaining_teams.remove(winning_team_idx)
        
        print(f"Pick #{pick + 1:2}: {teams[winning_team_idx]}")
    
    return draft_order, lottery_picks

def display_final_draft_order(teams, draft_order, lottery_picks):
    """Display the final draft order results"""
    print(f"\n" + "="*50)
    print("FINAL DRAFT ORDER")
    print("="*50)
    
    for i, team_idx in enumerate(draft_order):
        print(f"Pick #{i+1:2}: {teams[team_idx]:15} (LOTTERY)")
    
    print(f"\n* All {lottery_picks} picks determined by lottery with equal odds")

def run_fantasy_draft_lottery(num_teams=10, team_names=None, seed_value=42):
    """
    Main function to run the fantasy football draft lottery
    
    Args:
        num_teams: Number of teams in the league (8-12 typical)
        team_names: List of team names (optional)
        seed_value: Random seed for reproducible results
    """
    # Validate input
    if num_teams < 4 or num_teams > 20:
        print("Warning: Number of teams should typically be between 4-20")
    
    # Set the random seed
    set_seed(seed_value)
    
    # Create team names if not provided
    if team_names is None:
        team_names = [f"Team {i+1}" for i in range(num_teams)]
    elif len(team_names) != num_teams:
        print(f"Warning: {len(team_names)} team names provided but {num_teams} teams specified")
        team_names = team_names[:num_teams] + [f"Team {i+1}" for i in range(len(team_names), num_teams)]
    
    # Teams are ordered from worst record to best record (last season)
    print(f"\nTeams ordered by PREVIOUS SEASON record (worst to best):")
    for i, team in enumerate(team_names):
        print(f"{i+1:2}. {team}")
    
    # Assign lottery odds
    team_combinations = assign_lottery_odds(num_teams)
    
    # Run the lottery simulation
    draft_order, lottery_picks = simulate_lottery_drawing(team_names, team_combinations)
    
    # Display final results
    display_final_draft_order(team_names, draft_order, lottery_picks)
    
    return draft_order

# Example usage and testing
if __name__ == "__main__":
    # Example 1: 10-team league with default team names
    print("EXAMPLE 1: 10-team league")
    run_fantasy_draft_lottery(num_teams=10, seed_value=42)
    
    print("\n" + "="*70 + "\n")
    
    # Example 2: 12-team league with custom team names
    custom_teams = [
        "The Strugglers", "Barely Trying", "Last Place Joe", "Almost Good",
        "Middle of Pack", "Decent Squad", "Pretty Good", "Strong Team",
        "Championship Contenders", "Defending Champs", "Super Team", "Dynasty"
    ]
    
    print("EXAMPLE 2: 12-team league with custom names")
    run_fantasy_draft_lottery(num_teams=12, team_names=custom_teams, seed_value=123)
    
    print("\n" + "="*70 + "\n")
    
    # Example 3: 8-team league
    print("EXAMPLE 3: 8-team league")
    run_fantasy_draft_lottery(num_teams=8, seed_value=458)