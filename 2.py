class UndergroundSystem:
    def __init__(self):
        self._check_in: dict[int, tuple[str, int]] = {}
        self._routes: dict[tuple[str, str], list[int]] = {}

    def check_in(self, passenger_id: int, station: str, time: int) -> None:
        if passenger_id in self._check_in:
            raise ValueError(f"Passenger {passenger_id} already checked in")
        self._check_in[passenger_id] = (station, time)

    def check_out(self, passenger_id: int, station: str, time: int) -> None:
        if passenger_id not in self._check_in:
            raise ValueError(f"Passenger {passenger_id} has not checked in")
        start_station, start_time = self._check_in.pop(passenger_id)
        route = (start_station, station)
        if route not in self._routes:
            self._routes[route] = [0, 0]
        self._routes[route][0] += time - start_time
        self._routes[route][1] += 1

    def get_average_time(self, start_station: str, end_station: str) -> float:
        route = (start_station, end_station)
        if route not in self._routes:
            raise KeyError(f"No trips found for route {start_station} -> {end_station}")
        total_time, count = self._routes[route]
        return total_time / count
