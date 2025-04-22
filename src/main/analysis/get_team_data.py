import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from src.main.db.schema import Team, KeyStat, AttackingStat, DistributionStat, DefendingStat, GoalkeepingStat, DisciplinaryStat, Match

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
database_url = os.getenv('DATABASE_URL')
if database_url is None:
    raise ValueError("DATABASE_URL not found in .env file.")

def get_team_data(team_name):
    # Database connection
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get team ID
        team = session.query(Team).filter(Team.team_name == team_name).one()
        team_id = team.team_id

        # Fetch individual stats
        key_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(KeyStat).filter(KeyStat.team_id == team_id).all()]
        attacking_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(AttackingStat).filter(AttackingStat.team_id == team_id).all()]
        distribution_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(DistributionStat).filter(DistributionStat.team_id == team_id).all()]
        defending_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(DefendingStat).filter(DefendingStat.team_id == team_id).all()]
        goalkeeping_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(GoalkeepingStat).filter(GoalkeepingStat.team_id == team_id).all()]
        disciplinary_stats = [serialize_sqlalchemy_object(stat) for stat in session.query(DisciplinaryStat).filter(DisciplinaryStat.team_id == team_id).all()]

        match_ids = [stat['match_id'] for stat in key_stats]
        matches = session.query(Match).filter(Match.match_id.in_(match_ids)).all()
        matches_dict = {match.match_id: {"date": match.match_date, "result": match.score, "name": match.match_name} for match in matches}

        # Compute average stats
        average_stats = {
            "key_stats": compute_average_stats(key_stats),
            "attacking_stats": compute_average_stats(attacking_stats),
            "distribution_stats": compute_average_stats(distribution_stats),
            "defending_stats": compute_average_stats(defending_stats),
            "goalkeeping_stats": compute_average_stats(goalkeeping_stats),
            "disciplinary_stats": compute_average_stats(disciplinary_stats)
        }

        individual_stats = {
            "key_stats": [
                {"date": matches_dict[stat["match_id"]]["date"], "result": matches_dict[stat["match_id"]]["result"], "name": matches_dict[stat["match_id"]]["name"], **stat}
                for stat in key_stats
            ],
            "attacking_stats": attacking_stats,
            "distribution_stats": distribution_stats,
            "defending_stats": defending_stats,
            "goalkeeping_stats": goalkeeping_stats,
            "disciplinary_stats": disciplinary_stats
        }

        return {
            "team_name": team_name,
            "average_stats": average_stats,
            "individual_stats": individual_stats
        }
    except Exception as e:
        print(f"Error fetching data for team {team_name}: {e}")
        return None
    finally:
        session.close()

def serialize_sqlalchemy_object(obj):
    return {key: value for key, value in obj.__dict__.items() if not key.startswith('_')}

def compute_average_stats(stats):
    if not stats:
        return {}
    avg_stats = {}
    count = len(stats)
    for stat in stats:
        for key, value in stat.items():
            if key not in avg_stats:
                avg_stats[key] = value
            else:
                avg_stats[key] += value
    for key in avg_stats:
        avg_stats[key] /= count
    return avg_stats
