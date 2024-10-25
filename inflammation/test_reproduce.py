filename = "data/small-01.csv"
from inflammation import models, views
inflammation_data = models.load_csv(filename)
view_data = {'average': models.daily_mean(inflammation_data), 'max': models.daily_max(inflammation_data), 'min': models.daily_min(inflammation_data)}
views.visualize(view_data)
