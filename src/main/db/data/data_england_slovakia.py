# data_england_slovakia.py

def get_match_data():
    return {
        "match": {
            "match_name": "England vs Slovakia",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "2-1"
        },
        "teams": ["England", "Slovakia"],
        "key_stats": [
            {"team": "England", "possession_percent": 63, "total_attempts": 16, "attacks": 61, "corners_taken": 9, "passing_accuracy_percent": 88, "passes_completed": 711, "passes_attempted": 812, "balls_recovered": 39, "offsides": 1, "saves": 2, "distance_covered_km": 151.5, "yellow_cards": 3, "red_cards": 0},
            {"team": "Slovakia", "possession_percent": 37, "total_attempts": 13, "attacks": 38, "corners_taken": 1, "passing_accuracy_percent": 81, "passes_completed": 390, "passes_attempted": 484, "balls_recovered": 45, "offsides": 2, "saves": 0, "distance_covered_km": 156.7, "yellow_cards": 6, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "England", "goals": 2, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 16, "attempts_on_target": 2, "attempts_off_target": 7, "blocks": 3, "woodwork": 1, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 4, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 61, "clear_chances": 0, "corners_taken": 9, "offsides": 1, "dribbles": 24, "runs_into_attacking_third": 18, "runs_into_key_play_area": 19, "runs_into_penalty_area": 8},
            {"team": "Slovakia", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 13, "attempts_on_target": 3, "attempts_off_target": 7, "blocks": 7, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 3, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 38, "clear_chances": 0, "corners_taken": 1, "offsides": 2, "dribbles": 7, "runs_into_attacking_third": 15, "runs_into_key_play_area": 9, "runs_into_penalty_area": 1}
        ],
        "distribution_stats": [
            {"team": "England", "possession_percent": 63, "passing_accuracy_percent": 88, "passes_completed": 711, "passes_attempted": 812, "short_passes_completed": 122, "medium_passes_completed": 535, "long_passes_completed": 54, "backward_passes_completed": 107, "passes_completed_to_left": 220, "passes_completed_to_right": 234, "free_kicks_taken": 21, "passes_into_attacking_third": 42, "passes_into_key_play_area": 27, "passes_into_penalty_area": 17, "crossing_accuracy_percent": 12, "crosses_completed": 4, "crosses_attempted": 32, "times_in_possession": 236},
            {"team": "Slovakia", "possession_percent": 37, "passing_accuracy_percent": 81, "passes_completed": 390, "passes_attempted": 484, "short_passes_completed": 97, "medium_passes_completed": 253, "long_passes_completed": 40, "backward_passes_completed": 81, "passes_completed_to_left": 103, "passes_completed_to_right": 97, "free_kicks_taken": 12, "passes_into_attacking_third": 39, "passes_into_key_play_area": 29, "passes_into_penalty_area": 17, "crossing_accuracy_percent": 29, "crosses_completed": 4, "crosses_attempted": 14, "times_in_possession": 225}
        ],
        "defending_stats": [
            {"team": "England", "balls_recovered": 39, "blocks": 3, "penalties_conceded": 0, "tackles": 14, "tackles_won": 6, "tackles_lost": 8, "clearances_completed": 8, "clearances_attempted": 9},
            {"team": "Slovakia", "balls_recovered": 45, "blocks": 7, "penalties_conceded": 0, "tackles": 17, "tackles_won": 6, "tackles_lost": 11, "clearances_completed": 22, "clearances_attempted": 31}
        ],
        "goalkeeping_stats": [
            {"team": "England", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 1, "low_claims": 1, "punches_made": 0},
            {"team": "Slovakia", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 0, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 6, "high_claims": 3, "low_claims": 3, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "England", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 12, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 5},
            {"team": "Slovakia", "yellow_cards": 6, "red_cards": 0, "fouls_committed": 19, "fouls_committed_in_defensive_third": 6, "fouls_committed_in_own_half": 9}
        ]
    }
