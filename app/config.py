import os
from sqlalchemy.pool import NullPool


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here (for production)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = os.environ.get('FLASK_ENV') != 'production'
    # On Vercel each function invocation is a fresh/ephemeral process, and the
    # DB URL points at Supabase's transaction-mode pooler (port 6543), which
    # already pools connections on the server side. Letting SQLAlchemy keep
    # its own idle QueuePool on top of that would hold extra connections open
    # against the shared Supabase project (also used by the live
    # zhang-marketplace app), so disable app-side pooling in production and
    # open/close a connection per checkout instead.
    if os.environ.get('FLASK_ENV') == 'production':
        SQLALCHEMY_ENGINE_OPTIONS = {"poolclass": NullPool}