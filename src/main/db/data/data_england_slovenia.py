# data_england_slovenia.py

def get_match_data():
    return {
        "match": {
            "match_name": "England vs Slovenia",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "0-0"
        },
        "teams": ["England", "Slovenia"],
        "key_stats": [
            {"team": "England", "possession_percent": 72, "total_attempts": 12, "attacks": 57, "corners_taken": 6, "passing_accuracy_percent": 92, "passes_completed": 694, "passes_attempted": 755, "balls_recovered": 36, "offsides": 2, "saves": 1, "distance_covered_km": 109.6, "yellow_cards": 3, "red_cards": 0},
            {"team": "Slovenia", "possession_percent": 28, "total_attempts": 4, "attacks": 19, "corners_taken": 0, "passing_accuracy_percent": 77, "passes_completed": 208, "passes_attempted": 271, "balls_recovered": 35, "offsides": 0, "saves": 3, "distance_covered_km": 112.5, "yellow_cards": 2, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "England", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 12, "attempts_on_target": 3, "attempts_off_target": 4, "blocks": 2, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 57, "clear_chances": 1, "corners_taken": 6, "offsides": 2, "dribbles": 13, "runs_into_attacking_third": 12, "runs_into_key_play_area": 15, "runs_into_penalty_area": 2},
            {"team": "Slovenia", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 4, "attempts_on_target": 1, "attempts_off_target": 2, "blocks": 5, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 19, "clear_chances": 0, "corners_taken": 0, "offsides": 0, "dribbles": 6, "runs_into_attacking_third": 5, "runs_into_key_play_area": 4, "runs_into_penalty_area": 3}
        ],
        "distribution_stats": [
            {"team": "England", "possession_percent": 72, "passing_accuracy_percent": 92, "passes_completed": 694, "passes_attempted": 755, "short_passes_completed": 140, "medium_passes_completed": 507, "long_passes_completed": 47, "backward_passes_completed": 137, "passes_completed_to_left": 196, "passes_completed_to_right": 199, "free_kicks_taken": 9, "passes_into_attacking_third": 56, "passes_into_key_play_area": 42, "passes_into_penalty_area": 20, "crossing_accuracy_percent": 44, "crosses_completed": 8, "crosses_attempted": 18, "times_in_possession": 146},
            {"team": "Slovenia", "possession_percent": 28, "passing_accuracy_percent": 77, "passes_completed": 208, "passes_attempted": 271, "short_passes_completed": 43, "medium_passes_completed": 142, "long_passes_completed": 47, "backward_passes_completed": 44, "passes_completed_to_left": 48, "passes_completed_to_right": 55, "free_kicks_taken": 13, "passes_into_attacking_third": 20, "passes_into_key_play_area": 15, "passes_into_penalty_area": 4, "crossing_accuracy_percent": 29, "crosses_completed": 2, "crosses_attempted": 7, "times_in_possession": 144}
        ],
        "defending_stats": [
            {"team": "England", "balls_recovered": 36, "blocks": 2, "penalties_conceded": 0, "tackles": 7, "tackles_won": 3, "tackles_lost": 4, "clearances_completed": 5, "clearances_attempted": 5},
            {"team": "Slovenia", "balls_recovered": 35, "blocks": 5, "penalties_conceded": 0, "tackles": 15, "tackles_won": 8, "tackles_lost": 7, "clearances_completed": 20, "clearances_attempted": 26}
        ],
        "goalkeeping_stats": [
            {"team": "England", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 1, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 4, "high_claims": 1, "low_claims": 3, "punches_made": 0},
            {"team": "Slovenia", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 3, "saves_from_direct_free_kicks": 1, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 0, "high_claims": 1, "low_claims": 3, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "England", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 11, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 3},
            {"team": "Slovenia", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 9, "fouls_committed_in_defensive_third": 4, "fouls_committed_in_own_half": 2}
        ]
    }
