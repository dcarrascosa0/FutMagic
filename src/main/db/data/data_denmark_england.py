# data_denmark_england.py

def get_match_data():
    return {
        "match": {
            "match_name": "Denmark vs England",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "1-1"
        },
        "teams": ["Denmark", "England"],
        "key_stats": [
            {"team": "Denmark", "possession_percent": 46, "total_attempts": 16, "attacks": 41, "corners_taken": 4, "passing_accuracy_percent": 88, "passes_completed": 482, "passes_attempted": 546, "balls_recovered": 42, "offsides": 4, "saves": 3, "distance_covered_km": 110.4, "yellow_cards": 3, "red_cards": 0},
            {"team": "England", "possession_percent": 54, "total_attempts": 11, "attacks": 41, "corners_taken": 2, "passing_accuracy_percent": 87, "passes_completed": 470, "passes_attempted": 541, "balls_recovered": 38, "offsides": 0, "saves": 6, "distance_covered_km": 110.4, "yellow_cards": 1, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Denmark", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 16, "attempts_on_target": 7, "attempts_off_target": 4, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 1, "on_target_outside_area": 6, "off_target_outside_area": 2, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 41, "clear_chances": 0, "corners_taken": 4, "offsides": 0, "dribbles": 6, "runs_into_attacking_third": 19, "runs_into_key_play_area": 11, "runs_into_penalty_area": 5},
            {"team": "England", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 11, "attempts_on_target": 4, "attempts_off_target": 6, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 41, "clear_chances": 0, "corners_taken": 2, "offsides": 0, "dribbles": 7, "runs_into_attacking_third": 16, "runs_into_key_play_area": 10, "runs_into_penalty_area": 4}
        ],
        "distribution_stats": [
            {"team": "Denmark", "possession_percent": 46, "passing_accuracy_percent": 88, "passes_completed": 482, "passes_attempted": 546, "short_passes_completed": 172, "medium_passes_completed": 277, "long_passes_completed": 33, "backward_passes_completed": 99, "passes_completed_to_left": 128, "passes_completed_to_right": 144, "free_kicks_taken": 5, "passes_into_attacking_third": 38, "passes_into_key_play_area": 35, "passes_into_penalty_area": 25, "crossing_accuracy_percent": 40, "crosses_completed": 6, "crosses_attempted": 15, "times_in_possession": 155},
            {"team": "England", "possession_percent": 54, "passing_accuracy_percent": 87, "passes_completed": 470, "passes_attempted": 541, "short_passes_completed": 148, "medium_passes_completed": 283, "long_passes_completed": 33, "backward_passes_completed": 105, "passes_completed_to_left": 125, "passes_completed_to_right": 119, "free_kicks_taken": 17, "passes_into_attacking_third": 30, "passes_into_key_play_area": 35, "passes_into_penalty_area": 11, "crossing_accuracy_percent": 29, "crosses_completed": 2, "crosses_attempted": 7, "times_in_possession": 162}
        ],
        "defending_stats": [
            {"team": "Denmark", "balls_recovered": 42, "blocks": 1, "penalties_conceded": 0, "tackles": 21, "tackles_won": 13, "tackles_lost": 8, "clearances_completed": 11, "clearances_attempted": 13},
            {"team": "England", "balls_recovered": 38, "blocks": 1, "penalties_conceded": 0, "tackles": 13, "tackles_won": 6, "tackles_lost": 7, "clearances_completed": 7, "clearances_attempted": 14}
        ],
        "goalkeeping_stats": [
            {"team": "Denmark", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 2, "low_claims": 0, "punches_made": 1},
            {"team": "England", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 6, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 0, "low_claims": 2, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Denmark", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 13, "fouls_committed_in_defensive_third": 5, "fouls_committed_in_own_half": 4},
            {"team": "England", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 5, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 2}
        ]
    }
