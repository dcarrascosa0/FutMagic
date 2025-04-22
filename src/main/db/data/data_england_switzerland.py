# data_england_switzerland.py

def get_match_data():
    return {
        "match": {
            "match_name": "England vs Switzerland",
            "match_date": "2024-07-10",
            "venue": "Stadium Name",
            "score": "1-1"
        },
        "teams": ["England", "Switzerland"],
        "key_stats": [
            {"team": "England", "possession_percent": 51, "total_attempts": 13, "attacks": 75, "corners_taken": 4, "passing_accuracy_percent": 92, "passes_completed": 626, "passes_attempted": 680, "balls_recovered": 44, "offsides": 3, "saves": 2, "distance_covered_km": 142.6, "yellow_cards": 1, "red_cards": 0},
            {"team": "Switzerland", "possession_percent": 49, "total_attempts": 12, "attacks": 51, "corners_taken": 3, "passing_accuracy_percent": 93, "passes_completed": 583, "passes_attempted": 627, "balls_recovered": 40, "offsides": 0, "saves": 2, "distance_covered_km": 145.9, "yellow_cards": 2, "red_cards": 0}
        ],
        "attacking_stats": [
            {"team": "England", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 13, "attempts_on_target": 3, "attempts_off_target": 2, "blocks": 2, "woodwork": 0, "crossbar": 1, "post": 0, "on_target_outside_area": 2, "off_target_outside_area": 0, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 75, "clear_chances": 0, "corners_taken": 4, "offsides": 3, "dribbles": 18, "runs_into_attacking_third": 20, "runs_into_key_play_area": 18, "runs_into_penalty_area": 12},
            {"team": "Switzerland", "goals": 1, "goals_inside_area": 1, "goals_outside_area": 0, "total_attempts": 12, "attempts_on_target": 3, "attempts_off_target": 7, "blocks": 8, "woodwork": 1, "crossbar": 0, "post": 0, "on_target_outside_area": 0, "off_target_outside_area": 2, "assists": 1, "penalties_scored": 0, "penalties_missed": 0, "penalties_awarded": 0, "attacks": 51, "clear_chances": 0, "corners_taken": 3, "offsides": 0, "dribbles": 18, "runs_into_attacking_third": 17, "runs_into_key_play_area": 10, "runs_into_penalty_area": 12}
        ],
        "distribution_stats": [
            {"team": "England", "possession_percent": 51, "passing_accuracy_percent": 92, "passes_completed": 626, "passes_attempted": 680, "short_passes_completed": 113, "medium_passes_completed": 456, "long_passes_completed": 57, "backward_passes_completed": 118, "passes_completed_to_left": 193, "passes_completed_to_right": 170, "free_kicks_taken": 13, "passes_into_attacking_third": 74, "passes_into_key_play_area": 51, "passes_into_penalty_area": 10, "crossing_accuracy_percent": 14, "crosses_completed": 3, "crosses_attempted": 21, "times_in_possession": 183},
            {"team": "Switzerland", "possession_percent": 49, "passing_accuracy_percent": 93, "passes_completed": 583, "passes_attempted": 627, "short_passes_completed": 152, "medium_passes_completed": 390, "long_passes_completed": 41, "backward_passes_completed": 106, "passes_completed_to_left": 171, "passes_completed_to_right": 169, "free_kicks_taken": 11, "passes_into_attacking_third": 59, "passes_into_key_play_area": 36, "passes_into_penalty_area": 12, "crossing_accuracy_percent": 29, "crosses_completed": 5, "crosses_attempted": 17, "times_in_possession": 179}
        ],
        "defending_stats": [
            {"team": "England", "balls_recovered": 44, "blocks": 2, "penalties_conceded": 0, "tackles": 15, "tackles_won": 10, "tackles_lost": 5, "clearances_completed": 17, "clearances_attempted": 25},
            {"team": "Switzerland", "balls_recovered": 40, "blocks": 8, "penalties_conceded": 0, "tackles": 15, "tackles_won": 6, "tackles_lost": 9, "clearances_completed": 20, "clearances_attempted": 25}
        ],
        "goalkeeping_stats": [
            {"team": "England", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 2, "high_claims": 1, "low_claims": 1, "punches_made": 0},
            {"team": "Switzerland", "goals_conceded": 1, "own_goals_conceded": 0, "clean_sheets": 0, "saves": 2, "saves_from_direct_free_kicks": 0, "saves_from_indirect_free_kicks": 0, "saves_from_penalties": 0, "claims": 4, "high_claims": 1, "low_claims": 3, "punches_made": 1}
        ],
        "disciplinary_stats": [
            {"team": "England", "yellow_cards": 1, "red_cards": 0, "fouls_committed": 8, "fouls_committed_in_defensive_third": 0, "fouls_committed_in_own_half": 5},
            {"team": "Switzerland", "yellow_cards": 2, "red_cards": 0, "fouls_committed": 13, "fouls_committed_in_defensive_third": 1, "fouls_committed_in_own_half": 5}
        ]
    }
