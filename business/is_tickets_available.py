trains_range = ["805Ч", "211А"]


def is_tickets_available(request) -> tuple[bool, str]:
    trains = request.get("Trains")
    if trains:
        needed_trains = []

        for train in trains:
            train_number = train.get("TrainNumber")
            if train_number in trains_range:
                needed_trains.append(train)

        for train in needed_trains:
            car_groups = train.get("CarGroups")
            if len(car_groups) != 0:
                return True, train.get("TrainNumber")

    return False, ""
