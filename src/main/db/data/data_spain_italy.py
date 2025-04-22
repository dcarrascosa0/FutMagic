# data_spain_italy.py

def get_match_data():
    return {
        "match": {
            "match_name": "Spain vs Italy",
            "match_date": "2024-07-09",
            "venue": "Stadium Name",
            "score": "1-0"
        },
        "teams": ["Spain", "Italy"],
        "key_stats": [
            {"team": "Spain", "possession_percent": 57, "total_attempts": 20, "attacks": 56, "corners_taken": 5, "passing_accuracy_percent": 92, "passes_completed": 548, "passes_attempted": 594, "balls_recovered": 45, "offsides": 0, "saves": 1, "distance_covered_km": 116.9, "yellow_cards": 3, "red_cards": 0},
            {"team": "Italy", "possession_percent": 43, "total_attempts": 4, "attacks": 24, "corners_taken": 2, "passing_accuracy_percent": 86, "passes_completed": 381, "passes_attempted": 445, "balls_recovered": 40, "offsides": 0, "saves": 8, "distance_covered_km": 117.8, "yellow_cards": 2, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Spain", "goals": 1, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 20, "attempts_on_target": 8, "attempts_off_target": 8, "blocks": 0, "woodwork": 2, "crossbar": 1, "post": 1, "on_target_outside_area": 4, "off_target_outside_area": 3, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 56, "clear_chances": 2, "corners_taken": 5, "offsides": 0, "dribbles": 25, "runs_into_attacking_third": 34, "runs_into_key_play_area": 26, "runs_into_penalty_area": 11},
            {"team": "Italy", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 4, "attempts_on_target": 1, "attempts_off_target": 3, "blocks": 4, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 1, "assists": 0, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 24, "clear_chances": 0, "corners_taken": 2, "offsides": 0, "dribbles": 7, "runs_into_attacking_third": 8, "runs_into_key_play_area": 4, "runs_into_penalty_area": 3}
        ],
        "distribution_stats": [
            {"team": "Spain", "possession_percent": 57, "passing_accuracy_percent": 92, "passes_completed": 548, "passes_attempted": 594, "short_passes_completed": 89, "medium_passes_completed": 416, "long_passes_completed": 43, "backward_passes_completed": 107, "passes_completed_to_left": 150, "passes_completed_to_right": 157, "free_kicks_taken": 14, "passes_into_attacking_third": 44, "passes_into_key_play_area": 33, "passes_into_penalty_area": 13, "crossing_accuracy_percent": 38, "crosses_completed": 6, "crosses_attempted": 16, "times_in_possession": 163},
            {"team": "Italy", "possession_percent": 43, "passing_accuracy_percent": 86, "passes_completed": 381, "passes_attempted": 445, "short_passes_completed": 80, "medium_passes_completed": 268, "long_passes_completed": 33, "backward_passes_completed": 61, "passes_completed_to_left": 112, "passes_completed_to_right": 116, "free_kicks_taken": 17, "passes_into_attacking_third": 20, "passes_into_key_play_area": 14, "passes_into_penalty_area": 7, "crossing_accuracy_percent": 42, "crosses_completed": 5, "crosses_attempted": 12, "times_in_possession": 167}
        ],
        "defending_stats": [
            {"team": "Spain", "balls_recovered": 45, "blocks": 0, "penalties_conceded": 0, "tackles": 11, "tackles_won": 4, "tackles_lost": 7, "clearances_completed": 6, "clearances_attempted": 9},
            {"team": "Italy", "balls_recovered": 40, "blocks": 4, "penalties_conceded": 0, "tackles": 23, "tackles_won": 11, "tackles_lost": 12, "clearances_completed": 16, "clearances_attempted": 21}
        ],
        "goalkeeping_stats": [
            {"team": "Spain", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 1, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 1, "low_claims": 2, "punches_made": 0},
            {"team": "Italy", "goals_conceded": 1, "own_goals_conceded": 1, "clean_sheets": 0, "saves": 8, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 1, "low_claims": 1, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Spain", "yellow_cards": 3, "red_cards": 0, "fouls_committed": 17, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 6},
            {"team": "Italy", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 14, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 6}
        ]
    }
