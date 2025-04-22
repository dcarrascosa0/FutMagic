# data_poland_netherlands.py

def get_match_data():
    return {
        "match": {
            "match_name": "Poland vs Netherlands",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "1-2"
        },
        "teams": ["Poland", "Netherlands"],
        "key_stats": [
            {"team": "Poland", "possession_percent": 35, "total_attempts": 11, "attacks": 29, "corners_taken": 3, "passing_accuracy_percent": 80, "passes_completed": 227, "passes_attempted": 283, "balls_recovered": 36, "offsides": 2, "saves": 2, "distance_covered_km": 114.9, "yellow_cards": 0, "red_cards": 0},
            {"team": "Netherlands", "possession_percent": 65, "total_attempts": 20, "attacks": 65, "corners_taken": 6, "passing_accuracy_percent": 90, "passes_completed": 523, "passes_attempted": 580, "balls_recovered": 32, "offsides": 0, "saves": 6, "distance_covered_km": 108.7, "yellow_cards": 1, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Poland", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 11, "attempts_on_target": 7, "attempts_off_target": 3, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 3, "off_target_outside_area": 1, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 29, "clear_chances": 0, "corners_taken": 3, "offsides": 2, "dribbles": 16, "runs_into_attacking_third": 10, "runs_into_key_play_area": 8, "runs_into_penalty_area": 4},
            {"team": "Netherlands", "goals": 2, "goals_inside_area": 1, "goals_outside_area": 1, "total_attempts": 20, "attempts_on_target": 4, "attempts_off_target": 13, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 4, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 65, "clear_chances": 0, "corners_taken": 6, "offsides": 0, "dribbles": 17, "runs_into_attacking_third": 21, "runs_into_key_play_area": 24, "runs_into_penalty_area": 11}
        ],
        "distribution_stats": [
            {"team": "Poland", "possession_percent": 35, "passing_accuracy_percent": 80, "passes_completed": 227, "passes_attempted": 283, "short_passes_completed": 92, "medium_passes_completed": 116, "long_passes_completed": 19, "backward_passes_completed": 50, "passes_completed_to_left": 48, "passes_completed_to_right": 59, "free_kicks_taken": 8, "passes_into_attacking_third": 18, "passes_into_key_play_area": 11, "passes_into_penalty_area": 8, "crossing_accuracy_percent": 25, "crosses_completed": 4, "crosses_attempted": 16, "times_in_possession": 163},
            {"team": "Netherlands", "possession_percent": 65, "passing_accuracy_percent": 90, "passes_completed": 523, "passes_attempted": 580, "short_passes_completed": 133, "medium_passes_completed": 348, "long_passes_completed": 42, "backward_passes_completed": 100, "passes_completed_to_left": 137, "passes_completed_to_right": 140, "free_kicks_taken": 12, "passes_into_attacking_third": 49, "passes_into_key_play_area": 36, "passes_into_penalty_area": 25, "crossing_accuracy_percent": 35, "crosses_completed": 4, "crosses_attempted": 20, "times_in_possession": 165}
        ],
        "defending_stats": [
            {"team": "Poland", "balls_recovered": 36, "blocks": 3, "penalties_conceded": 0, "tackles": 13, "tackles_won": 7, "tackles_lost": 6, "clearances_completed": 24, "clearances_attempted": 27},
            {"team": "Netherlands", "balls_recovered": 32, "blocks": 1, "penalties_conceded": 0, "tackles": 14, "tackles_won": 7, "tackles_lost": 7, "clearances_completed": 16, "clearances_attempted": 20}
        ],
        "goalkeeping_stats": [
            {"team": "Poland", "goals_conceded": 2, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 0, "low_claims": 2, "punches_made": 0},
            {"team": "Netherlands", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 6, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 4, "high_claims": 3, "low_claims": 1, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Poland", "yellow_cards": 0, "red_cards": 0, "fouls_committed": 10, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 6},
            {"team": "Netherlands", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 8, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 3}
        ]
    }
