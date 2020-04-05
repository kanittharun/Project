from app import app, db
from app.models import FallEvent


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'FallEvent': FallEvent}
