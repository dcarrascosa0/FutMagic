# data_serbia_england.py

def get_match_data():
    return {
        "match": {
            "match_name": "Serbia vs England",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "0-1"
        },
        "teams": ["Serbia", "England"],
        "key_stats": [
            {"team": "Serbia", "possession_percent": 47, "total_attempts": 6, "attacks": 33, "corners_taken": 2, "passing_accuracy_percent": 89, "passes_completed": 454, "passes_attempted": 512, "balls_recovered": 29, "offsides": 0, "saves": 2, "distance_covered_km": 113.4, "yellow_cards": 3, "red_cards": 0},
            {"team": "England", "possession_percent": 53, "total_attempts": 5, "attacks": 34, "corners_taken": 1, "passing_accuracy_percent": 91, "passes_completed": 544, "passes_attempted": 600, "balls_recovered": 44, "offsides": 1, "saves": 1, "distance_covered_km": 116.2, "yellow_cards": 0, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Serbia", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 6, "attempts_on_target": 1, "attempts_off_target": 2, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 1, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 33, "clear_chances": 0, "corners_taken": 2, "offsides": 0, "dribbles": 5, "runs_into_attacking_third": 18, "runs_into_key_play_area": 13, "runs_into_penalty_area": 5},
            {"team": "England", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 5, "attempts_on_target": 3, "attempts_off_target": 1, "blocks": 1, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 0, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 34, "clear_chances": 0, "corners_taken": 1, "offsides": 1, "dribbles": 7, "runs_into_attacking_third": 15, "runs_into_key_play_area": 10, "runs_into_penalty_area": 3}
        ],
        "distribution_stats": [
            {"team": "Serbia", "possession_percent": 47, "passing_accuracy_percent": 89, "passes_completed": 454, "passes_attempted": 512, "short_passes_completed": 105, "medium_passes_completed": 314, "long_passes_completed": 35, "backward_passes_completed": 87, "passes_completed_to_left": 120, "passes_completed_to_right": 127, "free_kicks_taken": 9, "passes_into_attacking_third": 38, "passes_into_key_play_area": 17, "passes_into_penalty_area": 10, "crossing_accuracy_percent": 10, "crosses_completed": 2, "crosses_attempted": 20, "times_in_possession": 146},
            {"team": "England", "possession_percent": 53, "passing_accuracy_percent": 91, "passes_completed": 544, "passes_attempted": 600, "short_passes_completed": 144, "medium_passes_completed": 360, "long_passes_completed": 40, "backward_passes_completed": 127, "passes_completed_to_left": 147, "passes_completed_to_right": 147, "free_kicks_taken": 7, "passes_into_attacking_third": 42, "passes_into_key_play_area": 19, "passes_into_penalty_area": 9, "crossing_accuracy_percent": 15, "crosses_completed": 3, "crosses_attempted": 20, "times_in_possession": 153}
        ],
        "defending_stats": [
            {"team": "Serbia", "balls_recovered": 29, "blocks": 1, "penalties_conceded": 0, "tackles": 20, "tackles_won": 13, "tackles_lost": 7, "clearances_completed": 14, "clearances_attempted": 17},
            {"team": "England", "balls_recovered": 44, "blocks": 1, "penalties_conceded": 0, "tackles": 20, "tackles_won": 13, "tackles_lost": 4, "clearances_completed": 17, "clearances_attempted": 20}
        ],
        "goalkeeping_stats": [
            {"team": "Serbia", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 1, "low_claims": 0, "punches_made": 1},
            {"team": "England", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 1, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 1, "high_claims": 0, "low_claims": 1, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Serbia", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 19, "fouls_committed_in_defensive_third": 5, "fouls_committed_in_own_half": 12},
            {"team": "England", "yellow_cards": 0, "red_cards": 0, "fouls_committed": 8, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 3}
        ]
    }
