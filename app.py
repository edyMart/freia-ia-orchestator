from flask import Flask
from routes.Services import Services_BP
app = Flask(__name__)

v = "v0"
path = f"""servicios/api/{v}"""

app.register_blueprint(Services_BP, url_prefix=f"""{path}""")

if __name__ == '__main__':
    app.run()
