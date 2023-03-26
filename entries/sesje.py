from flask import request,session

import app

@app.before_request
def _last_page_visited():
    if "current_page" in session:
        session['last_page_visited'] = session['current_page']
    session['last_page_visited'] = request.path
    # session.permanent = True