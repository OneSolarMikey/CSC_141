#

def make_car(manufacturer, model, **car_info):
    car_details = {
        'manufacturer': manufacturer,
        'model': model,
    }
    car_details.update(car_info)
    return car_details

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
