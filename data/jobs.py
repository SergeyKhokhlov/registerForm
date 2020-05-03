import sqlalchemy
from .db_session import SqlAlchemyBase


class Job(SqlAlchemyBase):
    __tablename__ = 'jobs'

    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
