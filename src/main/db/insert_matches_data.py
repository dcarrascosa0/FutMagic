import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Match, Team, KeyStat, AttackingStat, DistributionStat, DefendingStat, GoalkeepingStat, \
    DisciplinaryStat, Base
import importlib.util


def insert_match_data(match_data, session):
    """
    Insert match data into the database. Skip insertion if the match already exists.

    Args:
        match_data (dict): Data of the match to be inserted.
        session (Session): SQLAlchemy session for database operations.
    """

    def get_or_create_team(team_name):
        team = session.query(Team).filter_by(team_name=team_name).first()
        if not team:
            team = Team(team_name=team_name)
            session.add(team)
            session.commit()
        return team

    match_info = match_data["match"]
    existing_match = session.query(Match).filter_by(match_name=match_info["match_name"],
                                                    match_date=match_info["match_date"]).first()
    if existing_match:
        print(f"Match '{match_info['match_name']}' on {match_info['match_date']} already exists. Skipping insertion.")
        return

    match = Match(
        match_name=match_info["match_name"],
        match_date=match_info["match_date"],
        venue=match_info["venue"],
        score=match_info["score"]
    )
    session.add(match)
    session.commit()

    match_id = match.match_id

    teams = {team_name: get_or_create_team(team_name) for team_name in match_data["teams"]}

    key_stats = [KeyStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                         **{k: v for k, v in stat.items() if k != "team"}) for stat in match_data["key_stats"]]
    attacking_stats = [AttackingStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                                     **{k: v for k, v in stat.items() if k != "team"}) for stat in
                       match_data["attacking_stats"]]
    distribution_stats = [DistributionStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                                           **{k: v for k, v in stat.items() if k != "team"}) for stat in
                          match_data["distribution_stats"]]
    defending_stats = [DefendingStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                                     **{k: v for k, v in stat.items() if k != "team"}) for stat in
                       match_data["defending_stats"]]
    goalkeeping_stats = [GoalkeepingStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                                         **{k: v for k, v in stat.items() if k != "team"}) for stat in
                         match_data["goalkeeping_stats"]]
    disciplinary_stats = [DisciplinaryStat(match_id=match_id, team_id=teams[stat["team"]].team_id,
                                           **{k: v for k, v in stat.items() if k != "team"}) for stat in
                          match_data["disciplinary_stats"]]

    session.bulk_save_objects(
        key_stats + attacking_stats + distribution_stats + defending_stats + goalkeeping_stats + disciplinary_stats)
    session.commit()


def main():
    load_dotenv()
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL not found in .env file.")

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    data_folder = 'data'
    match_files = os.listdir(data_folder)
    for file_name in match_files:
        if file_name.endswith('.py') and file_name != '__init__.py':
            module_name = file_name[:-3]
            module_path = os.path.join(data_folder, file_name)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                get_data_function = getattr(module, 'get_match_data', None)
                if callable(get_data_function):
                    match_data = get_data_function()
                    insert_match_data(match_data, session)
            else:
                print(f"Failed to load module: {file_name}")

    print("All match statistics inserted successfully.")


if __name__ == "__main__":
    main()
