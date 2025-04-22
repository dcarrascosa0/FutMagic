# data_spain_germany.py

def get_match_data():
    return {
        "match": {
            "match_name": "Spain vs Germany",
            "match_date": "2024-07-12",
            "venue": "Stadium Name",
            "score": "2-1"
        },
        "teams": ["Spain", "Germany"],
        "key_stats": [
            {"team": "Spain", "possession_percent": 52, "total_attempts": 18, "attacks": 56, "corners_taken": 1, "passing_accuracy_percent": 87, "passes_completed": 504, "passes_attempted": 580, "balls_recovered": 65, "offsides": 3, "saves": 4, "distance_covered_km": 145.9, "yellow_cards": 7, "red_cards": 1},
            {"team": "Germany", "possession_percent": 48, "total_attempts": 23, "attacks": 56, "corners_taken": 5, "passing_accuracy_percent": 87, "passes_completed": 534, "passes_attempted": 617, "balls_recovered": 50, "offsides": 2, "saves": 4, "distance_covered_km": 151.3, "yellow_cards": 8, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Spain", "goals": 2, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 18, "attempts_on_target": 6, "attempts_off_target": 9, "blocks": 8, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 4, "off_target_outside_area": 6, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 56, "clear_chances": 1, "corners_taken": 1, "offsides": 3, "dribbles": 23, "runs_into_attacking_third": 35, "runs_into_key_play_area": 28, "runs_into_penalty_area": 10},
            {"team": "Germany", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 23, "attempts_on_target": 5, "attempts_off_target": 10, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 3, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 56, "clear_chances": 0, "corners_taken": 5, "offsides": 2, "dribbles": 10, "runs_into_attacking_third": 20, "runs_into_key_play_area": 11, "runs_into_penalty_area": 7}
        ],
        "distribution_stats": [
            {"team": "Spain", "possession_percent": 52, "passing_accuracy_percent": 87, "passes_completed": 504, "passes_attempted": 580, "short_passes_completed": 135, "medium_passes_completed": 323, "long_passes_completed": 46, "backward_passes_completed": 110, "passes_completed_to_left": 127, "passes_completed_to_right": 115, "free_kicks_taken": 24, "passes_into_attacking_third": 50, "passes_into_key_play_area": 35, "passes_into_penalty_area": 10, "crossing_accuracy_percent": 42, "crosses_completed": 5, "crosses_attempted": 12, "times_in_possession": 214},
            {"team": "Germany", "possession_percent": 48, "passing_accuracy_percent": 87, "passes_completed": 534, "passes_attempted": 617, "short_passes_completed": 176, "medium_passes_completed": 317, "long_passes_completed": 41, "backward_passes_completed": 101, "passes_completed_to_left": 144, "passes_completed_to_right": 126, "free_kicks_taken": 20, "passes_into_attacking_third": 52, "passes_into_key_play_area": 37, "passes_into_penalty_area": 29, "crossing_accuracy_percent": 39, "crosses_completed": 13, "crosses_attempted": 33, "times_in_possession": 214}
        ],
        "defending_stats": [
            {"team": "Spain", "balls_recovered": 65, "blocks": 8, "penalties_conceded": 0, "tackles": 13, "tackles_won": 5, "tackles_lost": 8, "clearances_completed": 22, "clearances_attempted": 33},
            {"team": "Germany", "balls_recovered": 50, "blocks": 3, "penalties_conceded": 0, "tackles": 23, "tackles_won": 6, "tackles_lost": 17, "clearances_completed": 13, "clearances_attempted": 16}
        ],
        "goalkeeping_stats": [
            {"team": "Spain", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 4, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 10, "high_claims": 5, "low_claims": 5, "punches_made": 0},
            {"team": "Germany", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 4, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 0, "low_claims": 2, "punches_made": 1}
        ],
        "disciplinary_stats": [
            {"team": "Spain", "yellow_cards": 7, "red_cards": 1, "fouls_committed": 17, "fouls_committed_in_defensive_third": 3, "fouls_committed_in_own_half": 6},
            {"team": "Germany", "yellow_cards": 8, "red_cards": 0, "fouls_committed": 22, "fouls_committed_in_defensive_third": 4, "fouls_committed_in_own_half": 10}
        ]
    }
