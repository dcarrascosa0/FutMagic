# data_spain_france.py

def get_match_data():
    return {
        "match": {
            "match_name": "Spain vs France",
            "match_date": "2024-07-13",
            "venue": "Stadium Name",
            "score": "2-1"
        },
        "teams": ["Spain", "France"],
        "key_stats": [
            {"team": "Spain", "possession_percent": 58, "total_attempts": 6, "attacks": 39, "corners_taken": 4, "passing_accuracy_percent": 89, "passes_completed": 456, "passes_attempted": 513, "balls_recovered": 25, "offsides": 0, "saves": 2, "distance_covered_km": 110.3, "yellow_cards": 2, "red_cards": 0},
            {"team": "France", "possession_percent": 42, "total_attempts": 9, "attacks": 46, "corners_taken": 6, "passing_accuracy_percent": 85, "passes_completed": 303, "passes_attempted": 358, "balls_recovered": 31, "offsides": 0, "saves": 0, "distance_covered_km": 107.3, "yellow_cards": 2, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Spain", "goals": 2, "goals_inside_area": 1, "goals_outside_area": 1, "total_attempts": 6, "attempts_on_target": 2, "attempts_off_target": 2, "blocks": 2, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 1, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 39, "clear_chances": 0, "corners_taken": 4, "offsides": 0, "dribbles": 20, "runs_into_attacking_third": 10, "runs_into_key_play_area": 12, "runs_into_penalty_area": 3},
            {"team": "France", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 9, "attempts_on_target": 3, "attempts_off_target": 4, "blocks": 2, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 0, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 46, "clear_chances": 0, "corners_taken": 6, "offsides": 0, "dribbles": 26, "runs_into_attacking_third": 20, "runs_into_key_play_area": 12, "runs_into_penalty_area": 10}
        ],
        "distribution_stats": [
            {"team": "Spain", "possession_percent": 58, "passing_accuracy_percent": 89, "passes_completed": 456, "passes_attempted": 513, "short_passes_completed": 113, "medium_passes_completed": 313, "long_passes_completed": 33, "backward_passes_completed": 109, "passes_completed_to_left": 100, "passes_completed_to_right": 114, "free_kicks_taken": 13, "passes_into_attacking_third": 40, "passes_into_key_play_area": 27, "passes_into_penalty_area": 3, "crossing_accuracy_percent": 13, "crosses_completed": 2, "crosses_attempted": 15, "times_in_possession": 166},
            {"team": "France", "possession_percent": 42, "passing_accuracy_percent": 85, "passes_completed": 303, "passes_attempted": 358, "short_passes_completed": 68, "medium_passes_completed": 202, "long_passes_completed": 34, "backward_passes_completed": 51, "passes_completed_to_left": 83, "passes_completed_to_right": 82, "free_kicks_taken": 9, "passes_into_attacking_third": 30, "passes_into_key_play_area": 17, "passes_into_penalty_area": 13, "crossing_accuracy_percent": 29, "crosses_completed": 8, "crosses_attempted": 28, "times_in_possession": 164}
        ],
        "defending_stats": [
            {"team": "Spain", "balls_recovered": 25, "blocks": 2, "penalties_conceded": 0, "tackles": 10, "tackles_won": 1, "tackles_lost": 9, "clearances_completed": 22, "clearances_attempted": 26},
            {"team": "France", "balls_recovered": 31, "blocks": 2, "penalties_conceded": 0, "tackles": 17, "tackles_won": 5, "tackles_lost": 12, "clearances_completed": 8, "clearances_attempted": 12}
        ],
        "goalkeeping_stats": [
            {"team": "Spain", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 1, "low_claims": 1, "punches_made": 1},
            {"team": "France", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 0, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 5, "high_claims": 3, "low_claims": 2, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Spain", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 9, "fouls_committed_in_defensive_third": 5, "fouls_committed_in_own_half": 7},
            {"team": "France", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 14, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 3}
        ]
    }
