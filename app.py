import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from src.main.db.schema import Team, KeyStat, AttackingStat, DistributionStat, DefendingStat, GoalkeepingStat, \
    DisciplinaryStat, Match

app = Flask(__name__)
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teams', methods=['GET'])
def get_teams():
    try:
        teams = session.query(Team).all()
        teams_list = [{"team_id": team.team_id, "team_name": team.team_name} for team in teams]
        return jsonify(teams_list)
    except exc.SQLAlchemyError as e:
        logging.error(f"Error fetching teams: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/team/<int:team_id>/stats', methods=['GET'])
def get_team_stats(team_id):
    try:
        logging.debug(f"Fetching stats for team_id: {team_id}")

        key_stats = [serialize_sqlalchemy_object(stat) for stat in
                     session.query(KeyStat).filter(KeyStat.team_id == team_id).all()]
        attacking_stats = [serialize_sqlalchemy_object(stat) for stat in
                           session.query(AttackingStat).filter(AttackingStat.team_id == team_id).all()]
        distribution_stats = [serialize_sqlalchemy_object(stat) for stat in
                              session.query(DistributionStat).filter(DistributionStat.team_id == team_id).all()]
        defending_stats = [serialize_sqlalchemy_object(stat) for stat in
                           session.query(DefendingStat).filter(DefendingStat.team_id == team_id).all()]
        goalkeeping_stats = [serialize_sqlalchemy_object(stat) for stat in
                             session.query(GoalkeepingStat).filter(GoalkeepingStat.team_id == team_id).all()]
        disciplinary_stats = [serialize_sqlalchemy_object(stat) for stat in
                              session.query(DisciplinaryStat).filter(DisciplinaryStat.team_id == team_id).all()]

        match_ids = [stat['match_id'] for stat in key_stats]
        matches = session.query(Match).filter(Match.match_id.in_(match_ids)).all()
        matches_dict = {match.match_id: {"date": match.match_date, "result": match.score, "match_name": match.match_name} for match in matches}

        if not (
                key_stats or attacking_stats or distribution_stats or defending_stats or goalkeeping_stats or disciplinary_stats):
            logging.warning(f"No stats found for team_id: {team_id}")
            return jsonify({"error": "No stats found"}), 404

        average_stats = {
            "key_stats": compute_average_stats(key_stats),
            "attacking_stats": compute_average_stats(attacking_stats),
            "distribution_stats": compute_average_stats(distribution_stats),
            "defending_stats": compute_average_stats(defending_stats),
            "goalkeeping_stats": compute_average_stats(goalkeeping_stats),
            "disciplinary_stats": compute_average_stats(disciplinary_stats)
        }

        return jsonify({
            "average_stats": average_stats,
            "individual_stats": {
                "key_stats": [
                    {"date": matches_dict[stat["match_id"]]["date"], "result": matches_dict[stat["match_id"]]["result"],
                     "match_name": matches_dict[stat["match_id"]]["match_name"], **stat} for stat in key_stats],
                "attacking_stats": attacking_stats,
                "distribution_stats": distribution_stats,
                "defending_stats": defending_stats,
                "goalkeeping_stats": goalkeeping_stats,
                "disciplinary_stats": disciplinary_stats
            }
        })
    except exc.SQLAlchemyError as e:
        logging.error(f"Error fetching stats for team_id {team_id}: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/team/<int:team_id>/match/<int:match_id>/stats', methods=['GET'])
def get_match_stats(team_id, match_id):
    try:
        logging.debug(f"Fetching stats for team_id: {team_id}, match_id: {match_id}")

        key_stats = [serialize_sqlalchemy_object(stat) for stat in
                     session.query(KeyStat).filter(KeyStat.team_id == team_id, KeyStat.match_id == match_id).all()]
        attacking_stats = [serialize_sqlalchemy_object(stat) for stat in
                           session.query(AttackingStat).filter(AttackingStat.team_id == team_id,
                                                               AttackingStat.match_id == match_id).all()]
        distribution_stats = [serialize_sqlalchemy_object(stat) for stat in
                              session.query(DistributionStat).filter(DistributionStat.team_id == team_id,
                                                                     DistributionStat.match_id == match_id).all()]
        defending_stats = [serialize_sqlalchemy_object(stat) for stat in
                           session.query(DefendingStat).filter(DefendingStat.team_id == team_id,
                                                               DefendingStat.match_id == match_id).all()]
        goalkeeping_stats = [serialize_sqlalchemy_object(stat) for stat in
                             session.query(GoalkeepingStat).filter(GoalkeepingStat.team_id == team_id,
                                                                   GoalkeepingStat.match_id == match_id).all()]
        disciplinary_stats = [serialize_sqlalchemy_object(stat) for stat in
                              session.query(DisciplinaryStat).filter(DisciplinaryStat.team_id == team_id,
                                                                     DisciplinaryStat.match_id == match_id).all()]

        if not (
                key_stats or attacking_stats or distribution_stats or defending_stats or goalkeeping_stats or disciplinary_stats):
            logging.warning(f"No stats found for team_id: {team_id}, match_id: {match_id}")
            return jsonify({"error": "No stats found"}), 404

        return jsonify({
            "key_stats": key_stats,
            "attacking_stats": attacking_stats,
            "distribution_stats": distribution_stats,
            "defending_stats": defending_stats,
            "goalkeeping_stats": goalkeeping_stats,
            "disciplinary_stats": disciplinary_stats
        })
    except exc.SQLAlchemyError as e:
        logging.error(f"Error fetching stats for team_id {team_id}, match_id {match_id}: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
