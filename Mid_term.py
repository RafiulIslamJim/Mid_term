class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_show("dummy_id", "Dummy Movie", "00:00")  

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__allocate_seats(id)

    def __allocate_seats(self, id):
        seats = [['O' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, show_id, seat_list):
        if show_id not in [show[0] for show in self.__show_list]:
            print("Error: Invalid show ID.")
            return

        seats = self.__seats.get(show_id)
        for seat in seat_list:
            row, col = seat
            if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                if seats[row - 1][col - 1] == 'O':
                    seats[row - 1][col - 1] = 'X'
                else:
                    print(f"Seat at row {row}, column {col} is already booked.")
            else:
                print(f"Error: Invalid seat at row {row}, column {col}.")

    def view_show_list(self):
        print("Show List:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in [show[0] for show in self.__show_list]:
            print("Error: Invalid show ID.")
            return

        seats = self.__seats.get(show_id)
        print("Available Seats:")
        for i in range(self.__rows):
            for j in range(self.__cols):
                if seats[i][j] == 'O':
                    print(f"Row {i + 1}, Column {j + 1}")


cinema = Star_Cinema()

hall1 = Hall(5, 10, 1)
hall2 = Hall(6, 8, 2)

cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

hall1.entry_show("show1", "Avengers", "15:00")
hall1.entry_show("show2", "Joker", "18:00")
hall2.entry_show("show3", "Inception", "20:00")

hall1.book_seats("show1", [(1, 1), (2, 2), (3, 3)])
hall1.book_seats("show1", [(1, 1), (2, 2), (3, 3)])  

hall1.view_show_list()
hall1.view_available_seats("show1")
