# data_netherlands_turkiye.py

def get_match_data():
    return {
        "match": {
            "match_name": "Netherlands vs Turkiye",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "2-1"
        },
        "teams": ["Netherlands", "Turkiye"],
        "key_stats": [
            {"team": "Netherlands", "possession_percent": 56, "total_attempts": 11, "attacks": 52, "corners_taken": 3, "passing_accuracy_percent": 90, "passes_completed": 480, "passes_attempted": 531, "balls_recovered": 31, "offsides": 4, "saves": 3, "distance_covered_km": 109.3, "yellow_cards": 4, "red_cards": 0},
            {"team": "Turkiye", "possession_percent": 44, "total_attempts": 15, "attacks": 31, "corners_taken": 7, "passing_accuracy_percent": 84, "passes_completed": 310, "passes_attempted": 371, "balls_recovered": 29, "offsides": 2, "saves": 3, "distance_covered_km": 109.7, "yellow_cards": 2, "red_cards": 1}
        ],
        "attacking_stats": [
            {"team": "Netherlands", "goals": 2, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 11, "attempts_on_target": 4, "attempts_off_target": 4, "blocks": 4, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 1, "off_target_outside_area": 2, "assists": 2, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 52, "clear_chances": 0, "corners_taken": 3, "offsides": 4, "dribbles": 18, "runs_into_attacking_third": 29, "runs_into_key_play_area": 19, "runs_into_penalty_area": 15},
            {"team": "Turkiye", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 15, "attempts_on_target": 4, "attempts_off_target": 7, "blocks": 3, "woodwork": 0, "crossbar": 0, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 2, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 31, "clear_chances": 0, "corners_taken": 7, "offsides": 2, "dribbles": 18, "runs_into_attacking_third": 15, "runs_into_key_play_area": 13, "runs_into_penalty_area": 7}
        ],
        "distribution_stats": [
            {"team": "Netherlands", "possession_percent": 56, "passing_accuracy_percent": 90, "passes_completed": 480, "passes_attempted": 531, "short_passes_completed": 123, "medium_passes_completed": 336, "long_passes_completed": 21, "backward_passes_completed": 67, "passes_completed_to_left": 151, "passes_completed_to_right": 138, "free_kicks_taken": 9, "passes_into_attacking_third": 44, "passes_into_key_play_area": 34, "passes_into_penalty_area": 10, "crossing_accuracy_percent": 23, "crosses_completed": 3, "crosses_attempted": 13, "times_in_possession": 160},
            {"team": "Turkiye", "possession_percent": 44, "passing_accuracy_percent": 84, "passes_completed": 310, "passes_attempted": 371, "short_passes_completed": 88, "medium_passes_completed": 187, "long_passes_completed": 35, "backward_passes_completed": 67, "passes_completed_to_left": 86, "passes_completed_to_right": 102, "free_kicks_taken": 19, "passes_into_attacking_third": 18, "passes_into_key_play_area": 10, "passes_into_penalty_area": 9, "crossing_accuracy_percent": 32, "crosses_completed": 3, "crosses_attempted": 13, "times_in_possession": 162}
        ],
        "defending_stats": [
            {"team": "Netherlands", "balls_recovered": 31, "blocks": 4, "penalties_conceded": 0, "tackles": 10, "tackles_won": 4, "tackles_lost": 6, "clearances_completed": 15, "clearances_attempted": 18},
            {"team": "Turkiye", "balls_recovered": 29, "blocks": 3, "penalties_conceded": 0, "tackles": 18, "tackles_won": 9, "tackles_lost": 9, "clearances_completed": 8, "clearances_attempted": 12}
        ],
        "goalkeeping_stats": [
            {"team": "Netherlands", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 2, "low_claims": 1, "punches_made": 1},
            {"team": "Turkiye", "goals_conceded": 2, "own_goals_conceded": 1, "clean_sheets": 0, "saves": 3, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 3, "high_claims": 0, "low_claims": 1, "punches_made": 2}
        ],
        "disciplinary_stats": [
            {"team": "Netherlands", "yellow_cards": 4, "red_cards": 0, "fouls_committed": 15, "fouls_committed_in_defensive_third": 5, "fouls_committed_in_own_half": 7},
            {"team": "Turkiye", "yellow_cards": 2, "red_cards": 1, "fouls_committed": 7, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 5}
        ]
    }
