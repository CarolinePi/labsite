from .models import TvModel, FridgeModel


def update_tv_clicks(id, clicks):
    tv_model = TvModel.objects.get(id=id)
    tv_model.clicks = clicks
    tv_model.save()


def update_fridge_clicks(id, clicks):
    fridge_model = FridgeModel.objects.get(id=id)
    fridge_model.clicks = clicks
    fridge_model.save()

