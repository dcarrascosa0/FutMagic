# data_netherlands_england.py

def get_match_data():
    return {
        "match": {
            "match_name": "Netherlands vs England",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "1-2"
        },
        "teams": ["Netherlands", "England"],
        "key_stats": [
            {"team": "Netherlands", "possession_percent": 40, "total_attempts": 6, "attacks": 29, "corners_taken": 3, "passing_accuracy_percent": 90, "passes_completed": 384, "passes_attempted": 427, "balls_recovered": 24, "offsides": 1, "saves": 2, "distance_covered_km": 107.1, "yellow_cards": 3, "red_cards": 0},
            {"team": "England", "possession_percent": 60, "total_attempts": 9, "attacks": 45, "corners_taken": 0, "passing_accuracy_percent": 92, "passes_completed": 548, "passes_attempted": 598, "balls_recovered": 24, "offsides": 4, "saves": 2, "distance_covered_km": 107.3, "yellow_cards": 3, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Netherlands", "goals": 1, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 6, "attempts_on_target": 2, "attempts_off_target": 2, "blocks": 3, "woodwork": 1, "crossbar": 1, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 0, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 1, "attacks": 29, "clear_chances": 0, "corners_taken": 3, "offsides": 1, "dribbles": 8, "runs_into_attacking_third": 9, "runs_into_key_play_area": 18, "runs_into_penalty_area": 10},
            {"team": "England", "goals": 2, "goals_inside_area": 2, "goals_outside_area": 0, "total_attempts": 9, "attempts_on_target": 4, "attempts_off_target": 2, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 1, "assists": 1, "penalties_scored": 1, "penalties_missed": 0, "penalties_awarded": 1, "attacks": 45, "clear_chances": 0, "corners_taken": 0, "offsides": 4, "dribbles": 12, "runs_into_attacking_third": 9, "runs_into_key_play_area": 10, "runs_into_penalty_area": 2}
        ],
        "distribution_stats": [
            {"team": "Netherlands", "possession_percent": 40, "passing_accuracy_percent": 90, "passes_completed": 384, "passes_attempted": 427, "short_passes_completed": 108, "medium_passes_completed": 154, "long_passes_completed": 13, "backward_passes_completed": 39, "passes_completed_to_left": 59, "passes_completed_to_right": 59, "free_kicks_taken": 10, "passes_into_attacking_third": 27, "passes_into_key_play_area": 16, "passes_into_penalty_area": 12, "crossing_accuracy_percent": 42, "crosses_completed": 5, "crosses_attempted": 12, "times_in_possession": 122},
            {"team": "England", "possession_percent": 60, "passing_accuracy_percent": 92, "passes_completed": 548, "passes_attempted": 598, "short_passes_completed": 90, "medium_passes_completed": 173, "long_passes_completed": 10, "backward_passes_completed": 115, "passes_completed_to_left": 154, "passes_completed_to_right": 123, "free_kicks_taken": 11, "passes_into_attacking_third": 39, "passes_into_key_play_area": 16, "passes_into_penalty_area": 35, "crossing_accuracy_percent": 17, "crosses_completed": 5, "crosses_attempted": 12, "times_in_possession": 124}
        ],
        "defending_stats": [
            {"team": "Netherlands", "balls_recovered": 24, "blocks": 3, "penalties_conceded": 1, "tackles": 13, "tackles_won": 8, "tackles_lost": 5, "clearances_completed": 12, "clearances_attempted": 16},
            {"team": "England", "balls_recovered": 24, "blocks": 2, "penalties_conceded": 0, "tackles": 16, "tackles_won": 10, "tackles_lost": 6, "clearances_completed": 16, "clearances_attempted": 16}
        ],
        "goalkeeping_stats": [
            {"team": "Netherlands", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 5, "high_claims": 1, "low_claims": 4, "punches_made": 1},
            {"team": "England", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 4, "high_claims": 0, "low_claims": 4, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Netherlands", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 11, "fouls_committed_in_defensive_third": 4, "fouls_committed_in_own_half": 6},
            {"team": "England", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 11, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 6}
        ]
    }
