import sqlite3
import os
from .models import TvModel, FridgeModel


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# def update_clicks(id, clicks, db):
#     conn = sqlite3.connect(BASE_DIR + '/db.sqlite3', check_same_thread=False)
#     c = conn.cursor()
#     c.execute("UPDATE " + db + " SET clicks = (?) WHERE id = (?)",
#               (str(clicks), str(id)))
#     conn.commit()
#     conn.close()

def update_tv_clicks(id, clicks):
    tv_model = TvModel.objects.filter(id=id)
    tv_model.clicks = clicks
    tv_model.save()


def update_fridge_clicks(id, clicks):
    fridge_model = FridgeModel.objects.filter(id=id)
    fridge_model.clicks = clicks
    fridge_model.save()

