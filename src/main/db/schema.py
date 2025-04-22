from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Match(Base):
    __tablename__ = 'matches'
    match_id = Column(Integer, primary_key=True)
    match_name = Column(String(255), nullable=False)
    match_date = Column(Date, nullable=False)
    venue = Column(String(255), nullable=False)
    score = Column(String(10), nullable=False)

class Team(Base):
    __tablename__ = 'teams'
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(255), unique=True, nullable=False)

class KeyStat(Base):
    __tablename__ = 'key_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    possession_percent = Column(Float)
    total_attempts = Column(Integer)
    attacks = Column(Integer)
    corners_taken = Column(Integer)
    passing_accuracy_percent = Column(Float)
    passes_completed = Column(Integer)
    passes_attempted = Column(Integer)
    balls_recovered = Column(Integer)
    offsides = Column(Integer)
    saves = Column(Integer)
    distance_covered_km = Column(Float)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)

class AttackingStat(Base):
    __tablename__ = 'attacking_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    goals = Column(Integer)
    goals_inside_area = Column(Integer)
    goals_outside_area = Column(Integer)
    total_attempts = Column(Integer)
    attempts_on_target = Column(Integer)
    attempts_off_target = Column(Integer)
    blocks = Column(Integer)
    woodwork = Column(Integer)
    crossbar = Column(Integer)
    post = Column(Integer)
    on_target_outside_area = Column(Integer)
    off_target_outside_area = Column(Integer)
    assists = Column(Integer)
    penalties_scored = Column(Integer)
    penalties_missed = Column(Integer)
    penalties_awarded = Column(Integer)
    attacks = Column(Integer)
    clear_chances = Column(Integer)
    corners_taken = Column(Integer)
    offsides = Column(Integer)
    dribbles = Column(Integer)
    runs_into_attacking_third = Column(Integer)
    runs_into_key_play_area = Column(Integer)
    runs_into_penalty_area = Column(Integer)

class DistributionStat(Base):
    __tablename__ = 'distribution_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    possession_percent = Column(Float)
    passing_accuracy_percent = Column(Float)
    passes_completed = Column(Integer)
    passes_attempted = Column(Integer)
    short_passes_completed = Column(Integer)
    medium_passes_completed = Column(Integer)
    long_passes_completed = Column(Integer)
    backward_passes_completed = Column(Integer)
    passes_completed_to_left = Column(Integer)
    passes_completed_to_right = Column(Integer)
    free_kicks_taken = Column(Integer)
    passes_into_attacking_third = Column(Integer)
    passes_into_key_play_area = Column(Integer)
    passes_into_penalty_area = Column(Integer)
    crossing_accuracy_percent = Column(Float)
    crosses_completed = Column(Integer)
    crosses_attempted = Column(Integer)
    times_in_possession = Column(Integer)

class DefendingStat(Base):
    __tablename__ = 'defending_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    balls_recovered = Column(Integer)
    blocks = Column(Integer)
    penalties_conceded = Column(Integer)
    tackles = Column(Integer)
    tackles_won = Column(Integer)
    tackles_lost = Column(Integer)
    clearances_completed = Column(Integer)
    clearances_attempted = Column(Integer)

class GoalkeepingStat(Base):
    __tablename__ = 'goalkeeping_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    goals_conceded = Column(Integer)
    own_goals_conceded = Column(Integer)
    clean_sheets = Column(Integer)
    saves = Column(Integer)
    saves_from_direct_free_kicks = Column(Integer)
    saves_from_indirect_free_kicks = Column(Integer)
    saves_from_penalties = Column(Integer)
    claims = Column(Integer)
    high_claims = Column(Integer)
    low_claims = Column(Integer)
    punches_made = Column(Integer)

class DisciplinaryStat(Base):
    __tablename__ = 'disciplinary_stats'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    fouls_committed = Column(Integer)
    fouls_committed_in_defensive_third = Column(Integer)
    fouls_committed_in_own_half = Column(Integer)

def create_all_tables(engine):
    Base.metadata.create_all(engine)
