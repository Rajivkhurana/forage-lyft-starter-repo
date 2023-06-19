from datetime import datetime


class Calliope:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        today = datetime.today().date()
        time_delta = today - self.last_service_date
        mileage_delta = self.current_mileage - self.last_service_mileage
        if time_delta.days >= 1095 or mileage_delta >= 30000:
            return True
        return False

    def check_tire_service(self, tire_wear):
        return False


class Glissade:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        today = datetime.today().date()
        time_delta = today - self.last_service_date
        mileage_delta = self.current_mileage - self.last_service_mileage
        if time_delta.days >= 1095 or mileage_delta >= 60000:
            return True
        return False

    def check_tire_service(self, tire_wear):
        return False


class Palindrome:
    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        today = datetime.today().date()
        time_delta = today - self.last_service_date
        if time_delta.days >= 1825 or self.warning_light_is_on:
            return True
        return False

    def check_tire_service(self, tire_wear):
        return False


class Rorschach:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        today = datetime.today().date()
        time_delta = today - self.last_service_date
        mileage_delta = self.current_mileage - self.last_service_mileage
        if time_delta.days >= 1825 or mileage_delta >= 60000:
            return True
        return False

    def check_tire_service(self, tire_wear):
        return False


class Thovex:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        today = datetime.today().date()
        time_delta = today - self.last_service_date
        mileage_delta = self.current_mileage - self.last_service_mileage
        if time_delta.days >= 1825 or mileage_delta >= 30000:
            return True
        return False

    def check_tire_service(self, tire_wear):
        return False


class CarFactory:
    def __init__(self, car_type):
        self.car_type = car_type

    def manufacture_car(self, last_service_date, current_mileage, last_service_mileage):
        if self.car_type == "Calliope":
            return Calliope(last_service_date, current_mileage, last_service_mileage)
        elif self.car_type == "Glissade":
            return Glissade(last_service_date, current_mileage, last_service_mileage)
        elif self.car_type == "Palindrome":
            return Palindrome(last_service_date, current_mileage, last_service_mileage)
        elif self.car_type == "Rorschach":
            return Rorschach(last_service_date, current_mileage, last_service_mileage)
        elif self.car_type == "Thovex":
            return Thovex(last_service_date, current_mileage, last_service_mileage)
        else:
            return None


class LyftFleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_needing_service(self):
        cars_needing_service = []
        for car in self.cars:
            if car.needs_service():
                cars_needing_service.append(car)
        return cars_needing_service


if __name__ == "__main__":
    fleet = LyftFleet()

    car_factory = CarFactory("Calliope")
    car1 = car_factory.manufacture_car(datetime(2020, 1, 1), 50000, 40000)
    fleet.add_car(car1)

    car_factory = CarFactory("Glissade")
    car2 = car_factory.manufacture_car(datetime(2020, 6, 1), 80000, 70000)
    fleet.add_car(car2)

    car_factory = CarFactory("Palindrome")
    car3 = car_factory.manufacture_car(datetime(2019, 1, 1), 100000, 90000)
    fleet.add_car(car3)

    car_factory = CarFactory("Rorschach")
    car4 = car_factory.manufacture_car(datetime(2018, 1, 1), 120000, 110000)
    fleet.add_car(car4)

    car_factory = CarFactory("Thovex")
    car5 = car_factory.manufacture_car(datetime(2019, 6, 1), 70000, 60000)
    fleet.add_car(car5)

    # Check tire servicing criteria for Carrigan and Octoprime tires
    carrigan_tire_wear = [0.7, 0.8, 0.9, 1.0]
    octoprime_tire_wear = [0.5, 0.6, 0.7, 0.8]
    for car in fleet.cars:
        if car.check_tire_service(carrigan_tire_wear):
            print(f"{car.car_type} needs tire service for Carrigan tires.")
        if car.check_tire_service(octoprime_tire_wear):
            print(f"{car.car_type} needs tire service for Octoprime tires.")
