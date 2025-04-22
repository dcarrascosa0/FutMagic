# data_spain_georgia.py

def get_match_data():
    return {
        "match": {
            "match_name": "Spain vs Georgia",
            "match_date": "2024-07-11",
            "venue": "Stadium Name",
            "score": "4-1"
        },
        "teams": ["Spain", "Georgia"],
        "key_stats": [
            {"team": "Spain", "possession_percent": 72, "total_attempts": 36, "attacks": 108, "corners_taken": 13, "passing_accuracy_percent": 94, "passes_completed": 772, "passes_attempted": 823, "balls_recovered": 42, "offsides": 3, "saves": 0, "distance_covered_km": 114.1, "yellow_cards": 1, "red_cards": 0},
            {"team": "Georgia", "possession_percent": 28, "total_attempts": 4, "attacks": 13, "corners_taken": 3, "passing_accuracy_percent": 81, "passes_completed": 229, "passes_attempted": 281, "balls_recovered": 35, "offsides": 0, "saves": 9, "distance_covered_km": 110.4, "yellow_cards": 1, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Spain", "goals": 4, "goals_inside_area": 4, "goals_outside_area": 0, "total_attempts": 36, "attempts_on_target": 13, "attempts_off_target": 12, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 3, "off_target_outside_area": 6, "assists": 4, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 108, "clear_chances": 0, "corners_taken": 13, "offsides": 3, "dribbles": 22, "runs_into_attacking_third": 42, "runs_into_key_play_area": 35, "runs_into_penalty_area": 13},
            {"team": "Georgia", "goals": 1, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 4, "attempts_on_target": 0, "attempts_off_target": 3, "blocks": 11, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 2, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 13, "clear_chances": 0, "corners_taken": 3, "offsides": 0, "dribbles": 14, "runs_into_attacking_third": 7, "runs_into_key_play_area": 6, "runs_into_penalty_area": 2}
        ],
        "distribution_stats": [
            {"team": "Spain", "possession_percent": 72, "passing_accuracy_percent": 94, "passes_completed": 772, "passes_attempted": 823, "short_passes_completed": 169, "medium_passes_completed": 560, "long_passes_completed": 43, "backward_passes_completed": 142, "passes_completed_to_left": 216, "passes_completed_to_right": 227, "free_kicks_taken": 5, "passes_into_attacking_third": 85, "passes_into_key_play_area": 77, "passes_into_penalty_area": 25, "crossing_accuracy_percent": 27, "crosses_completed": 7, "crosses_attempted": 26, "times_in_possession": 160},
            {"team": "Georgia", "possession_percent": 28, "passing_accuracy_percent": 81, "passes_completed": 229, "passes_attempted": 281, "short_passes_completed": 67, "medium_passes_completed": 142, "long_passes_completed": 20, "backward_passes_completed": 38, "passes_completed_to_left": 62, "passes_completed_to_right": 71, "free_kicks_taken": 14, "passes_into_attacking_third": 8, "passes_into_key_play_area": 1, "passes_into_penalty_area": 1, "crossing_accuracy_percent": 0, "crosses_completed": 0, "crosses_attempted": 5, "times_in_possession": 162}
        ],
        "defending_stats": [
            {"team": "Spain", "balls_recovered": 42, "blocks": 1, "penalties_conceded": 0, "tackles": 12, "tackles_won": 5, "tackles_lost": 7, "clearances_completed": 3, "clearances_attempted": 4},
            {"team": "Georgia", "balls_recovered": 35, "blocks": 11, "penalties_conceded": 0, "tackles": 15, "tackles_won": 7, "tackles_lost": 8, "clearances_completed": 18, "clearances_attempted": 27}
        ],
        "goalkeeping_stats": [
            {"team": "Spain", "goals_conceded": 1, "own_goals_conceded": 1, "clean_sheets": 0, "saves": 0, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 2, "low_claims": 1, "punches_made": 0},
            {"team": "Georgia", "goals_conceded": 4, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 9, "saves_from_direct_free_kicks": 1, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 0, "low_claims": 0, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Spain", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 11, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 1},
            {"team": "Georgia", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 5, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 3}
        ]
    }
