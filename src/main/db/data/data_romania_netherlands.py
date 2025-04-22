# data_romania_netherlands.py

def get_match_data():
    return {
        "match": {
            "match_name": "Romania vs Netherlands",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "0-3"
        },
        "teams": ["Romania", "Netherlands"],
        "key_stats": [
            {"team": "Romania", "possession_percent": 39, "total_attempts": 5, "attacks": 35, "corners_taken": 4, "passing_accuracy_percent": 76, "passes_completed": 213, "passes_attempted": 282, "balls_recovered": 19, "offsides": 0, "saves": 3, "distance_covered_km": 112.5, "yellow_cards": 2, "red_cards": 0},
            {"team": "Netherlands", "possession_percent": 61, "total_attempts": 24, "attacks": 66, "corners_taken": 13, "passing_accuracy_percent": 89, "passes_completed": 449, "passes_attempted": 505, "balls_recovered": 29, "offsides": 4, "saves": 1, "distance_covered_km": 109.4, "yellow_cards": 2, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Romania", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 5, "attempts_on_target": 1, "attempts_off_target": 3, "blocks": 6, "woodwork": 0, "crossbar": 1, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 35, "clear_chances": 0, "corners_taken": 4, "offsides": 0, "dribbles": 6, "runs_into_attacking_third": 9, "runs_into_key_play_area": 11, "runs_into_penalty_area": 5},
            {"team": "Netherlands", "goals": 3, "goals_inside_area": 3, "goals_outside_area": 0, "total_attempts": 24, "attempts_on_target": 6, "attempts_off_target": 12, "blocks": 1, "woodwork": 1, "crossbar": 0, "post": 1, "on_target_outside_area": 2, "off_target_outside_area": 3, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 66, "clear_chances": 2, "corners_taken": 13, "offsides": 4, "dribbles": 17, "runs_into_attacking_third": 20, "runs_into_key_play_area": 17, "runs_into_penalty_area": 14}
        ],
        "distribution_stats": [
            {"team": "Romania", "possession_percent": 39, "passing_accuracy_percent": 76, "passes_completed": 213, "passes_attempted": 282, "short_passes_completed": 50, "medium_passes_completed": 136, "long_passes_completed": 27, "backward_passes_completed": 40, "passes_completed_to_left": 52, "passes_completed_to_right": 46, "free_kicks_taken": 13, "passes_into_attacking_third": 19, "passes_into_key_play_area": 11, "passes_into_penalty_area": 3, "crossing_accuracy_percent": 15, "crosses_completed": 2, "crosses_attempted": 13, "times_in_possession": 176},
            {"team": "Netherlands", "possession_percent": 61, "passing_accuracy_percent": 89, "passes_completed": 449, "passes_attempted": 505, "short_passes_completed": 115, "medium_passes_completed": 297, "long_passes_completed": 27, "backward_passes_completed": 40, "passes_completed_to_left": 109, "passes_completed_to_right": 107, "free_kicks_taken": 8, "passes_into_attacking_third": 39, "passes_into_key_play_area": 23, "passes_into_penalty_area": 20, "crossing_accuracy_percent": 23, "crosses_completed": 2, "crosses_attempted": 7, "times_in_possession": 174}
        ],
        "defending_stats": [
            {"team": "Romania", "balls_recovered": 19, "blocks": 6, "penalties_conceded": 0, "tackles": 13, "tackles_won": 7, "tackles_lost": 8, "clearances_completed": 18, "clearances_attempted": 31},
            {"team": "Netherlands", "balls_recovered": 29, "blocks": 1, "penalties_conceded": 0, "tackles": 7, "tackles_won": 5, "tackles_lost": 3, "clearances_completed": 16, "clearances_attempted": 22}
        ],
        "goalkeeping_stats": [
            {"team": "Romania", "goals_conceded": 3, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 2, "low_claims": 1, "punches_made": 1},
            {"team": "Netherlands", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 1, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 1, "low_claims": 1, "punches_made": 1}
        ],
        "disciplinary_stats": [
            {"team": "Romania", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 8, "fouls_committed_in_defensive_third": 3, "fouls_committed_in_own_half": 5},
            {"team": "Netherlands", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 9, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 4}
        ]
    }
