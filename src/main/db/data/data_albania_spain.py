# data_albania_spain.py

def get_match_data():
    return {
        "match": {
            "match_name": "Albania vs Spain",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "0-1"
        },
        "teams": ["Albania", "Spain"],
        "key_stats": [
            {"team": "Albania", "possession_percent": 41, "total_attempts": 10, "attacks": 31, "corners_taken": 2, "passing_accuracy_percent": 85, "passes_completed": 341, "passes_attempted": 403, "balls_recovered": 48, "offsides": 1, "saves": 2, "distance_covered_km": 117.2, "yellow_cards": 2, "red_cards": 0},
            {"team": "Spain", "possession_percent": 59, "total_attempts": 17, "attacks": 59, "corners_taken": 6, "passing_accuracy_percent": 92, "passes_completed": 530, "passes_attempted": 579, "balls_recovered": 42, "offsides": 2, "saves": 4, "distance_covered_km": 118.1, "yellow_cards": 1, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Albania", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 10, "attempts_on_target": 4, "attempts_off_target": 3, "blocks": 4, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 1, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 31, "clear_chances": 0, "corners_taken": 2, "offsides": 1, "dribbles": 21, "runs_into_attacking_third": 15, "runs_into_key_play_area": 18, "runs_into_penalty_area": 4},
            {"team": "Spain", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 17, "attempts_on_target": 3, "attempts_off_target": 10, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 2, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 59, "clear_chances": 0, "corners_taken": 6, "offsides": 2, "dribbles": 22, "runs_into_attacking_third": 23, "runs_into_key_play_area": 16, "runs_into_penalty_area": 6}
        ],
        "distribution_stats": [
            {"team": "Albania", "possession_percent": 41, "passing_accuracy_percent": 85, "passes_completed": 341, "passes_attempted": 403, "short_passes_completed": 62, "medium_passes_completed": 246, "long_passes_completed": 33, "backward_passes_completed": 67, "passes_completed_to_left": 87, "passes_completed_to_right": 85, "free_kicks_taken": 17, "passes_into_attacking_third": 23, "passes_into_key_play_area": 12, "passes_into_penalty_area": 7, "crossing_accuracy_percent": 18, "crosses_completed": 2, "crosses_attempted": 11, "times_in_possession": 178},
            {"team": "Spain", "possession_percent": 59, "passing_accuracy_percent": 92, "passes_completed": 530, "passes_attempted": 579, "short_passes_completed": 96, "medium_passes_completed": 394, "long_passes_completed": 40, "backward_passes_completed": 96, "passes_completed_to_left": 142, "passes_completed_to_right": 166, "free_kicks_taken": 7, "passes_into_attacking_third": 42, "passes_into_key_play_area": 19, "passes_into_penalty_area": 16, "crossing_accuracy_percent": 38, "crosses_completed": 9, "crosses_attempted": 24, "times_in_possession": 167}
        ],
        "defending_stats": [
            {"team": "Albania", "balls_recovered": 48, "blocks": 4, "penalties_conceded": 0, "tackles": 13, "tackles_won": 10, "tackles_lost": 3, "clearances_completed": 15, "clearances_attempted": 20},
            {"team": "Spain", "balls_recovered": 42, "blocks": 3, "penalties_conceded": 0, "tackles": 20, "tackles_won": 12, "tackles_lost": 8, "clearances_completed": 20, "clearances_attempted": 22}
        ],
        "goalkeeping_stats": [
            {"team": "Albania", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 2, "low_claims": 1, "punches_made": 2},
            {"team": "Spain", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 4, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 6, "high_claims": 2, "low_claims": 4, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Albania", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 6, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 3},
            {"team": "Spain", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 15, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 4}
        ]
    }
