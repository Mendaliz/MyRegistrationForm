from flask import Flask, render_template, redirect

from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm


inf = "db/mars_explorer.db"

db_session.global_init(inf)
session = db_session.create_session()

session.query(User).filter(User.address == "module_1", User.age < 21).update({User.address: "module_3"},
                                                                             synchronize_session="evaluate")


jobs = session.query(Jobs).all()

max_len = len(max(jobs, key=lambda x: len(x.collaborators.split(", "))).collaborators.split(", "))
ids = list(map(lambda x: x.team_leader, filter(lambda y: len(y.collaborators.split(", ")) == max_len, jobs)))
users = session.query(User).filter(User.id in ids).all()
print("\n".join([str(i) for i in users]))
