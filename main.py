from app import app, db
import views
import models
from entries.blueprint import entries
import admin

app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run()
