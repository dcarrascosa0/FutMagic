# data_netherlands_france.py

def get_match_data():
    return {
        "match": {
            "match_name": "Netherlands vs France",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "0-0"
        },
        "teams": ["Netherlands", "France"],
        "key_stats": [
            {"team": "Netherlands", "possession_percent": 42, "total_attempts": 8, "attacks": 26, "corners_taken": 3, "passing_accuracy_percent": 89, "passes_completed": 354, "passes_attempted": 397, "balls_recovered": 28, "offsides": 4, "saves": 3, "distance_covered_km": 107.6, "yellow_cards": 1, "red_cards": 0},
            {"team": "France", "possession_percent": 58, "total_attempts": 16, "attacks": 58, "corners_taken": 6, "passing_accuracy_percent": 92, "passes_completed": 613, "passes_attempted": 664, "balls_recovered": 30, "offsides": 0, "saves": 4, "distance_covered_km": 106, "yellow_cards": 0, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Netherlands", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 8, "attempts_on_target": 4, "attempts_off_target": 0, "blocks": 5, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 0, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 26, "clear_chances": 0, "corners_taken": 3, "offsides": 4, "dribbles": 6, "runs_into_attacking_third": 5, "runs_into_key_play_area": 4, "runs_into_penalty_area": 5},
            {"team": "France", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 16, "attempts_on_target": 3, "attempts_off_target": 8, "blocks": 4, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 58, "clear_chances": 2, "corners_taken": 6, "offsides": 0, "dribbles": 14, "runs_into_attacking_third": 12, "runs_into_key_play_area": 8, "runs_into_penalty_area": 4}
        ],
        "distribution_stats": [
            {"team": "Netherlands", "possession_percent": 42, "passing_accuracy_percent": 89, "passes_completed": 354, "passes_attempted": 397, "short_passes_completed": 82, "medium_passes_completed": 238, "long_passes_completed": 34, "backward_passes_completed": 67, "passes_completed_to_left": 85, "passes_completed_to_right": 103, "free_kicks_taken": 8, "passes_into_attacking_third": 27, "passes_into_key_play_area": 16, "passes_into_penalty_area": 7, "crossing_accuracy_percent": 19, "crosses_completed": 3, "crosses_attempted": 8, "times_in_possession": 135},
            {"team": "France", "possession_percent": 58, "passing_accuracy_percent": 92, "passes_completed": 613, "passes_attempted": 664, "short_passes_completed": 140, "medium_passes_completed": 427, "long_passes_completed": 46, "backward_passes_completed": 122, "passes_completed_to_left": 154, "passes_completed_to_right": 175, "free_kicks_taken": 8, "passes_into_attacking_third": 63, "passes_into_key_play_area": 40, "passes_into_penalty_area": 7, "crossing_accuracy_percent": 38, "crosses_completed": 3, "crosses_attempted": 8, "times_in_possession": 163}
        ],
        "defending_stats": [
            {"team": "Netherlands", "balls_recovered": 28, "blocks": 5, "penalties_conceded": 0, "tackles": 16, "tackles_won": 9, "tackles_lost": 7, "clearances_completed": 20, "clearances_attempted": 23},
            {"team": "France", "balls_recovered": 30, "blocks": 4, "penalties_conceded": 0, "tackles": 13, "tackles_won": 5, "tackles_lost": 6, "clearances_completed": 11, "clearances_attempted": 12}
        ],
        "goalkeeping_stats": [
            {"team": "Netherlands", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 2, "low_claims": 1, "punches_made": 0},
            {"team": "France", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 4, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 2, "low_claims": 1, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Netherlands", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 13, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 4},
            {"team": "France", "yellow_cards": 0, "red_cards": 0, "fouls_committed": 8, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 3}
        ]
    }
