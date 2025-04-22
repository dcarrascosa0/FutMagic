# data_netherlands_austria.py

def get_match_data():
    return {
        "match": {
            "match_name": "Netherlands vs Austria",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "2-3"
        },
        "teams": ["Netherlands", "Austria"],
        "key_stats": [
            {"team": "Netherlands", "possession_percent": 52, "total_attempts": 11, "attacks": 43, "corners_taken": 5, "passing_accuracy_percent": 85, "passes_completed": 364, "passes_attempted": 429, "balls_recovered": 34, "offsides": 1, "saves": 3, "distance_covered_km": 108.1, "yellow_cards": 0, "red_cards": 0},
            {"team": "Austria", "possession_percent": 48, "total_attempts": 9, "attacks": 33, "corners_taken": 2, "passing_accuracy_percent": 81, "passes_completed": 322, "passes_attempted": 396, "balls_recovered": 44, "offsides": 1, "saves": 0, "distance_covered_km": 111.9, "yellow_cards": 3, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Netherlands", "goals": 2, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 11, "attempts_on_target": 2, "attempts_off_target": 6, "blocks": 3, "woodwork": 1, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 2, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 43, "clear_chances": 2, "corners_taken": 5, "offsides": 1, "dribbles": 18, "runs_into_attacking_third": 12, "runs_into_key_play_area": 12, "runs_into_penalty_area": 5},
            {"team": "Austria", "goals": 3, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 9, "attempts_on_target": 5, "attempts_off_target": 1, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 0, "assists": 3, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 33, "clear_chances": 1, "corners_taken": 2, "offsides": 1, "dribbles": 8, "runs_into_attacking_third": 12, "runs_into_key_play_area": 11, "runs_into_penalty_area": 5}
        ],
        "distribution_stats": [
            {"team": "Netherlands", "possession_percent": 52, "passing_accuracy_percent": 85, "passes_completed": 364, "passes_attempted": 429, "short_passes_completed": 85, "medium_passes_completed": 248, "long_passes_completed": 31, "backward_passes_completed": 67, "passes_completed_to_left": 98, "passes_completed_to_right": 91, "free_kicks_taken": 17, "passes_into_attacking_third": 37, "passes_into_key_play_area": 21, "passes_into_penalty_area": 14, "crossing_accuracy_percent": 22, "crosses_completed": 4, "crosses_attempted": 18, "times_in_possession": 191},
            {"team": "Austria", "possession_percent": 48, "passing_accuracy_percent": 81, "passes_completed": 322, "passes_attempted": 396, "short_passes_completed": 85, "medium_passes_completed": 191, "long_passes_completed": 46, "backward_passes_completed": 67, "passes_completed_to_left": 69, "passes_completed_to_right": 71, "free_kicks_taken": 11, "passes_into_attacking_third": 24, "passes_into_key_play_area": 17, "passes_into_penalty_area": 14, "crossing_accuracy_percent": 57, "crosses_completed": 4, "crosses_attempted": 7, "times_in_possession": 188}
        ],
        "defending_stats": [
            {"team": "Netherlands", "balls_recovered": 34, "blocks": 3, "penalties_conceded": 0, "tackles": 12, "tackles_won": 15, "tackles_lost": 8, "clearances_completed": 8, "clearances_attempted": 10},
            {"team": "Austria", "balls_recovered": 44, "blocks": 3, "penalties_conceded": 0, "tackles": 15, "tackles_won": 4, "tackles_lost": 3, "clearances_completed": 11, "clearances_attempted": 13}
        ],
        "goalkeeping_stats": [
            {"team": "Netherlands", "goals_conceded": 3, "own_goals_conceded": 1, "clean_sheets": 0, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 1, "low_claims": 0, "punches_made": 1},
            {"team": "Austria", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 0, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 0, "low_claims": 0, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Netherlands", "yellow_cards": 0, "red_cards": 0, "fouls_committed": 10, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 4},
            {"team": "Austria", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 16, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 8}
        ]
    }
