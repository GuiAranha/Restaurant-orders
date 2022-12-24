class TrackOrders:
    def __init__(self):
        self._days = {}
        self._orders = []
        self._length = 0

    def __len__(self):
        return self._length

    def add_new_order(self, customer, order, day):
        self._orders.append([customer, order, day])
        self._length += 1

        if day in self._days:
            self._days[day] += 1
        else:
            self._days[day] = 1

    def count_orders(self, orders, customer, product=""):
        orders_count = {}

        for name, dish, _ in orders:
            if name == customer:
                if dish not in orders_count:
                    orders_count[dish] = 1
                else:
                    orders_count[dish] += 1

        if product:
            return orders_count[product]

        return orders_count

    def most_ordered(self, orders, client):
        counter = self.count_orders(orders, client)
        return max(counter.items(), key=lambda x: x[1])[0]

    def get_most_ordered_dish_per_customer(self, customer):
        return self.most_ordered(self._orders, customer)

    def get_never_ordered_per_customer(self, customer):
        foods = set()
        client_foods = set()

        for _, food, _ in self._orders:
            foods.add(food)

        for name, food, _ in self._orders:
            if name == customer:
                client_foods.add(food)
        return foods.difference(client_foods)

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        client_days = set()

        for _, _, day in self._orders:
            days.add(day)

        for name, _, day in self._orders:
            if name == customer:
                client_days.add(day)

        return days.difference(client_days)

    def get_busiest_day(self):
        return max(self._days.items(), key=lambda x: x[1])[0]

    def get_least_busy_day(self):
        return min(self._days.items(), key=lambda x: x[1])[0]
