import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main.db.schema import Team, KeyStat, AttackingStat, DistributionStat, DefendingStat, GoalkeepingStat, DisciplinaryStat

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
database_url = os.getenv('DATABASE_URL')
if database_url is None:
    raise ValueError("DATABASE_URL not found in .env file.")
# Database connection
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()


def get_team_stats(team_name):
    key_stats = session.query(KeyStat).join(Team).filter(Team.team_name == team_name).all()
    attacking_stats = session.query(AttackingStat).join(Team).filter(Team.team_name == team_name).all()
    distribution_stats = session.query(DistributionStat).join(Team).filter(Team.team_name == team_name).all()
    defending_stats = session.query(DefendingStat).join(Team).filter(Team.team_name == team_name).all()
    goalkeeping_stats = session.query(GoalkeepingStat).join(Team).filter(Team.team_name == team_name).all()
    disciplinary_stats = session.query(DisciplinaryStat).join(Team).filter(Team.team_name == team_name).all()

    return {
        "key_stats": key_stats,
        "attacking_stats": attacking_stats,
        "distribution_stats": distribution_stats,
        "defending_stats": defending_stats,
        "goalkeeping_stats": goalkeeping_stats,
        "disciplinary_stats": disciplinary_stats
    }


def summarize_stats(stats):
    summary = {}

    # Summarize key stats
    possession = [stat.possession_percent for stat in stats["key_stats"]]
    total_attempts = [stat.total_attempts for stat in stats["key_stats"]]

    summary["average_possession"] = sum(possession) / len(possession)
    summary["average_total_attempts"] = sum(total_attempts) / len(total_attempts)

    # Summarize attacking stats
    goals = [stat.goals for stat in stats["attacking_stats"]]
    attempts_on_target = [stat.attempts_on_target for stat in stats["attacking_stats"]]

    summary["average_goals"] = sum(goals) / len(goals)
    summary["average_attempts_on_target"] = sum(attempts_on_target) / len(attempts_on_target)

    # Summarize distribution stats
    passes_completed = [stat.passes_completed for stat in stats["distribution_stats"]]
    passing_accuracy = [stat.passing_accuracy_percent for stat in stats["distribution_stats"]]

    summary["average_passes_completed"] = sum(passes_completed) / len(passes_completed)
    summary["average_passing_accuracy"] = sum(passing_accuracy) / len(passing_accuracy)

    # Summarize defending stats
    balls_recovered = [stat.balls_recovered for stat in stats["defending_stats"]]
    tackles = [stat.tackles for stat in stats["defending_stats"]]

    summary["average_balls_recovered"] = sum(balls_recovered) / len(balls_recovered)
    summary["average_tackles"] = sum(tackles) / len(tackles)

    # Summarize goalkeeping stats
    saves = [stat.saves for stat in stats["goalkeeping_stats"]]
    clean_sheets = [stat.clean_sheets for stat in stats["goalkeeping_stats"]]

    summary["average_saves"] = sum(saves) / len(saves)
    summary["average_clean_sheets"] = sum(clean_sheets) / len(clean_sheets)

    # Summarize disciplinary stats
    yellow_cards = [stat.yellow_cards for stat in stats["disciplinary_stats"]]
    red_cards = [stat.red_cards for stat in stats["disciplinary_stats"]]

    summary["average_yellow_cards"] = sum(yellow_cards) / len(yellow_cards)
    summary["average_red_cards"] = sum(red_cards) / len(red_cards)

    return summary


def main():
    team_name = "Spain"
    stats = get_team_stats(team_name)
    summary = summarize_stats(stats)

    print(f"Statistics Summary for {team_name}:")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")


if __name__ == "__main__":
    main()
