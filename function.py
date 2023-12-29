import datetime as dt

new_month = dt.date.today().replace(day=28) + dt.timedelta (days = 4)
eo_month = new_month.replace(day=1)-dt.timedelta(days = 1)
prior_eo_month = eo_month.replace(day=1)-dt.timedelta(days = 1)

print(eo_month, prior_eo_month)