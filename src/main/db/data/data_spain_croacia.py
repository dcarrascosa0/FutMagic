# data_spain_croatia.py

def get_match_data():
    return {
        "match": {
            "match_name": "Spain vs Croatia",
            "match_date": "2024-07-09",
            "venue": "Stadium Name",
            "score": "3-0"
        },
        "teams": ["Spain", "Croatia"],
        "key_stats": [
            {"team": "Spain", "possession_percent": 46, "total_attempts": 11, "attacks": 33, "corners_taken": 5, "passing_accuracy_percent": 86, "passes_completed": 392, "passes_attempted": 455, "balls_recovered": 36, "offsides": 2, "saves": 5, "distance_covered_km": 118.1, "yellow_cards": 1, "red_cards": 0},
            {"team": "Croatia", "possession_percent": 54, "total_attempts": 16, "attacks": 32, "corners_taken": 0, "passing_accuracy_percent": 88, "passes_completed": 467, "passes_attempted": 528, "balls_recovered": 29, "offsides": 0, "saves": 2, "distance_covered_km": 118.6, "yellow_cards": 0, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "Spain", "goals": 3, "goals_inside_area": 3, "goals_outside_area": 0, "total_attempts": 11, "attempts_on_target": 5, "attempts_off_target": 3, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 0, "assists": 3, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 33, "clear_chances": 0, "corners_taken": 5, "offsides": 2, "dribbles": 19, "runs_into_attacking_third": 9, "runs_into_key_play_area": 10, "runs_into_penalty_area": 10},
            {"team": "Croatia", "goals": 0, "goals_inside_area": 0, "goals_outside_area": 0, "total_attempts": 16, "attempts_on_target": 5, "attempts_off_target": 8, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 2, "assists": 0, "penalties_scored": 0, "penalties_missed": 1, "penalties_awarded": 1, "attacks": 32, "clear_chances": 2, "corners_taken": 0, "offsides": 0, "dribbles": 12, "runs_into_attacking_third": 12, "runs_into_key_play_area": 11, "runs_into_penalty_area": 3}
        ],
        "distribution_stats": [
            {"team": "Spain", "possession_percent": 46, "passing_accuracy_percent": 86, "passes_completed": 392, "passes_attempted": 455, "short_passes_completed": 106, "medium_passes_completed": 247, "long_passes_completed": 39, "backward_passes_completed": 102, "passes_completed_to_left": 107, "passes_completed_to_right": 93, "free_kicks_taken": 13, "passes_into_attacking_third": 35, "passes_into_key_play_area": 17, "passes_into_penalty_area": 8, "crossing_accuracy_percent": 36, "crosses_completed": 4, "crosses_attempted": 11, "times_in_possession": 156},
            {"team": "Croatia", "possession_percent": 54, "passing_accuracy_percent": 88, "passes_completed": 467, "passes_attempted": 528, "short_passes_completed": 137, "medium_passes_completed": 296, "long_passes_completed": 34, "backward_passes_completed": 84, "passes_completed_to_left": 134, "passes_completed_to_right": 143, "free_kicks_taken": 15, "passes_into_attacking_third": 33, "passes_into_key_play_area": 19, "passes_into_penalty_area": 7, "crossing_accuracy_percent": 29, "crosses_completed": 4, "crosses_attempted": 14, "times_in_possession": 159}
        ],
        "defending_stats": [
            {"team": "Spain", "balls_recovered": 36, "blocks": 3, "penalties_conceded": 1, "tackles": 8, "tackles_won": 1, "tackles_lost": 7, "clearances_completed": 6, "clearances_attempted": 9},
            {"team": "Croatia", "balls_recovered": 29, "blocks": 3, "penalties_conceded": 0, "tackles": 11, "tackles_won": 4, "tackles_lost": 7, "clearances_completed": 5, "clearances_attempted": 5}
        ],
        "goalkeeping_stats": [
            {"team": "Spain", "goals_conceded": 0, "own_goals_conceded": 0, "clean_sheets": 1, "saves": 5, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 1, "claims": 3, "high_claims": 0, "low_claims": 3, "punches_made": 0},
            {"team": "Croatia", "goals_conceded": 3, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 1, "low_claims": 2, "punches_made": 0}
        ],
        "disciplinary_stats": [
            {"team": "Spain", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 14, "fouls_committed_in_defensive_third": 2, "fouls_committed_in_own_half": 5},
            {"team": "Croatia", "yellow_cards": 0, "red_cards": 0, "fouls_committed": 13, "fouls_committed_in_defensive_third": 3, "fouls_committed_in_own_half": 6}
        ]
    }
