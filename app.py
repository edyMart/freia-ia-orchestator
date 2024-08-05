from flask import Flask
from routes.Services import Services_BP
from routes.Oauth import Oauth_BP
from routes.Billing import Billing_BP

from middlewares.Oauth import OauthMiddleware

app = Flask(__name__)

v = "v0"
path = f"""/orchestrator/api/{v}/"""


# Middlewares
app.before_request(OauthMiddleware)

app.register_blueprint(Services_BP, url_prefix=f"""{path}/agent""")
app.register_blueprint(Oauth_BP, url_prefix=f"""{path}/oauth""")
app.register_blueprint(Billing_BP, url_prefix=f"""{path}/billing""")


if __name__ == '__main__':
    app.run()
