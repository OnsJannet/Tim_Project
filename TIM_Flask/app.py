
#!/usr/bin/python3
"""
    creates a Flask web application
    that provides a REST API for a database of users.
    and regiter the blueprints for the auth and admin modules.
"""
from flask import Flask
from Bleuprints.auth import auth_bp
from Bleuprints.admin import admin_bp
from Bleuprints.calculations import calculations_bp
from Bleuprints.vehicleparc import vehicleparc_bp
from Bleuprints.activityanalysis import activityanalysis_bp
from Bleuprints.activitycontribution import activitycontribution_bp
from Bleuprints.balanceliabilities import balanceliabilities_bp
from Bleuprints.cashflowanalysis import cashflowanalysis_bp
from Bleuprints.costofsale import costofsale_bp
from Bleuprints.dealerarea import dealerarea_bp
from Bleuprints.financialincome import financialincome_bp
from Bleuprints.financialrequirements import financialrequirements_bp
from Bleuprints.invdepr import invdepr_bp
from Bleuprints.ratiobalance import ratiobalance_bp
from Bleuprints.salaries import salaries_bp
from Bleuprints.sellingoper import sellingoper_bp
from Bleuprints.turnoverpart import turnoverpart_bp
from Bleuprints.turnoverservices import turnoverservices_bp
from Bleuprints.turnovervehicle import turnovervehicle_bp
from Bleuprints.vat import vat_bp
from Bleuprints.pl import pl_bp
from Bleuprints.shorts import shorts_bp
from Bleuprints.calculationshort import calculationshorts_bp
from Bleuprints.shorts import shorts_bp
from Bleuprints.dealerbenchmark import dealerbenchmark_bp
from Bleuprints.balanceassets import balanceassets_bp
from Bleuprints.db_routes import db_bp

from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = 'secret_key'
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(calculations_bp)
app.register_blueprint(vehicleparc_bp)
app.register_blueprint(activityanalysis_bp)
app.register_blueprint(activitycontribution_bp)
app.register_blueprint(balanceliabilities_bp)
app.register_blueprint(cashflowanalysis_bp)
app.register_blueprint(costofsale_bp)
app.register_blueprint(dealerarea_bp)
app.register_blueprint(financialincome_bp)
app.register_blueprint(financialrequirements_bp)
app.register_blueprint(invdepr_bp)
app.register_blueprint(ratiobalance_bp)
app.register_blueprint(salaries_bp)
app.register_blueprint(sellingoper_bp)
app.register_blueprint(turnoverpart_bp)
app.register_blueprint(turnoverservices_bp)
app.register_blueprint(turnovervehicle_bp)
app.register_blueprint(vat_bp)
app.register_blueprint(pl_bp)
app.register_blueprint(shorts_bp)
app.register_blueprint(calculationshorts_bp)
app.register_blueprint(balanceassets_bp)
app.register_blueprint(dealerbenchmark_bp)
app.register_blueprint(db_bp)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)