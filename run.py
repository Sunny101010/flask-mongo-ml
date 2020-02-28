#!flask/bin/python
import os
from app import app
#Load this config object for development mode
#app.config.from_object('configurations.DevelopmentConfig')
#port = 8080
#port = int(os.getenv("PORT"))
#app.run(host='0.0.0.0', port=port)
app.run(debug = True)