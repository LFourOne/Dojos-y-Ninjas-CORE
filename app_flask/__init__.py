from flask import Flask

app = Flask(__name__)
app.secret_key = "Shhhh, stay quiet!"

DATA_BASE = "esquema_dojos_y_ninjas"